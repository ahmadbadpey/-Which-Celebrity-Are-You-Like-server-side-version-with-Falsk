from app import app
from flask import Flask, request
from keras_vggface import VGGFace
from keras_vggface import utils
from keras_vggface.utils import preprocess_input
from mtcnn import MTCNN
import cv2 as cv
import numpy as np


@app.route('/predict', methods=['POST'])
def predict():
    image = request.get_json().get('image')

    vggface = VGGFace(model='vgg16')
    detector_obj = MTCNN()

    face = extract_face('uploads/'+image , detector_obj)
    face = face.astype('float32')
    input_sample = np.expand_dims(face, axis=0)
    samples = preprocess_input(input_sample)

    pred = vggface.predict(samples)
    # print(pred)

    output = utils.decode_predictions(pred)
    # print(output)

    prediction = output[0][0][0].replace("b'", "").replace("'", "")
    return prediction


def extract_face(address , detector_obj):
    img = cv.imread(address)

    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    face = detector_obj.detect_faces(rgb_img)[0]
    x, y, w, h = face['box']

    actual_face = img[y:y + h, x:x + w]  # This crop only section of image that contain person Face
    actual_face = cv.resize(actual_face, (224, 224))

    return np.asarray(actual_face)
