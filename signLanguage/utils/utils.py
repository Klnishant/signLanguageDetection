import os.path
import yaml
import base64
import sys

def decodeImage(imgstr,filename):
    imgdata = base64.b64decode(imgstr)
    with open("./data/"+filename,'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode(f.read())