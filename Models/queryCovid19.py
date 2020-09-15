import tensorflow as tf
import numpy as np
import cv2
import sys

def prepare(filepath):
    data = []
    image = cv2.imread(filepath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
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

def CoronaAI(image):
  model = tf.keras.models.load_model("/home/stefantcleal/site/CoronaAI/Models/GO.h5")
  prediction = model.predict(prepare(image))
  return " {:.2f}".format((1 - prediction[0][0])*100)
