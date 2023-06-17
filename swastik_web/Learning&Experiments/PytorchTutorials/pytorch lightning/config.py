# Training hyperparameters
INPUT_SIZE = 784
NUM_CLASSES = 10
LEARNING_RATE = 1e-3
BATCH_SIZE = 128
NUM_EPOCHS = 30

# Dataset
DATA_DIR = "dataset/"
NUM_WORKERS = 8

# Compute related
ACCELERATOR = "mps"
DEVICES = [0]
PRECISION = "16-mixed"