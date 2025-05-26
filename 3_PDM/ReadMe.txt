If you want to work with your own processed CARAVAN data, you should copy the output folder from step 2_River_to_Caravan,
 named output_caravan_"name_catchment", into this folder. After copying, you should run the script located in the folder
 data_conversion to convert the data to the required format.

Alternatively, you can bypass this step by running the script Loading_input_data.py, which is located in the LOADING INPUT
 folder. This script will directly load and prepare the input data without the need for manual copying and conversion.

The folder Hargreaves contains data generated using the Hargreaves method for estimating evapotranspiration. This data is
 not used in the hydrological models but is available for comparison purposes.

The file Final_version.ipynb runs the PDM and performs the final simulations and evaluations.