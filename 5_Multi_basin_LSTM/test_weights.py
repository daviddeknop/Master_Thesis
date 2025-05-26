import torch
from neuralhydrology.utils.config import Config
from neuralhydrology.modelzoo import get_model
from pathlib import Path

# Defineer de paden naar je configuratiebestand en checkpointbestand
config_path = Path(r"E:\Users\ddknop\LSTM_CARAVAN\config_z.yml")
checkpoint_path = Path(r"E:\Users\ddknop\LSTM_CARAVAN\runs\CARAVAN_Basins_2412_122237\model_epoch001.pt")

# Laad de configuratie
config = Config(config_path)

# Initialiseer het model op basis van de configuratie
model = get_model(cfg=config)

# Laad de opgeslagen gewichten direct in het model
checkpoint = torch.load(checkpoint_path, map_location="cpu")  # Gebruik "cuda" als je een GPU gebruikt
model.load_state_dict(checkpoint)  # Direct laden zonder 'model_state_dict'

# Print de modelstructuur
print("Modelstructuur:\n")
print(model)

# Print the submodules of the model (to count layers)
print("\nModel submodules:")
for name, module in model.named_modules():
    print(f"{name}: {module}")

# Optionally, count the number of layers in specific components
input_gate_layers = sum(1 for layer in model.input_gate.children())
dynamic_gates_layers = sum(1 for layer in model.dynamic_gates.children())
embedding_net_layers = sum(1 for layer in model.embedding_net.children())
head_layers = sum(1 for layer in model.head.children())

print(f"\nNumber of layers in input_gate: {input_gate_layers}")
print(f"Number of layers in dynamic_gates: {dynamic_gates_layers}")
print(f"Number of layers in embedding_net: {embedding_net_layers}")
print(f"Number of layers in head: {head_layers}")

