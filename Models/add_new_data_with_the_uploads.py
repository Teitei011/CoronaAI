from imutils import paths
import tensorflow as tf
import numpy as np
# from training_model import train
import time 
import glob
import cv2
import sys
import os

IMAGE_SIZE = 224
CLASSIFICATIONS = ["Covid19", "Normal"]
UPLOAD_FOLDER_PATH  = "/home/stefantcleal/site/CoronaAI/static/uploads"
DATASET_FOLDER = "/home/stefantcleal/site/CoronaAI/dataset/" #covid
ACCEPTED_PROBABILITY = 0.75


path = os.getcwd()

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)


def image_2_process(imagePaths):
    print("[INFO] Processing the images...")
    start = time.time()

    data = []
    for imagePath in imagePaths:
      image = cv2.imread(imagePath)
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      image = cv2.resize(image, (IMAGE_SIZE, IMAGE_SIZE))
      # update the data and labels lists, respectively
      data.append(image)

    # convert the data and labels to NumPy arrays while scaling the pixel
    # intensities to the range [0, 1]
    print(f"[INFO] Data shape {data[0].shape}")

    return  np.array(data) / 255.0

def import_uploaded_images():
    imagePaths = list(paths.list_images(UPLOAD_FOLDER_PATH))
    return imagePaths
    # return image_2_process(imagePaths)


def clean_upload_folder(folder_path):
    print("[INFO] Deleting uploaded Photos...")
    os.system(f"rm -rf {UPLOAD_FOLDER_PATH}")
    os.system(f"mkdir {UPLOAD_FOLDER_PATH}")
    print("[INFO] Deleted")


def prepare(filepath):
    data = []
    image = cv2.imread(filepath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    # update the data and labels lists, respectively
    data.append(image)

    return np.array(data) / 255.0

def query(image):
    model = tf.keras.models.load_model("covid19_2.model")
    prediction = model.predict(image)

    return model.predict(image) # Esse é só o resultado cru, sem o tratamento da função predict


def put_in_the_right_folder(image, classification):
    if (classification[0][0] > ACCEPTED_PROBABILITY): # COVID
        os.system(f"mv {image} {DATASET_FOLDER}/covid")
        

def retrain_the_AI():
    train()


def main():
    all_images = import_uploaded_images()

    for image in all_images:
        result = query(prepare(image))

        put_in_the_right_folder(image, result)

    
    # retrain_the_AI()
    # clean_upload_folder()


if __name__ == "__main__":
    main()

