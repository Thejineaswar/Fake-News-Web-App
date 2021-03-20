from flask import Flask, request,jsonify,render_template
import numpy as np
from models.svc import load_model,predict
model = load_model()
print("Model has been loaded")
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/fakeNews',methods=['POST'])
def fakeNews():
    value = [i for i in request.form.values()]
    print(value[0])
    res = predict(value[0])
    print(res)
    if(res==1):
        res = True
    else:
        res = False
    return render_template('index.html',prediction_text = f"This is {res}")



if __name__ == '__main__':
    app.run()
