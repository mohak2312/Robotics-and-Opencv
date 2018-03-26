from flask import Flask
from flask import request
import requests
from io import BytesIO
import json
from PIL import image
import cv2
import Dataset_recognizer

app = Flask(__name__)

@app.route('/data')
def data_req():
    error = None
    url = "192.168.1.4:5000/cam"
    if request.method == 'GET':
         f = requests.get(url)
        im = f.form['the_file']
        name = Dataset_recognizer.face_recognizer(im)
    return json.dumps({'Name':name})

@app.route('/cam')
def data_proc():
    cam = cv2.VideoCapture(0)
    ret, im =cam.read()
    return json.dumps({'the_file':im})
    
if __name__ == '__main__':
      app.run(host='192.168.1.4', port=5000)
