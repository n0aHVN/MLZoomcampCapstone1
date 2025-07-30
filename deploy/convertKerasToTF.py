import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('./models/xception_17_1.000.h5')

tf.saved_model.save(model, './deploy/fruit_prediction')