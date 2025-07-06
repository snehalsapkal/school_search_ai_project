from flask import Flask, render_template, request
import pandas as pd
from recommender import recommend_schools
from chatbot import chat_with_gpt

app = Flask(__name__)
df = pd.read_csv("data/schools.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"]
    recommendations = recommend_schools(query, df)
    return render_template("results.html", schools=recommendations)

@app.route("/chat", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        user_message = request.form["message"]
        response = chat_with_gpt(user_message)
    return render_template("chat.html", response=response)

if __name__ == "__main__":
    app.run()
