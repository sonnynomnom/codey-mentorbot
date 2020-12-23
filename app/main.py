from chatterbot import ChatBot
from scripts.chatbot import cs_chatbot
from scripts.chatbot import gpt_chatbot
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

    customer_support = ["Codecademy",
                        "Codecademy Pro", 
                        "student discount",
                        "refund", 
                        "cancel my subscription", 
                        "canel subscription", 
                        "Reset Password", 
                        "Codecademy Path",
                        "Codecademy for Business",
                        "Codecademy for Campus"]

    # check for customer support questions

    if any (inquery in userText for inquery in customer_support):
      # use hardcoded
      return str(cs_chatbot.get_response(userText))
    else:
      # use gtp-3
      return str(gpt_chatbot(userText)) 

if __name__ == "__main__":
    app.run()