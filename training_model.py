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





