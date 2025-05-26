import pickle
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import torch
from neuralhydrology.evaluation import metrics
from neuralhydrology.nh_run import start_run, eval_run
area = 111639970.52
#evaluate model
run_dir = Path('runs/CARAVAN_Basins_2503_115152')
for i in range(1, 21):
    eval_run(epoch = i,run_dir=run_dir, period="test")

# Base directory containing the test results
base_dir = Path('runs/CARAVAN_Basins_2503_115152/test')

# Initialize variables to track the best NSE and the corresponding epoch
max_nse = -float('inf')  # Set to negative infinity initially
best_epoch = None

# Loop through epochs 1 to 50
for i in range(1, 21):  # Epochs 1 to 50
    # Format the folder name for the current epoch
    epoch_folder = base_dir / f"model_epoch{i:03d}"
    metrics_file = epoch_folder / "test_metrics.csv"

    # Check if the test_metrics.csv file exists
    if not metrics_file.exists():
        print(f"test_metrics.csv file not found for epoch {i}. Skipping...")
        continue

    # Load the CSV file into a DataFrame
    df = pd.read_csv(metrics_file)

    # Extract the NSE value from the dataframe (assuming NSE is in a column named 'NSE')
    if 'NSE' in df.columns:
        nse_value = df['NSE'].iloc[0]  # Assuming NSE is on the first row
        print(f"Epoch {i}: NSE = {nse_value:.4f}")

        # Check if this is the highest NSE found so far
        if nse_value > max_nse:
            max_nse = nse_value
            best_epoch = i

# Output the best epoch and its NSE value
if best_epoch is not None:
    print(f"\nThe epoch with the highest NSE is Epoch {best_epoch} with an NSE value of {max_nse:.4f}")
else:
    print("No NSE values found.")

#%%
# fill in  with best epoch
with open(run_dir / "test" / "model_epoch019" / "test_results.p", "rb") as fp:
    results = pickle.load(fp)

qobs = results['6']['1D']['xr']['streamflow_obs']*area/(1000*3600*24)
qsim = results['6']['1D']['xr']['streamflow_sim']*area/(1000*3600*24)

fig, ax = plt.subplots(figsize=(16,10))
ax.plot(qobs['date'], qobs)
ax.plot(qsim['date'], qsim)
ax.set_ylabel("Discharge (m³/s)")
ax.set_title(f"Test period - NSE {results['6']['1D']['NSE']:.3f}")

    #data properties

values = metrics.calculate_all_metrics(qobs.isel(time_step=-1), qsim.isel(time_step=-1))
for key, val in values.items():
    print(f"{key}: {val:.3f}")
# %%
