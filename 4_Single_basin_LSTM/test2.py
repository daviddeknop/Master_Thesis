import xarray as xr

# Define the file path
file_path = r"E:\Users\ddknop\neuralhydrology_2_updated\output_caravan\timeseries\netcdf\6\6.nc"

# Open the NetCDF file using xarray
data = xr.open_dataset(file_path)

# Access the 'streamflow' variable
streamflow = data['streamflow'].values

# Find the first non-zero value in the streamflow array
first_non_zero = next((x for x in streamflow.flatten() if x > 0), None)

# Print the result
print("First non-zero value of 'streamflow':", first_non_zero)

# Close the dataset
data.close()
