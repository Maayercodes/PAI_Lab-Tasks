from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form  

        features = [
            float(data['Adj Close']),
            float(data['High']),
            float(data['Low']),
            float(data['Open']),
            float(data['Volume']),
            float(data['Target']),
            float(data['Score'])

        ]

        prediction = model.predict([features])[0]

        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)