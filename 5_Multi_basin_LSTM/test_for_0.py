import xarray as xr

# Path to the NetCDF file
file_path = r"E:\Users\ddknop\LSTM_CARAVAN\output_caravan\timeseries\netcdf\6\6.nc"

# Open the NetCDF file
try:
    print(f"Opening NetCDF file: {file_path}")
    dataset = xr.open_dataset(file_path)
    
    # Print all variable names (columns)
    print("\nVariables in the dataset (column names):")
    print(list(dataset.data_vars))  # Print only data variables
    
    # Print all variables including coordinates
    print("\nAll variables including coordinates:")
    print(list(dataset.variables))
    
except FileNotFoundError:
    print(f"Error: File not found - {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

