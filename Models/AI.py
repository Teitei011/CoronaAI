import tensorflow as tf
import numpy as np
import cv2
import sys

def prepare(filepath, size):
    data = []
    image = cv2.imread(filepath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (size, size))
    # update the data and labels lists, respectively
    data.append(image)

    return np.array(data) / 255.0



def predictFormatacao(array):
    variable = "Covid19: {:.2f}%\n".format(array[0][0] * 100)
    variable += "Saudável: {:.2f}%".format(array[0][1] * 100)

    return variable


def loadModel():
    return tf.keras.models.load_model("/home/stefantcleal/site/CoronaAI/Models/GO.h5")


def predict(model, image):
    return model.predict(prepare(image))

def see_if_image_is_Xray(image):
    model = tf.keras.models.load_model("/home/stefantcleal/site/CoronaAI/Models/GO.h5")
    prediction = model.predict(prepare(image))
    return " {:.2f}".format((1 - prediction[0][0])*100)


def AI(image):
    model = tf.keras.models.load_model("/home/stefantcleal/site/CoronaAI/Models/Filter.model")
    filter = model.predict(prepare(image, 512))

    if (filter[0][0] > 0.65):
        return "0.00"

    else:
        model = tf.keras.models.load_model("/home/stefantcleal/site/CoronaAI/Models/GO.h5")
        prediction = model.predict(prepare(image, 224))

        return " {:.2f}".format((1 - prediction[0][0])*100)