# EV-Charging-Analytics
# ⚡ EV Charging Demand Forecasting

An end-to-end data analytics and time-series forecasting project that analyzes historical EV charging activity and forecasts future charging demand.

The project transforms raw EV charging session data into a cleaned time-series dataset, performs exploratory analysis, compares multiple forecasting approaches, generates 30/90/365-day forecasts, and presents the results through an interactive Power BI dashboard.

---

## 📌 Project Overview

The growth of electric vehicles is increasing the demand for reliable charging infrastructure.

This project aims to answer:

- How has EV charging demand changed over time?
- What are the weekly and monthly demand patterns?
- Are weekdays busier than weekends?
- Which forecasting model performs best?
- What could charging demand look like in 2025?
- How can forecast results support charging infrastructure planning?

---

## 🎯 Objectives

1. Clean and preprocess raw EV charging session data.
2. Convert session-level data into a daily time series.
3. Perform exploratory data analysis (EDA).
4. Identify weekly, monthly, and yearly demand patterns.
5. Compare multiple forecasting models.
6. Evaluate models using RMSE and MAPE.
7. Generate 30-day, 90-day, and 365-day forecasts.
8. Build an interactive Power BI dashboard.
9. Extract actionable business insights.

---

## 🗂️ Dataset

The dataset contains EV charging session records including information such as:

- Charging session ID
- Start timestamp
- End timestamp
- Energy consumed
- Charging cost
- Station information
- Charger information

### Time Period

**January 2022 – December 2024**

### Dataset Size

Approximately **294,000 charging sessions**.

The session-level data was aggregated into a daily time series.

---

## 🧹 Data Cleaning & Preparation

The following preprocessing steps were performed:

- Removed duplicate charging sessions.
- Removed records with missing timestamps.
- Removed records with missing energy values.
- Removed invalid/non-positive energy consumption.
- Converted timestamps to datetime format.
- Aggregated charging sessions by day.
- Calculated total daily energy consumption.
- Calculated average session energy.
- Calculated total daily charging cost.
- Created calendar features.

### Final Daily Dataset

The processed dataset contains:

- `date`
- `charging_sessions`
- `energy_kwh`
- `avg_session_energy_kwh`
- `total_cost`
- `day_of_week`
- `day_of_week_num`
- `week`
- `month`
- `month_name`
- `quarter`
- `year`
- `is_weekend`

There are **1,096 daily observations** covering 2022–2024.

---

# 📊 Exploratory Data Analysis

Several patterns were identified during analysis.

### Year-over-Year Growth

Average daily energy demand increased significantly:

| Year | Average Daily Energy |
|------|----------------------:|
| 2022 | 5,511.86 kWh |
| 2023 | 11,093.49 kWh |
| 2024 | 21,168.83 kWh |

This represents approximately:

- **101.3% growth from 2022 → 2023**
- **90.8% growth from 2023 → 2024**

---

### Weekday vs Weekend

Average demand:

| Day Type | Average Demand |
|----------|---------------:|
| Weekday | 13,650.77 kWh |
| Weekend | 9,980.40 kWh |

Weekend demand was approximately **26.9% lower** than weekday demand.

This indicates a strong weekly demand pattern.

---
---

## 🧪 Model Evaluation Methodology

To ensure a fair comparison between forecasting approaches, models should be evaluated using a consistent time-series validation strategy.

### Evaluation Strategy

* **Chronological split:** Keep training observations earlier than testing observations to preserve the temporal order of the data.
* **Forecast horizon:** Evaluate models over the same forecast period wherever possible.
* **Baseline comparison:** Compare advanced models against a simple baseline, such as predicting demand using the previous week's corresponding day.
* **Consistent evaluation:** Calculate evaluation metrics on the same test observations for all compared models.

### Evaluation Metrics

| Metric | Description                    | Interpretation                                                                |
| ------ | ------------------------------ | ----------------------------------------------------------------------------- |
| RMSE   | Root Mean Squared Error        | Penalizes larger forecasting errors more heavily.                             |
| MAPE   | Mean Absolute Percentage Error | Expresses average absolute percentage error.                                  |
| MAE    | Mean Absolute Error            | Measures the average absolute difference between actual and predicted demand. |

### Model Selection

The preferred model should demonstrate reliable performance on held-out observations while producing forecasts that are useful for charging infrastructure planning.

Model selection should consider forecasting accuracy, stability, and the practical implications of prediction errors.

> **Note:** The actual train-test split, evaluation period, baseline configuration, and metric values should be documented based on the implemented forecasting pipeline.

# 🤖 Forecasting Models

Three major forecasting approaches were evaluated.

## 1. SARIMA

A seasonal ARIMA model was implemented with weekly seasonality.

Configuration:

```text
ARIMA Order:
(1, 1, 1)

Seasonal Order:
(1, 1, 1, 7)
