#%%
import pickle
from pathlib import Path
import pandas as pd

import matplotlib.pyplot as plt
import torch
from neuralhydrology.evaluation import metrics
from neuralhydrology.nh_run import start_run, eval_run

def main():
    # by default we assume that you have at least one CUDA-capable NVIDIA GPU
    if torch.cuda.is_available():
        start_run(config_file=Path("config_exp_4_area_size.yml"))

    else:
        start_run(config_file=Path("config_exp_4_area_size.yml"), gpu=-1)

# %%
if __name__ == "__main__":
    main()
