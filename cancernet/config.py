import os 

INPUT_DATASET = "datasets/original" # path to where you store the Kaggle dataset

BASE_PATH = "datasets/idc" # new dataset to be built
TRAIN_PATH = os.path.sep.join([BASE_PATH, "training"])
VAL_PATH = os.path.sep.join([BASE_PATH, "validation"])
TEST_PATH = os.path.sep.join([BASE_PATH, "testing"])

TRAIN_SPLIT = 0.8 # 80% of the images will be used to train the model (10% of this will be used to validate), and the remaining 20% used for testing 
VAL_SPLIT = 0.1

print("Configuration successfull:", BASE_PATH)
