# SMART DUST CONTROL

### SMART ADAPTIVE DUST EXTRACTION AND POWDER RECOVERY SYSTEM FOR STONE MILLS

An end-to-end professional industrial software and intelligent monitoring prototype for stone mills and powder processing facilities.

---

## 1. Project Overview
**SMART DUST CONTROL** is an intelligent decision-support platform designed to monitor stone mill operating parameters, predict outlet dust emissions, estimate powder recovery, classify equipment maintenance risks, detect anomalies, and dynamically optimize blower fan extraction settings.

---

## 2. Problem Statement
Stone mills frequently experience airborne dust hazards, inefficient static dust extraction, energy waste from blowers running at full speed, fine powder product loss, filter clogging, and mechanical equipment wear.

---

## 3. Key Objectives
- **Dust Emission Control**: Minimize outlet dust concentrations below safety thresholds.
- **Powder Recovery Maximization**: Reclaim valuable fine mineral powder from baghouse collectors.
- **Energy Optimization**: Reduce blower power consumption by adapting extraction setpoints to real-time mill loads.
- **Equipment Health Maintenance**: Monitor motor temperatures, filter clogging, and vibration levels to prevent unplanned downtime.

---

## 4. Key Features
- **Synthetic Data Engine**: 50,000 sensor observations generated with physical non-linear relationships.
- **Data Cleaning & Quality Pipeline**: Automated schema validation, bounds checking, and data quality report generation.
- **Machine Learning Architecture**:
  - Model 1: Dust Prediction Regressor (`outlet_dust_mg_m3`)
  - Model 2: Powder Recovery Regressor (`recovered_powder_kg_hr`)
  - Model 3: Maintenance Risk Classifier (`NORMAL` / `WARNING` / `CRITICAL`)
  - Model 4: IsolationForest Anomaly Detector
- **Adaptive Extraction Optimizer**: Multi-objective grid search optimization balancing dust, recovery, power, and stress.
- **Digital Twin Simulator**: Dynamic software simulation of stone mill operation with parameter sliders.
- **FastAPI Backend**: Async REST API with OpenAPI documentation (`/docs`).
- **SQLite Database**: SQLAlchemy ORM persistence storing sensors, predictions, alerts, and metrics.
- **Industrial Web Dashboard**: Responsive dark glassmorphism UI with live Plotly.js charts.

---

## 5. System Architecture
```
[ Web Dashboard UI ] <---> [ FastAPI REST Backend ] <---> [ ML Models & Optimizer ] <---> [ SQLite Database ]
```

---

## 6. Technology Stack
- **Language**: Python 3.11
- **Machine Learning**: Scikit-Learn, XGBoost, Joblib
- **Data Analysis**: Pandas, NumPy, Matplotlib, Seaborn
- **Backend API**: FastAPI, Uvicorn, Pydantic, SQLAlchemy
- **Database**: SQLite
- **Frontend**: HTML5, Vanilla CSS3 (Dark Glassmorphism Theme), Vanilla JS, Plotly.js
- **Testing & Containerization**: Pytest, Docker, Docker Compose

---

## 7. Dataset Specifications
- **Size**: 50,000 rows x 32 parameters
- **Variables**: Machine load, moisture, stone hardness, inlet/outlet dust, airflow, RPM, kW, differential pressure, filter clogging, vibration, motor temp, powder recovery rates.

---

## 8. Machine Learning Performance Summary
- **Dust Model**: $R^2 > 0.92$, low MAE/RMSE
- **Recovery Model**: $R^2 > 0.94$, precise powder estimation
- **Maintenance Risk Classifier**: Weighted F1-score $> 0.95$

---

## 9. Optimization Objective
$$\text{Score} = w_{\text{dust}} \cdot S_{\text{dust}} + w_{\text{rec}} \cdot S_{\text{rec}} + w_{\text{energy}} \cdot S_{\text{energy}} + w_{\text{stress}} \cdot S_{\text{stress}} - \text{Penalty}$$

---

## 10. API Endpoints
- `GET /` - Main Dashboard UI
- `GET /health` - Health Check
- `GET /dashboard/summary` - Live KPI Metrics
- `GET /sensors/history` - Time-Series Sensor History
- `POST /prediction/dust` - Dust Inference
- `POST /prediction/recovery` - Recovery Inference
- `POST /prediction/maintenance` - Risk Classification
- `POST /anomaly/detect` - Anomaly Detection
- `POST /optimize/extraction` - Extraction Optimization
- `POST /simulation/run` - Digital Twin Simulation
- `GET /alerts` - Active System Alarms
- `GET /reports` - System Summary & Export

---

## 11. Industrial Web Dashboard Pages
1. **Live Dashboard** (`index.html`)
2. **Adaptive Control** (`adaptive_control.html`)
3. **Digital Twin** (`simulation.html`)
4. **ML Inference** (`prediction.html`)
5. **Analytics** (`analytics.html`)
6. **Maintenance** (`maintenance.html`)
7. **Reports** (`reports.html`)

---

## 12. Installation & Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Automated End-to-End Pipeline
```bash
python run_pipeline.py
```

### Step 3: Start Server & Dashboard
```bash
python run.py
```
Open `http://localhost:8000` in your web browser.

---

## 13. Running Tests
```bash
python -m pytest tests/ -v
```

---

## 14. Docker Deployment
```bash
docker-compose up --build -d
```

---

## 15. Project Folder Structure
```
stonemill/
├── data/ (raw, cleaned, processed, predictions)
├── notebooks/ (01_data_generation, 02_cleaning, 03_eda, 04_training)
├── src/ (data, features, models, optimization, simulation, utils)
├── models/ (.pkl trained model files)
├── backend/ (main.py, database.py, models.py, schemas.py, routers/)
├── frontend/ (index.html, css/, js/, pages)
├── reports/ (eda plots, metrics, generated HTML reports)
├── tests/ (pytest test suite)
├── docs/ (PROJECT_REPORT, ARCHITECTURE, API, DATA_DICTIONARY, INSTALLATION)
├── requirements.txt, Dockerfile, docker-compose.yml, run_pipeline.py, run.py
```

---

## 16. Engineering Safety Limitations
This software system is a **Decision-Support Engineering Prototype**. Predictions, recommendations, and simulations do not replace qualified engineering validation or hardware safety interlocks.

---

## 17. Future Enhancements
- Integration of physical OPC-UA / MQTT industrial IoT sensor feeds.
- Reinforcement Learning for closed-loop VFD fan speed control.

---

## 18. License
MIT License - Open for industrial research and educational prototyping.

---

## 19. Contact & Attribution
Developed by multidisciplinary industrial automation and software engineering team.
