from flask import Flask, request,jsonify,render_template
import numpy as np
from models.humour_detection import *
from models.svc import load_model,predict
model = load_model()
print("Fake News Model has been loaded")
# svc = define_svc()
# print("Humour model has been loaded")
app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/fakeNews',methods=['POST'])
def fakeNews():
    value = [i for i in request.form.values()]
    res = predict(value[0])
    if(res==1):
        res = "real news"
    else:
        res = "fake news"

    # res_1 = predict_humour(value[0])
    # print(res_1)
    return render_template('index.html',prediction_text = f"This is {res}")



if __name__ == '__main__':
    app.run()
