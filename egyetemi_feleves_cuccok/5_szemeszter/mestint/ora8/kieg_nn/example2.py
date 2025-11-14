import numpy as np
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# split into input (X) and output (y) variables
print(np.shape(dataset))
kever=np.random.permutation(768)
X=dataset[kever,:8]
Y=dataset[kever,8]
print(set(Y)) # ha osztályozás akkor a 0 sz 1. osztály
#tanító (80%) (70-95%)
X_train=X[:600,:]
Y_train=Y[:600]
#teszt (20%)
X_test=X[600:,:]
Y_test=Y[600:]

# # define the keras model

model = Sequential() # osztályozás act={sigmoid,tanh,relu}
model.add(Dense(8,input_dim=8,activation='sigmoid'))
model.add(Dense(6,activation='relu'))
model.add(Dense(4,activation='relu'))
#Osztályozó utolsó réteg softmax/sigmoid
#Regresszió 'linear'
model.add(Dense(1,activation='sigmoid'))
#osztályozás{binary_crossentropy,categorical_crossentropy}
#regressió {MSE}
#opti RMSProp
model.compile(loss='binary_crossentropy',
              optimizer='adam',metrics=['accuracy'])
model.fit(X_train,Y_train,epochs=300,batch_size=64,verbose=0)
_, accuracy = model.evaluate(X_train, Y_train)
print('Tanító Accuracy: %.2f' % (accuracy*100))
_, accuracy = model.evaluate(X_test, Y_test)
print('Test Accuracy: %.2f' % (accuracy*100))






# model = Sequential()
# model.add(Dense(8, input_dim=8, activation='relu'))
# model.add(Dense(6, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))
# # compile the keras model
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# # fit the keras model on the dataset
# model.fit(X, y, epochs=100, batch_size=32)
# # evaluate the keras model
# _, accuracy = model.evaluate(X, y)
# print('Accuracy: %.2f' % (accuracy*100))