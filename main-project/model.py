import numpy as np
import cv2
import os
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout , BatchNormalization
from keras.callbacks import ReduceLROnPlateau
from sklearn import preprocessing
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

#import data
images = []
labels = []
for char in os.listdir("./test"):
  label = char.replace("hand_", "")
  print(label)
  folder_path = os.path.join("./test", char)
  for file_name in os.listdir(folder_path):
    image_path = os.path.join(folder_path, file_name)
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (128, 128))
    img_normalize = img/255 #normalize data to range(0,1)
    images.append(img_normalize)
    labels.append(label)
images = np.array(images, dtype='float16')
labels = np.array(labels)
print(images.shape)

#encode labels
le = preprocessing.LabelEncoder()
le.fit(labels)
labels_encoded = le.transform(labels)
Y_train = to_categorical(labels_encoded)
X_train = images

#split data to train and validation set
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=0.2, random_state=42)

#setup model
learning_rate_reduction = ReduceLROnPlateau(monitor='val_accuracy', patience=2, verbose=1, factor=0.5, min_lr=0.00001)

model = Sequential()
model.add(Conv2D(75, (3, 3), strides=1, padding='same', activation='relu', input_shape=(128, 128, 1)))
model.add(BatchNormalization())
model.add(MaxPool2D((2, 2), strides=2, padding='same'))
model.add(Conv2D(50, (3, 3), strides=1, padding='same', activation='relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(MaxPool2D((2, 2), strides=2, padding='same'))
model.add(Conv2D(25, (3, 3), strides=1, padding='same', activation='relu'))
model.add(BatchNormalization())
model.add(MaxPool2D((2, 2), strides=2, padding='same'))
model.add(Flatten())
model.add(Dense(units=512, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(units=1, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#train model
history = model.fit(X_train, Y_train, batch_size=32, epochs=10, validation_data=(X_val, Y_val), callbacks=[learning_rate_reduction])

#save model
model.save('./hand test')