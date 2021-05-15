import tensorflow as tf
import unittest
import dlmri_tutorial
import numpy as np
import six

__all__ = ['cReLU',
           'ModReLU',
           'Identity',
           'get',
           'Cardioid',
         ]

def get(identifier):
    return Activation(identifier)

def Activation(identifier):
    if identifier is None:
        return Identity()
    if isinstance(identifier, six.string_types):
        identifier = str(identifier)
        return deserialize(identifier)
    elif callable(identifier):
        return identifier
    else:
        raise TypeError(
            'Could not interpret activation function identifier: {}'.format(
                identifier))

def deserialize(act):
    if act == 'ModReLU' or act == 'modrelu':
        return ModReLU()
    elif act == 'cReLU' or act == 'crelu':
        return cReLU()
    elif act == 'hard_sigmoid':
        return HardSigmoid()
    elif act == 'cardioid':
        return Cardioid()
    elif act is None or act == 'identity':
        return Identity()
    else:
        raise ValueError(f"Selected activation '{act}' not implemented in complex activations")

def serialize(act):
    return act.__name__


class HardSigmoid(tf.keras.layers.Layer):
    def __init__(self, bias=0.1, trainable=True):
        super().__init__()
        self.bias_init = bias
        self.trainable = trainable

    @property
    def __name__(self):
        return 'hard_sigmoid'

    def build(self, input_shape):
        super().build(input_shape)
        initializer = tf.keras.initializers.Constant(self.bias_init)
        self.bias = self.add_weight('bias',
                                      shape=(input_shape[-1]),
                                      initializer=initializer,
                                      )
    def call(self, z):
        return tf.cast(tf.keras.activations.hard_sigmoid(dlmri_tutorial.complex_abs(z) + self.bias), tf.complex64)
    
class cReLU(tf.keras.layers.Layer):
    def call(self, z):
        actre = tf.keras.activations.relu(tf.math.real(z))
        actim = tf.keras.activations.relu(tf.math.imag(z))
        return tf.complex(actre, actim)
        
    @property
    def __name__(self):
        return 'cReLU'
        
class Identity(tf.keras.layers.Layer):    
    @property
    def __name__(self):
        return 'identity'

    def call(self, z):
        return z

class ModReLU(tf.keras.layers.Layer):
    def __init__(self, bias=0.0, trainable=True):
        super().__init__()
        self.bias_init = bias
        self.trainable = trainable
    
    @property
    def __name__(self):
        return 'ModReLU'

    def build(self, input_shape):
        super().build(input_shape)
        initializer = tf.keras.initializers.Constant(self.bias_init)
        self.bias = self.add_weight('bias',
                                      shape=(input_shape[-1]),
                                      initializer=initializer,
                                      )
    def call(self, z):
        return tf.cast(tf.keras.activations.relu(dlmri_tutorial.complex_abs(z) + self.bias), tf.complex64) * dlmri_tutorial.complex_norm(z)

    def __str__(self):
        s = f"ModReLU: bias_init={self.bias_init}, trainable={self.trainable}"
        return s

class Cardioid(tf.keras.layers.Layer):
    def __init__(self, bias=2.0, trainable=True):
        super().__init__()
        self.bias_init = bias
        self.trainable = trainable

    def build(self, input_shape):
        super().build(input_shape)
        initializer_bias = tf.keras.initializers.Constant(self.bias_init)
        self.bias = self.add_weight('bias',
                                      shape=(input_shape[-1]),
                                      initializer=initializer_bias,
                                      trainable=self.trainable,
                                      )
    def call(self, z):
        phase = dlmri_tutorial.complex_angle(z)
        cos = tf.cast(tf.math.cos(phase), tf.complex64) 

        return 0.5 * (1 + cos) * z
        
    def __str__(self):
        s = f"Cardioid: bias_init={self.bias_init}, trainable={self.trainable}"
        return s

    @property
    def __name__(self):
        return 'cardioid'

class TestActivation(unittest.TestCase):   
    def _test(self, act, args, shape):
        model = act(**args)
        x = tf.complex(tf.random.normal(shape), tf.random.normal(shape))
        Kx = model(x)
        print(model)
    
    def test_cReLU(self):
        self._test(cReLU, {}, [5, 32])

    def test_ModReLU(self):
        self._test(ModReLU, {'bias':0.1, 'trainable':True}, [5, 32])

    def test_Cardioid(self):
        self._test(Cardioid, {'bias':0.1, 'trainable':True}, [5, 32])

if __name__ == "__main__":
    unittest.test()