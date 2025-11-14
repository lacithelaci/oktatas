from numpy import loadtxt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
dataset = loadtxt('segment.txt', delimiter=' ')
import tensorflow as tf
print(np.shape(dataset))

# split into input (X) and output (y) variables
X = dataset[:,0:19]

y = tf.keras.utils.to_categorical(dataset[:,19])

print(np.shape(y))
# define the keras model
model = Sequential()
model.add(Dense(10, input_dim=19, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='sigmoid'))
# compile the keras model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=300, batch_size=768)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))