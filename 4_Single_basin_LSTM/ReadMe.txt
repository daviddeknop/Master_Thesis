If you want to work with your own processed Caravan data, you should copy the output folder from step 2_River_to_Caravan,
named output_caravan_"name_catchment", into this folder. After copying, you should run the script Changing_foldername.py.

Alternatively, you can bypass this step by running the script Loading_input_data.py, which is located in the LOADING INPUT
folder. This script will directly load and prepare the input data without the need for manual copying and conversion.

To train the model, run the script train_"catchment".py.

To reproduce the results presented in this thesis, it is important to initialize the model with the following random seeds:
42, 512, and 10000. These seeds ensure the consistency and replicability of the results.The seed values can be modified
in the corresponding configuration file named config_z_fixed_seed_"catchment".yml.

The evaluation of the trained models is conducted within the Evaluation_results folder. The script Evaluation.py is used 
to assess the performance of individual model runs. In addition, the Jupyter notebook evaluation_ens.ipynb is used to compute
the ensemble means across multiple model runs.

It is important to note that each time a model is executed, a corresponding output directory is automatically generated in
the runs folder. The name of this directory is randomly generated and based on the timestamp at which the model was executed.
As a result, users are required to manually specify the correct run folder name in the relevant scripts or notebooks,
at the locations indicated with three dots (...).