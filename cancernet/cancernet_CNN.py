from tensorflow.keras.models import Sequential # this will be the kind of layering we will use
from tensorflow.keras.layers import BatchNormalization, Activation, MaxPooling2D, SeparableConv2D, Flatten, Dense, Dropout # config for our layers 
from tensorflow.keras import backend as K # usefull in case custom operations are needed

class CancerNet:
    @staticmethod
    def build(width, height, depth, classes):
        model = Sequential()
        shape = (height, width, depth)
        channelDim = -1 # makes sure the batch normalization is applied to the channels (depth) of the shape 

        if K.image_data_format == "channels_first": # Incase for any reason this will be run with anythign other than TensorFlow
            shape = (depth, width, height)
            channelDim = 1

        
