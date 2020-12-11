import pygame
import sys
import os
from PIL import Image
import numpy
import cv2 as cv
import tensorflow as tf
import os
import tensorflow.python.util.deprecation as deprecation


# Suppress warning
deprecation._PRINT_DEPRECATION_WARNINGS = False
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


def NeuralNetwork():
    # Load data number set
    mnist_data = tf.keras.datasets.mnist
    # Split data for training and testing
    (x_train, y_train), (_, _) = mnist_data.load_data()

    # Preprocessing by normalizing data
    x_train = tf.keras.utils.normalize(x_train, axis=1)
    # x_test = tf.keras.utils.normalize(x_test, axis=1)

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))

    # Number of neurons with layers
    model.add(tf.keras.layers.Dense(units=512, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.Dense(units=512, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics="accuracy",
    )
    model.fit(x_train, y_train, epochs=4, verbose=0)
    return model


def output_image():
    pygame.image.save(screen, os.path.expanduser("./pic.png"))
    image = Image.open("./pic.png")
    image = image.resize((28, 28), Image.ANTIALIAS)
    image.save(fp="pic.png", quality=100, optimize=True)


def prediction(model):
    # Load image and normalize
    img = cv.imread("./pic.png")[:, :, 0]
    img = numpy.array([img])
    img = tf.cast(img, tf.float32) / 255
    prediction = model.predict(img)
    return numpy.argmax(prediction)


if __name__ == "__main__":

    model = NeuralNetwork()

    # Color
    black = (0, 0, 0)
    white = (255, 255, 255)
    screen_color = white
    paint_color = black

    # Initialize the game
    pygame.init()

    # Set screen with width and height and fill with black
    screen = pygame.display.set_mode((560, 560))
    screen.fill(black)

    # Set title
    pygame.display.set_caption("Number Guesser")

    # Set clock rate
    clock = pygame.time.Clock()

    running = True
    mouse_press = False

    while running:
        print("\033c", end="")
        for event in pygame.event.get():
            # If click close windows
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            # If click e to erase the board
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    screen.fill(black)

            # Get mouse position
            mx, my = pygame.mouse.get_pos()

            # Draw circle at mouse position
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pygame.draw.circle(screen, white, (mx, my), 15)
            if pygame.mouse.get_pressed() == (0, 0, 1):
                pygame.draw.circle(screen, black, (mx, my), 15)

            # Release mouse -> save image and trigger predict
            if event.type == pygame.MOUSEBUTTONUP:
                output_image()
                number = prediction(model)
                print("Predicted number:", number)
                mouse_press == False
        clock.tick(120)

        pygame.display.update()
