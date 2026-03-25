import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

(x_train,y_train), (x_test,y_test)= tf.keras.datasets.mnist.load_data()

x_train, x_test= x_train/255.0, x_test/255.0

x_train= x_train.reshape(-1,28,28,1)
x_test= x_test.reshape(-1,28,28,1)

data_augmentation = tf.keras.Sequential([
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
    layers.RandomTranslation(0.1,0.1)
])

model= models.Sequential([
    data_augmentation,
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(128,activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10,activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train,y_train,epochs=8,validation_split=0.1)

test_loss,test_acc= model.evaluate(x_test,y_test)
print(f"Test accuracy :- {test_acc}")

predictions= model.predict(x_test)

for i in range(5):
    plt.imshow(x_test[i].reshape(28,28), cmap=plt.cm.binary)
    plt.title(f"Predicted :- {predictions[i].argmax()} | Actual :- {y_test[i]}")
    plt.show()

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train','Validation'])
plt.show()
