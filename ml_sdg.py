# -*- coding: utf-8 -*-
"""ML-SDG

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bplxxOxrv4W0t1yBHoA9P8GkAfxpLYlt
"""

# Import necessary libraries
import numpy as np
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load iris dataset
iris = load_iris()
X, Y = iris.data, iris.target

# Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

#sgd
# Split data into train and test sets
x_train , x_test , y_train , y_test =  train_test_split(X,Y,test_size=0.3)

# Define ANN model
model = tf.keras.Sequential([
  tf.keras.layers.Flatten(input_shape=(4,)),
  tf.keras.layers.Dense(50, activation='relu'),
  tf.keras.layers.Dense(3, activation='softmax')
])

# Compile the model
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(x_train, tf.keras.utils.to_categorical(y_train, num_classes=3), epochs=100, validation_data=(x_test, tf.keras.utils.to_categorical(y_test, num_classes=3)))

# Plot the loss graph
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()