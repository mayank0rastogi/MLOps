import tensorflow as tf
import numpy as np
import json
import requests

SIZE=128
MODEL_URI='http://localhost:8501/v1/models/pets:predict'
CLASSES=['CAT','DOG']

def get_predictions(image_path):

    image=tf.keras.preprocessing.image.load_img(image_path,target_size=(SIZE,SIZE))
    #convert the image to a numpy array
    image=tf.keras.preprocessing.image.img_to_array(image)
    #use the mobile-net preprocess input
    image=tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image=np.expand_dims(image,axis=0)



    data=json.dumps({
    'instances':image.tolist()

    })

    # By default it has utf-8 encoding which we required here in data.encode()
    response=requests.post(MODEL_URI,data=data.encode())
    result=json.loads(response.text)
    # print(result)
    prediction=np.squeeze(result['predictions'][0])
    class_name= CLASSES[int(prediction>0.5)]
    return class_name

# get_predictions('anon.jpg')
