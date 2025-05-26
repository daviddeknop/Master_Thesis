import os


current_cwd = os.getcwd()
old_path = os.path.join(current_cwd, "output_caravan_zwalm", "timeseries", "netcdf", "vlaamsebekken")
new_path = os.path.join(current_cwd, "output_caravan_zwalm", "timeseries", "netcdf", "6")

os.path.exists(old_path)
os.rename(old_path, new_path)


old_path = os.path.join(current_cwd, "output_caravan_zwalm", "timeseries", "csv", "vlaamsebekken")
new_path = os.path.join(current_cwd, "output_caravan_zwalm", "timeseries", "csv", "6")

os.path.exists(old_path)
os.rename(old_path, new_path)


current_cwd = os.getcwd()
old_path = os.path.join(current_cwd, "output_caravan_bellebeek", "timeseries", "netcdf", "vlaamsebekken")
new_path = os.path.join(current_cwd, "output_caravan_bellebeek", "timeseries", "netcdf", "7")

os.path.exists(old_path)
os.rename(old_path, new_path)


old_path = os.path.join(current_cwd, "output_caravan_bellebeek", "timeseries", "csv", "vlaamsebekken")
new_path = os.path.join(current_cwd, "output_caravan_bellebeek", "timeseries", "csv", "7")

os.path.exists(old_path)
os.rename(old_path, new_path)



