from flask import Flask,request,render_template

import pickle
import pandas as pd

model = pickle.load(open('model.pk','rb'))

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('taxiFare.html')

@app.route('/predict',methods=['GET','POST'])

def predict():
    if request.method=='POST':
        duration =float(request.form['duration'])
        duration=duration/60
        distance = float(request.form['distance'])
        num_passenger=int(request.form['passenger'])
        fare=float(request.form['fare'])
        tip=float(request.form['tip'])
        ex_charge=float(request.form['charges'])
        surge=request.form['surge']
        if (surge == 'Yes'):
                d= 1
        
        else:
                d= 0

        output = model.predict([[duration,distance,num_passenger,fare,tip,ex_charge,d]])

        output = round(output[0],2)
        return render_template('taxiFare.html',predictions=output)


if __name__ == '__main__':
	app.run(debug=True)
