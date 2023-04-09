
from flask import Flask, jsonify, render_template
import json
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    with open('output/model.h5', 'rb') as file:
        model = pickle.load(file)
    predictions = model.predict([[3, 170, 64, 37, 225, 34.5, 0.356, 30]])
    print(predictions)
    return 'no errors!'

if __name__ == "__main__":
    app.run(debug=True)

