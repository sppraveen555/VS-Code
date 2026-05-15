import tensorflow as tf
import matplotlib.pyplot as plt


(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()


train_images = train_images / 255.0
test_images = test_images / 255.0


model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])


model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


model.fit(train_images, train_labels, epochs=5)


loss, accuracy = model.evaluate(test_images, test_labels)

print("Test Accuracy:", accuracy)


prediction = model.predict(test_images)


plt.imshow(test_images[0], cmap="gray")
plt.title("Predicted Number: " + str(prediction[0].argmax()))
plt.show()