
from flask import Flask, jsonify, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/<vals>')
def predict(vals):
    items = vals.split(',')
    vals = [float(i) for i in items]

    with open('output/scaler.h5', 'rb') as f:
        scaler = pickle.load(f)

    with open('output/model.h5', 'rb') as file:
        model = pickle.load(file)
    predictions = model.predict([vals])

    if predictions[0] == 1:
        print(type(scaler))
        return jsonify('You have indicators for diabetes')
    else:
        print(type(scaler))
        return jsonify('You do not have indicators for diabetes')

if __name__ == "__main__":
    app.run(port=8000, debug=True)

