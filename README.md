# 🌪️ Storm Events Damage Prediction  
**Repository:** [ngabrielaxej/Stormevents_Damage_Prediction](https://github.com/ngabrielaxej/Stormevents_Damage_Prediction)

A machine-learning pipeline to predict property and crop damage from storm events, using structured event data and textual narratives.

---

## 📘 Table of Contents  
- [Overview](#-overview)  
- [Project Objectives](#-project-objectives)  
- [Data Description](#-data-description)  
- [Repository Structure](#-repository-structure)  
- [Installation](#-installation)  
- [Usage](#-usage)  
- [Modeling](#-modeling)  
- [Results](#-results)  
- [Next Steps](#-next-steps)  
- [Contributors](#-contributors)  
- [License](#-license)  

---

## 🧠 Overview  
This project implements a full pipeline for **predicting damages** (to crops and properties) from storm events documented in large datasets. The pipeline integrates:  
- structured attributes (e.g., event type, location, time)  
- unstructured text (event narratives)  
- machine-learning models for regression of damage amounts  

Ideal for risk modelling, disaster-impact analysis, and forecasting.

---

## 🎯 Project Objectives  
- Clean, integrate, and preprocess storm-event datasets  
- Extract features from textual descriptions of events  
- Build and evaluate regression models to predict damage  
- Provide interpretability and insights into the models (e.g., feature importance)  
- Prepare the workflow for reuse and extension  

---

## 🧾 Data Description  
The data originates from storm-event tracking sources and includes key fields such as:  
- `EVENT_TYPE` – type of disaster (e.g., tornado, flood)  
- `BEGIN_LAT`, `BEGIN_LON`, `END_LAT`, `END_LON` – geographical coordinates  
- `BEGIN_DATE_TIME`, `END_DATE_TIME` – timestamps of the event  
- `EPISODE_NARRATIVE`, `EVENT_NARRATIVE` – textual description of the event  
- `DAMAGE_PROPERTY`, `DAMAGE_CROPS` – target variables (estimated damage)  
- additional indicators (wind speed, hail size, etc) and derived features  


---

## 📁 Repository Structure  

📂 storm_damage_pipeline/\
│\
├── data/                 # Raw and processed datasets\
├── notebooks/            # Exploratory analysis & model experiments\
├── models/               # Trained models and checkpoints\
├── artifacts/            # Outputs, logs, and feature importances\
├── storm_damage_pipeline.py  # Main script for pipeline execution\
└── utils/                # Helper functions for preprocessing and NLP\



## ⚙️ Installation  
Clone the repository and install dependencies:

git clone https://github.com/ngabrielaxej/Stormevents_Damage_Prediction.git
cd Stormevents_Damage_Prediction
pip install -r requirements.txt

## 🧭 Usage

To run the main pipeline:\
python storm_damage_pipeline.py \
  --input "data/StormEvents_details-ftp_v1.0_d2013.csv" \
  --outdir "./artifacts" \
  --model ridge \
  --sample 20000 \
  --tfidf 20000


## 🤖 Modeling

Models implemented include:

**Ridge Regression** – a reliable linear baseline

**Random Forest Regressor** – non-linear tree-based model

**TabTransformer** – advanced model combining categorical, numeric & text embeddings

Model interpretability is provided via SHAP values

## 📈 Results



## 🚀 Future Work/Limitation

- Enhance NLP pipeline (e.g., entity extraction, context embedding)

- Incorporate geospatial features (proximity to coast, elevation, infrastructure)

- Build web-service/API for real-time predictions

- Expand dataset to include more years and event types

- Deploy model to cloud or container for production use

## 👥 Contributors
Nathania Gabriela
Duc-Anh Nguyen

## 📄 License

This project is licensed under the MIT License


## 🌍 Acknowledgments

Data provided by storm-event tracking source NOAA.
Thanks to the open-source community and contributors for tools and libraries used in this project.

