import os,sys,shutil
from flask import Flask,render_template,jsonify,request,Response
from flask_cors import cross_origin,CORS
from signLanguage.utils.utils import decodeImage,encodeImageIntoBase64

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename="inputImage.jpg"

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict',methods=['GET,POST'])
@cross_origin()
def predictRoute():
    try:
        image=request.json['image']
        decodeImage(clApp.filename)

        os.system("cd yolov5/ && python detect.py --weights best.pt --img 416 --conf 0.5 --source ../data/inputImage.jpg")
        
        opencodedbase64=encodeImageIntoBase64("yolov5/runs/detect/exp/inputImage.jpg")
        result = {image: opencodedbase64.decode('utf8')}
        if os.path.exists("yolov5/runs"):
            shutil.rmtree("yolov5/runs")

    except ValueError as val:
        print(val)
        return Response("value not found inside json data")
    except KeyError:
        return Response("key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "invalid input"

    return jsonify(result)


@app.route("/live",methods=['GET'])
@cross_origin()
def predictLive():
    try:
        os.system("cd yolov5/ && python detect.py --weights best.pt --img 416 --conf 0.5 --source 0")
        if os.path.exists("yolov5/runs"):
            shutil.rmtree("yolov5/runs")
        return "camera starting!!"
    except ValueError as val:
        print(val)
        return Response("value not found in json data")
    
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0",port=8000)