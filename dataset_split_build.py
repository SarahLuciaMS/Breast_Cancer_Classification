# Since we are building new paths for each image and shuffling them to have an adequate split, we will need the following:

from cancernet import config
from imutils import paths 
import random, shutil, os 

paths_original = list(paths.list_images(config.INPUT_DATASET)) 
random.seed(42)
random.shuffle(paths_original)

print("Total images found:", len(paths_original))

print("First three shuffled paths:") # just to make sure paths are working properly
for paths in paths_original[:3]:
    print(paths)

index = int(len(paths_original) * config.TRAIN_SPLIT) # refer to the comm in config.py to understand the split
train_paths = paths_original[:index]
test_paths = paths_original[index:]

index = int(len(train_paths) * config.VAL_SPLIT)
val_paths = train_paths[:index]
train_paths = train_paths[index:]

dataset_split = [("training", train_paths, config.TRAIN_PATH), 
                 ("validating", val_paths, config.VAL_PATH),
                 ("testing", test_paths, config.TEST_PATH)
]

print("Val images:", len(val_paths)) # just to make sure the split was done properly 
print("Test images:", len(test_paths))
print("Train images:", len(train_paths))
print("Check it all adds up:", len(val_paths) + len(test_paths) + len(train_paths))

for (split_type, original_path, base_path) in dataset_split: 
    print(f"Building {split_type} set")

    if not os.path.exists(base_path): 
        print(f"Building directory {base_path}")
        os.makedirs(base_path)

    for path in original_path:
        file = path.split(os.path.sep)[-1]
        label = file[-5:-4] # this will specify only the class (0, 1) of each component in the split sets 

        label_path = os.path.sep.join([base_path, label])
        if not os.path.exists(label_path):
            print(f"Building {label_path} directory:")
            os.makedirs(label_path)

            final_path = os.path.sep.join([label_path, file]) 
            shutil.copy2(path, final_path)

            
        








    

