import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from prophet import Prophet
import matplotlib.pyplot as plt

PROJECT = Path(r"C:\Users\lenovo\Downloads\EV_charging_project")

train = pd.read_csv(
    PROJECT / "train_daily.csv",
    parse_dates=["start_timestamp"]
)

test = pd.read_csv(
    PROJECT / "test_daily.csv",
    parse_dates=["start_timestamp"]
)

# -----------------------------
# Prepare data for Prophet
# -----------------------------
prophet_train = train[
    ["start_timestamp", "energy_kwh"]
].rename(
    columns={
        "start_timestamp": "ds",
        "energy_kwh": "y"
    }
)

# -----------------------------
# Build Prophet model
# -----------------------------
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False,
    seasonality_mode="additive",
    changepoint_prior_scale=0.05
)

model.fit(prophet_train)

# -----------------------------
# Forecast TEST period
# -----------------------------
future = test[
    ["start_timestamp"]
].rename(
    columns={"start_timestamp": "ds"}
)

forecast = model.predict(future)

pred = forecast["yhat"].values
actual = test["energy_kwh"].values

# -----------------------------
# Metrics
# -----------------------------
rmse = np.sqrt(
    mean_squared_error(actual, pred)
)

mape = (
    mean_absolute_percentage_error(actual, pred)
    * 100
)

print("\n==============================")
print("       PROPHET RESULTS")
print("==============================")

print(f"RMSE : {rmse:,.2f} kWh")
print(f"MAPE : {mape:.2f}%")

# -----------------------------
# Save predictions
# -----------------------------
predictions = pd.DataFrame({
    "date": test["start_timestamp"],
    "actual_energy_kwh": actual,
    "prophet_predicted_energy_kwh": pred
})

predictions.to_csv(
    PROJECT / "prophet_test_predictions.csv",
    index=False
)

# -----------------------------
# Save metrics
# -----------------------------
metrics = pd.DataFrame([{
    "model": "Prophet",
    "RMSE_kWh": rmse,
    "MAPE_percent": mape
}])

metrics.to_csv(
    PROJECT / "prophet_metrics.csv",
    index=False
)

# -----------------------------
# Plot
# -----------------------------
plt.figure(figsize=(12, 5))

plt.plot(
    test["start_timestamp"],
    actual,
    label="Actual"
)

plt.plot(
    test["start_timestamp"],
    pred,
    label="Prophet Forecast",
    linewidth=2
)

plt.title(
    "Prophet — EV Charging Energy Demand Forecast"
)

plt.xlabel("Date")
plt.ylabel("Energy Demand (kWh)")
plt.legend()

plt.tight_layout()

plt.savefig(
    PROJECT / "prophet_test_forecast.png",
    dpi=160
)

plt.show()

print("\nFiles created:")
print("prophet_test_predictions.csv")
print("prophet_metrics.csv")
print("prophet_test_forecast.png")