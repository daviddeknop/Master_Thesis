import pandas as pd
from pathlib import Path
import pickle



preprocess_output_folder = Path('data/Zwalm_data/preprocess_output')
p_ep_zwalm = pd.read_pickle(preprocess_output_folder/'Final_Forcings_PDM.pkl')

print(p_ep_zwalm)


preprocess_output_folder = Path('data/Zwalm_data/preprocess_output')
p_ep_zwalm = pd.read_pickle(preprocess_output_folder/'p_ep_with_adaptions_ep.pkl')

print(p_ep_zwalm)
