import torch
from neuralhydrology.utils.config import Config
from neuralhydrology.modelzoo import get_model
from pathlib import Path

# Defineer de paden naar je configuratiebestand en checkpointbestand
config_path = Path(r"E:\Users\ddknop\neuralhydrology_2_updated\config_z.yml")
checkpoint_path = Path(r"E:\Users\ddknop\neuralhydrology_2_updated\runs\Zwalm_2312_125351\model_epoch039.pt")
checkpoint_path = Path(r"E:\Users\ddknop\neuralhydrology_2_updated\runs\Zwalm_2301_165653\model_epoch003.pt")

# Laad de configuratie
config = Config(config_path)
print(config)

# Initialiseer het model op basis van de configuratie
model = get_model(cfg=config)
print(model)
# Laad de opgeslagen gewichten direct in het model
checkpoint = torch.load(checkpoint_path, map_location="cpu")  # Gebruik "cuda" als je een GPU gebruikt
print(checkpoint.keys())
model.load_state_dict(checkpoint)  # Direct laden zonder 'model_state_dict'

# Print de modelstructuur
print("Modelstructuur:\n")
print(model)

# Print de modelparameters
print("\nModelparameters:")
for name, param in model.named_parameters():
    print(f"{name}: {param.shape}")

# Print the number of layers in the LSTM
num_layers = model.lstm.num_layers
print(f"The LSTM has {num_layers} layers.")
