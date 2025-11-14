from numpy import loadtxt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense


# load the dataset
dataset = loadtxt('segment.txt', delimiter=' ')
import tensorflow as tf
print(np.shape(dataset))
#
# # split into input (X) and output (y) variables
X = dataset[:,0:19]
#mert nem 0-ról indul -1 az y-ból
print(set(dataset[:,19]))
y = tf.keras.utils.to_categorical(dataset[:,19]-1)

X_train = X[:1600,:]
Y_train = y[:1600,:]
X_test = X[1600:,:]
Y_test = y[1600:,:]
print(np.shape(y))
# # define the keras model
model = Sequential()
model.add(Dense(10, input_dim=19, activation='relu'))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(8, activation='sigmoid'))
model.add(Dense(7, activation='sigmoid'))
# # compile the keras model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X_train, Y_train, epochs=300, batch_size=512)
# evaluate the keras model
_, accuracy = model.evaluate(X_train, Y_train)
print('Accuracy: %.2f' % (accuracy*100))
_, accuracy = model.evaluate(X_test, Y_test)
print('Accuracy: %.2f' % (accuracy*100))