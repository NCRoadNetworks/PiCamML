import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import Model
from keras_tuner.tuners import RandomSearch
from keras_tuner.engine.hyperparameters import HyperParameters
from tensorflow.keras.preprocessing.image import ImageDataGenerator