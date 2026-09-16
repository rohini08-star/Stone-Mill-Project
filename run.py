import uvicorn
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from src.config import API_HOST, API_PORT
from src.utils.logger import logger

if __name__ == "__main__":
    logger.info(f"Starting SMART DUST CONTROL FastAPI server on http://{API_HOST}:{API_PORT}...")
    uvicorn.run("backend.main:app", host=API_HOST, port=API_PORT, reload=True)
