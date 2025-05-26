import xarray as xr

# Specify the file path
current_cwd = os.getcwd()
file_path = current_cwd /'output_caravan' / 'timeseries' / 'netcdf' / '01013500' /'01013500.nc'


ds = xr.open_dataset(file_path)
print("Dataset successfully loaded!")

# Print the dataset summary
print(ds.head())