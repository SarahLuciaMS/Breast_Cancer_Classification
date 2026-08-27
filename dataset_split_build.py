# Since we are building new paths for each image and shuffling them to have an adequate split, we will need the following:

from cancernet import config # to get the config for the split we made earlier in a seperate file
from imutils import paths # to locate the paths of the images
import random, shutil, os # to shuffle the images and manage files and paths directly in your system

