# %%
import pickle
import pandas as pd

# Define file paths
input_file = "Traindata_with_zwalm_EU.txt"
output_file = "per_basin_train_periods_EU.pkl"

# Define time periods
default_period = [["30/06/1972", "24/11/2012"]]
special_period = [["30/06/1972", "24/11/2012"]]

# Initialize the dictionary for training periods
training_periods = {}

# Read the basin IDs from the input file
with open(input_file, "r") as file:
    basin_ids = [line.strip() for line in file if line.strip()]  # Remove empty lines and whitespace

# Assign periods to the basin IDs
for i, basin_id in enumerate(basin_ids):
    # Define the period based on the basin
    if i == 0:  # First basin gets the special period
        period = special_period
    else:  # All other basins get the default period
        period = default_period

    # Convert start and end dates to datetime objects
    start_date = pd.to_datetime(period[0][0], format="%d/%m/%Y")
    end_date = pd.to_datetime(period[0][1], format="%d/%m/%Y")

    # Add the start and end dates into lists, ensuring each basin has lists of dates
    training_periods[basin_id] = {
        'start_dates': [start_date],  # List of start dates as datetime objects
        'end_dates': [end_date],     # List of end dates as datetime objects
    }

# Save the dictionary to a .pkl file
with open(output_file, "wb") as pkl_file:
    pickle.dump(training_periods, pkl_file)

print(f"Training periods file created: {output_file}")



# %%import pickle

# %% 
import pickle
import pandas as pd

# Define file paths
input_file = "Traindata_with_zwalm_EU.txt"
output_file = "per_basin_validation_periods_EU.pkl"

# Define time periods
default_period = [["25/11/2012", "31/12/2022"]]
special_period = [["25/11/2012", "14/12/2017"]]

# Initialize the dictionary for validation periods
validation_periods = {}

# Read the basin IDs from the input file
with open(input_file, "r") as file:
    basin_ids = [line.strip() for line in file if line.strip()]  # Remove empty lines and whitespace

# Assign periods to the basin IDs
for i, basin_id in enumerate(basin_ids):
    # Define the period based on the basin
    if i == 0:  # First basin gets the special period
        period = special_period
    else:  # All other basins get the default period
        period = default_period

    # Convert start and end dates to datetime objects
    start_date = pd.to_datetime(period[0][0], format="%d/%m/%Y")
    end_date = pd.to_datetime(period[0][1], format="%d/%m/%Y")

    # Add the start and end dates into lists, ensuring each basin has lists of dates
    validation_periods[basin_id] = {
        'start_dates': [start_date],  # List of start dates as datetime objects
        'end_dates': [end_date],     # List of end dates as datetime objects
    }

# Save the dictionary to a .pkl file
with open(output_file, "wb") as pkl_file:
    pickle.dump(validation_periods, pkl_file)

print(f"Validation periods file created: {output_file}")







# %%
import pickle
import pandas as pd

# Define file paths
input_file = "Zwalm_code.txt"
output_file = "train_Zwalm.pkl"

# Define time periods
special_period = [["15/12/2017", "31/12/2022"]]

# Initialize the dictionary for training periods
training_periods = {}

# Read the basin IDs from the input file
with open(input_file, "r") as file:
    basin_ids = [line.strip() for line in file if line.strip()]  # Remove empty lines and whitespace

# Assign periods to the basin IDs
for i, basin_id in enumerate(basin_ids):
    # Define the period based on the basin
    if i == 0:  # First basin gets the special period
        period = special_period
    else:
        period = special_period  # Assuming all basins use the same period in this example

    # Convert start and end dates to datetime objects
    start_date = pd.to_datetime(period[0][0], format="%d/%m/%Y")
    end_date = pd.to_datetime(period[0][1], format="%d/%m/%Y")

    # Add the start and end dates into lists, ensuring each basin has lists of dates
    training_periods[basin_id] = {
        'start_dates': [start_date],  # List of start dates as datetime objects
        'end_dates': [end_date],     # List of end dates as datetime objects
    }

# Save the dictionary to a .pkl file
with open(output_file, "wb") as pkl_file:
    pickle.dump(training_periods, pkl_file)

print(f"Training periods file created: {output_file}")


