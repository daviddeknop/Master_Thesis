# Master Thesis – Source Code Repository

This repository contains the source code developed for my master's thesis:  
**"DEEP LEARNING VS. CONCEPTUAL
RAINFALL-RUNOFF MODELS: A
COMPARATIVE STUDY"**

The work includes comparative experiments between a traditional conceptual hydrological model (PDM) and various Long Short-Term Memory (LSTM)-based deep learning models.
The code in the Resository is partely based on [Thesis](https://github.com/olivierbonte/master_thesis) and the Neuralhydrology Environment [NeuralHuydrology](https://github.com/neuralhydrology/neuralhydrology).

---

## Repository Structure

The project is organized by phase, following the flow of the thesis:

- `1_Conversion_river_shape`: Preprocessing shapefiles and hydrological boundaries  
- `2_River_to_Caravan`: Converting local hydrological data to Caravan-compatible format  
- `3_PDM`: Implementation and evaluation of the conceptual PDM hydrological model  
- `4_Single_basin_LSTM`: LSTM modeling for individual catchments  
- `5_Multi_basin_LSTM`: LSTM modeling across multiple catchments  

---

##  Software Setup
First, ensure that [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is installed on your local device. Then, download this repository as a ZIP file.
Open your command-line interface (or the Anaconda Prompt if `conda` is not in your system path), navigate to the folder where the desired `.yml` file is located.
Two separate conda environments are used:

### Environment 1: Preprocessing & Conversion & PDM
Supports geospatial and data preprocessing scripts from:

- `1_Conversion_river_shape`  
- `2_River_to_Caravan`  
- `3_PDM`  

**Installation:**
```bash
conda env create -f environment_1.yml
```
### Environment 2: LSTM Modeling

Supports deep learning model training, evaluation, and visualization for:

- `4_Single_basin_LSTM`  
- `5_Multi_basin_LSTM`  

**Installation:**
```bash
conda env create -f environment_2.yml
```
##  Loading Data

Each of the main phase directories (e.g., `1_Conversion_river_shape`, `2_River_to_Caravan`, etc.) contains a subdirectory named `LOADING INPUT`. This folder is essential for executing the scripts in that phase, as it holds the necessary input files specific to the corresponding processing step. The required data files are downloaded from the associated Zenodo repositories.

## ReadMe
Each main directory contains its own README file, providing more detailed and context-specific information related to the scripts and data within that section.
