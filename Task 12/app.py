from flask import Flask, render_template, request
from chatbot import chatbot

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["question"]
        response = chatbot.respond(user_input)
        if not response:
            response = "I'm not sure how to respond to that. Please contact the admissions office."
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
