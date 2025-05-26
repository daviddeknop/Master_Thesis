import pandas as pd
from pathlib import Path
import pickle


path = Path('per_basin_train_periods_US.pkl')

# Load the pickle file as a dictionary
with open(path, 'rb') as file:
    training_periods = pickle.load(file)

# Optionally, convert to a pandas DataFrame if needed
df = pd.DataFrame.from_dict(training_periods, orient='index')

print(training_periods['10026301']['start_dates'])


path = Path('per_basin_validation_periods_US.pkl')
df = pd.read_pickle(path)

print(df)

path = Path('train_Zwalm.pkl')
df = pd.read_pickle(path)

print(df)

