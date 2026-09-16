import time
import sys
from pathlib import Path

# Ensure src modules can be imported
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from src.data.generate_dataset import generate_stone_mill_dataset
from src.data.clean_data import clean_stone_mill_data
from src.data.preprocess import preprocess_and_split
from src.data.eda import generate_eda_charts
from src.models.train_all import train_and_evaluate_all
from src.utils.logger import logger
from backend.database import engine, Base, SessionLocal
from backend.models import SensorReading
import pandas as pd
from src.config import CLEANED_DATA_PATH

def run_complete_pipeline():
    logger.info("=========================================================")
    logger.info("  STARTING SMART DUST CONTROL COMPLETE PIPELINE EXECUTION")
    logger.info("=========================================================")
    start_time = time.time()

    # Step 1: Generate Raw Dataset (50,000 rows)
    logger.info("\n--- STEP 1: SYNTHETIC DATASET GENERATION ---")
    generate_stone_mill_dataset()

    # Step 2: Clean Dataset & Quality Report
    logger.info("\n--- STEP 2: DATA CLEANING & QUALITY REPORTING ---")
    clean_stone_mill_data()

    # Step 3: Feature Engineering & Preprocessing Split
    logger.info("\n--- STEP 3: PREPROCESSING & TRAIN/VAL/TEST SPLITTING ---")
    preprocess_and_split()

    # Step 4: Exploratory Data Analysis (EDA) Charts
    logger.info("\n--- STEP 4: GENERATING EDA CHARTS ---")
    generate_eda_charts()

    # Step 5: Machine Learning Model Training & Metrics Generation
    logger.info("\n--- STEP 5: TRAINING MACHINE LEARNING MODELS ---")
    train_and_evaluate_all()

    # Step 6: Database Initialization & Seeding
    logger.info("\n--- STEP 6: SEEDING SQLITE DATABASE ---")
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        count = db.query(SensorReading).count()
        if count == 0 and CLEANED_DATA_PATH.exists():
            df_clean = pd.read_csv(CLEANED_DATA_PATH).tail(500)
            df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'])
            readings = []
            for _, row in df_clean.iterrows():
                r = SensorReading(**row.to_dict())
                readings.append(r)
            db.bulk_save_objects(readings)
            db.commit()
            logger.info(f"Database seeded with {len(readings)} initial sensor readings.")
        else:
            logger.info(f"Database already contains {count} sensor readings.")
    finally:
        db.close()

    elapsed = time.time() - start_time
    logger.info("=========================================================")
    logger.info(f"  PIPELINE EXECUTION COMPLETED IN {elapsed:.2f} SECONDS")
    logger.info("=========================================================")

if __name__ == "__main__":
    run_complete_pipeline()
