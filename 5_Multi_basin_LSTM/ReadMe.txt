If you want to work with your own processed Caravan data, you should copy the output folder from step 2_River_to_Caravan, named
output_caravan_"name_catchment", into this directory. After copying, you must download the Caravan dataset, which can be found
at DOI: 10.5281/zenodo.14673536. Once downloaded, you can merge your catchment data with the Caravan dataset.

According to the type of experiment you wish to conduct:

Gauged basin simulation: Central European catchments
Rename output_caravan_"name_catchment" to output_caravan_EU if you are conducting the experiment on the Zwalm, and to
output_caravan_EU_bellebeek for the Bellebeek. Then, run the following scripts in sequence: Extract_codes_for_EU.py,
organize_attributes_caravan_EU.py, organize_timeseries_EU.py, and Make_pkl_files_for_split_EU.py.

Gauged basin simulation: USA catchments
Rename output_caravan_"name_catchment" to output_caravan_US when running the experiment on the Zwalm. Then, execute the following scripts:
Extract_codes_for_USA.py, organize_attributes_caravan_USA.py, organize_timeseries_USA.py, and Make_pkl_files_for_split_USA.py.

Gauged basin simulation: area-filtered Caravan dataset
Rename output_caravan_"name_catchment" to output_caravan when running the experiment on the Zwalm. Then run the 
scripts in the adapting_caravan folder in the following order: attributes_for_filters.ipynb, timeseries_for_filters.ipynb, 
and Make_pkl_files_for_split_area.py.

Gauged basin simulation: size- and area-filtered Caravan dataset
Follow the same procedure as in (3).

Ungauged basin simulation (Central European catchments)
Follow the same procedure as in (1).

Alternatively, you can bypass all of these steps by running the script Loading_input_data.py, located in the LOADING INPUT folder. 
This script will directly load and prepare the input data without requiring manual copying or conversion.

To train the model, run one of the train_"...".py scripts, depending on the specific experiment you are conducting.

To reproduce the results presented in this thesis, it is essential to initialize the models using the following random seeds:
42, 512, and 10000. These seeds ensure consistency and reproducibility of the results. The seed values can be modified in the 
corresponding configuration file of the experiment.

The evaluation of the trained models is performed in the Evaluation_results folder. The script evaluation.py is used to assess 
the performance of individual model runs. Additionally, the Jupyter notebook evaluation_ensemble_mean.ipynb is used to compute 
the ensemble means across multiple model executions.

It is important to note that each time a model is executed, a corresponding output directory is automatically created in the runs folder. 
The name of this directory is randomly generated based on the timestamp of execution. Consequently, users must manually specify the correct 
run folder name in the relevant scripts or notebooks, at the locations indicated with three dots (...).