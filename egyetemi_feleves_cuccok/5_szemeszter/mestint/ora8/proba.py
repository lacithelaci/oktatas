import numpy as np
import matplotlib.pyplot as plt
from keras import Sequential
from keras.src.layers import Dense
from sklearn.model_selection import train_test_split

data = np.loadtxt('pima-indians-diabetes.csv', delimiter=',')
perm = np.random.permutation(762)
data = data[perm, :]
y = data[:, -1]
x = data[:, :-1]

print(x.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

model = Sequential()

model.add(Dense(units=64, input_dim=8, activation='sigmoid'))  # regresszió --> linear
model.add(Dense(units=32,  activation='sigmoid'))
model.add(Dense(units=16,  activation='relu'))
model.add(Dense(units=1,  activation='sigmoid'))  # sigmoid vagy softmax szokott lenni

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train,epochs=50,batch_size = 32)

_, megoldas = model.evaluate(X_test, y_test)
print(megoldas)