import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

#Loading the model
logreg_model = pickle.load(open('logreg_model.pkl', 'rb'))
logreg_transformer = pickle.load(open('logreg_transform.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/logreg_predict_api', methods = ['POST'])
def logreg_predict_api():
    logreg_data = request.json['logreg_data']
    print(logreg_data)
    print(pd.Series(logreg_data.values()))
    new_logreg_data = logreg_transformer.transform(pd.Series(logreg_data.values()))
    output = logreg_model.predict(new_logreg_data)
    print(output[0])
    return jsonify(str(output[0]))



@app.route('/predict', methods = ['POST'])
def predict():
    data = [str(logreg_data) for logreg_data in request.form.values()]
    final_input = logreg_transformer.transform(pd.Series(data))
    print(final_input)
    output = logreg_model.predict(final_input)
    return render_template("index.html", prediction_text = "The predictive rating for the Review out of a score of 5 is {}". format(output))



if __name__ == '__main__':
    app.run(debug=True)


