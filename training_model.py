import matplotlib
matplotlib.use ("Agg")

import os
import numpy as np 
import matplotlib.pyplot as plt
from imutils import paths
from sklearn.metrics import confusion_matrix, classification_report
from cancernet import config, cancernet_CNN
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adagrad # will try using Adam afterwards to see which one performs better
from tensorflow.keras.callbacks import LearningRateScheduler
from tensorflow.keras.utils import to_categorical

epochsNum = 40
init_lr = 0.01
batchSize = 64

train_paths = list(paths.list_images(config.TRAIN_PATH))
len_train = len(train_paths)
len_val = len(list(paths.list_images(config.VAL_PATH_PATH)))
len_test = len(list(paths.list_images(config.TEST_PATH)))

train_labels = [int(p.split(os.path.sep)[:2]) for p in paths]
train_labels = to_categorical(train_labels)
class_total = train_labels.sum(axis = 0)
class_weight = class_total.max() / class_total # getting rid of imbalance 












