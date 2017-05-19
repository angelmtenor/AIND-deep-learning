from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential

model = Sequential()
model.add(Conv2D(filters=32, kernel_size=3, strides=2, padding='same',
                 activation='relu', input_shape=(128, 128, 3)))

model.add(MaxPooling2D(pool_size=2, strides=2))

model.summary()
