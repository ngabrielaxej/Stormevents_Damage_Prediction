# 🌪️ Damage by storm events prediction

A machine learning pipeline for **predicting property and crop damages** caused by natural disasters (e.g., storms, floods, tornadoes).  
The project integrates **structured data** (e.g., location, time, magnitude) and **unstructured text data** (event narratives) using **NLP, feature engineering, and regression models**.

---

## 📘 Table of Contents
- [Overview](#-overview)
- [Project Objectives](#-project-objectives)
- [Data Description](#-data-description)
- [Pipeline Overview](#-pipeline-overview)
- [Installation](#-installation)
- [Usage](#-usage)
- [Modeling](#-modeling)
- [Results](#-results)
- [Next Steps](#-next-steps)
- [Contributors](#-contributors)
- [License](#-license)

---

## 🧠 Overview

This project focuses on developing a predictive model for estimating damages from natural disaster events.  
We combine:
- **Tabular features:** location, date, event type, intensity
- **Text features:** event narratives describing causes and consequences
- **Target:** total damages on crops and properties

The model can be used to estimate potential losses for new events or simulate risk under different scenarios.

---

## 🎯 Project Objectives

- Preprocess and integrate structured and unstructured disaster event data  
- Extract key insights from textual event descriptions using NLP  
- Train and evaluate regression models for damage prediction  
- Provide explainable insights using SHAP feature importance  

---

## 🧾 Data Description

The dataset is based on **NOAA Storm Events** and includes:

| Column Name | Description |
|--------------|-------------|
| `EVENT_TYPE` | Type of natural disaster (e.g., Tornado, Flood, Hail) |
| `BEGIN_LAT`, `BEGIN_LON` | Starting coordinates of the event |
| `END_LAT`, `END_LON` | Ending coordinates of the event |
| `EVENT_NARRATIVE`, `EPISODE_NARRATIVE` | Text descriptions of the event |
| `DAMAGE_PROPERTY`, `DAMAGE_CROPS` | Reported damage estimates |
| `BEGIN_DATE_TIME`, `END_DATE_TIME` | Temporal information |
| Other indicators: `BEGIN_RANGE`, `BEGIN_AZIMUTH`, `LOCATION`, etc. |

---

## 🧩 Pipeline Overview

```bash
📂 storm_damage_pipeline/
│
├── data/                 # Raw and processed datasets
├── notebooks/            # Exploratory analysis & model experiments
├── models/               # Trained models and checkpoints
├── artifacts/            # Outputs, logs, and feature importances
├── storm_damage_pipeline.py  # Main script for pipeline execution
└── utils/                # Helper functions for preprocessing and NLP
