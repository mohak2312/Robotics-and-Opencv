import requests
import json
import cv2

while True:
    url = "192.168.1.4:5000/data"
    r = requests.get(url)
    if r.text['Name'] == None:
        pass
    else:
        if r.text['Name'] == "<Insert name and motion>"
        ##Enter code for setting motor positions
        
