import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Input

# 1. Adatok betöltése
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizáljuk 0-1 közé
x_train = x_train / 255.0
x_test = x_test / 255.0

# Címkék one-hot kódolása
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 2. Háló létrehozása
model = Sequential([
    Input(shape=(28, 28)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# 3. Modell fordítása
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 4. Modell tanítása
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.1)

# 5. Értékelés a teszt adatokon
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Teszt pontosság: {test_acc:.4f}')
