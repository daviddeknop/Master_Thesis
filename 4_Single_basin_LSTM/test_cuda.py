import torch

if torch.cuda.is_available():
    print("CUDA is available. You have a CUDA-capable GPU.")
else:
    print("CUDA is not available. You do not have a CUDA-capable GPU.")