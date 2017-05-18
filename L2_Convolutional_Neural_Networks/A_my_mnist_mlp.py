from keras.datasets import mnist
from keras.layers import Dense, Dropout, Flatten
from keras.models import Sequential
from keras.utils import np_utils

# Import pre-shuffled MNIST database
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print("MNIST training examples: ", len(X_train), " \t test examples: ", len(X_test))

# Rescale the Images
X_train = X_train / 255
X_test = X_test / 255

# Encode Categorical Integer Labels Using a One-Hot Scheme
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

# Model Architecture
model = Sequential()
model.add(Flatten(input_shape=X_train.shape[1:]))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))
model.summary()

# Compile the Model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the Model
model.fit(X_train, y_train, batch_size=256, epochs=10, validation_split=0.2, verbose=2, shuffle=True)

# Classification Accuracy on the Test Set
score = model.evaluate(X_test, y_test, verbose=0)

print('\n Test accuracy: {:.4f}'.format(score[1]))
