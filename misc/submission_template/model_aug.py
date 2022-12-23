import os
import tensorflow as tf
import joblib
from tensorflow.python.ops.numpy_ops import np_config
np_config.enable_numpy_behavior()
tfk = tf.keras
tfkl = tf.keras.layers

class dataAugmentation(tfkl.Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def call(self, inputs,training=None):
          return inputs

class model:
    def __init__(self, path):
        self.model = tf.keras.models.load_model(os.path.join(path, 'MODEL_NAME') , custom_objects={"data_augmentation": data_augmentation})
        self.path = path

    def predict(self, X):
        
        # Insert your preprocessing here
        scaler = joblib.load(os.path.join(self.path, 'scaler.gz'))
        X = scaler.transform(X.reshape(-1, X.shape[-1])).reshape(X.shape)

        out = self.model.predict(X)
        out = tf.argmax(out, axis=-1)

        return out
