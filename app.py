from flask import Flask,render_template,redirect,url_for,request,jsonify
from flask_cors import cross_origin,CORS
from src.Mask.loggers import logger
from src.Mask.exceptions import CustomException
import os,sys
from src.Mask.Pipelines.prediction import MaskPredictionPipeline
from src.Mask.Utils import decode_image




#creating flask object
app = Flask(__name__)
CORS(app)


@cross_origin
@app.route('/')
def index():
    return render_template("index.html")

@cross_origin
@app.route('/train',methods=['POST',"GET"])
def train():
    os.system("main.py")
    return "Training model Done"

class ClientApp():
    def __init__(self):
        #user given  image changing them into jpg format
        self.filename = "inputImage.jpg"
        #creating an object of MaskPredictionPipeline class
        self.classifier = MaskPredictionPipeline(filename=self.filename)


@cross_origin
@app.route('/predict',methods=['POST',"GET"])
def predict():
    image = request.json['image']
    decode_image(image,clapp.filename) ##clApp object of clientapp class
    result  = clapp.classifier.prediction()
    return jsonify(result)








if __name__ == '__main__':
    clapp = ClientApp()
    app.run(host="0.0.0.0",port=8080,debug=True)