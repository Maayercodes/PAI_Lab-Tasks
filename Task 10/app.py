from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html', result=None)

# Sentiment route
@app.route('/hospital', methods=['POST'])
def sentiment():
    sentence = request.form['sentence']
    result = f'Sentiment analysis for: {sentence}'
    return render_template('index.html', result=result)

# Starting the Flask app
if __name__ == "__main__":
    app.run(debug=True)

