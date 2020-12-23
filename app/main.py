# from chatterbot import ChatBot
# from scripts.chatbot import cs_chatbot
# from scripts.chatbot import gpt_chatbot
from flask import Flask, render_template, request

import config

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

import json
import openai

# Creating ChatBot Instance
cs_chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

 # Training with Personal Ques & Ans 
training_data_simple = open('../training_data/normal.txt').read().splitlines()
training_data_personal = open('../training_data/all.txt').read().splitlines()

training_data = training_data_simple + training_data_personal

trainer = ListTrainer(cs_chatbot)
trainer.train(training_data)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(cs_chatbot)


# chatbot.py Camelia

openai.api_key = config.api_key #os.getenv("API_KEY")

def gpt_chatbot(question):

    # prompt = """Codey is Codecademy's AI assistant and knows everything there is to know about programming. 
    # Codey wants to help our learners with all kinds of questions and provide them detailed answers to any questions that they ask. 
    # The assistant is helpful, creative, clever, very friendly, and very encouraging.

    # Sonny: What is HTML?\nCodey: HTML (HyperText Markup Language) is the main building block of websites and webpages. It is used to specify the layout and content of a webpage, and makes it possible for a browser to read and display it. And it can be assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript.\n\n
    # Sonny: What is while loop?\nCodey: \nA while loop is a control flow structure that repeats a statement or group of statements until a certain condition becomes false. The condition is checked before the control flow enters the loop. This helps control the program flow.\n\n
    # Sonny: What is a variable?\nCodey: A variable is a named memory location used to store data. This data can be of different data types.\n\n
    # Sonny: What is the difference between HTML and CSS?\nCodey: HTML stands for Hypertext Markup Language, and CSS stands for Cascading Style Sheets. HTML and CSS are both used to define the look and layout of a website. HTML is used to define the content and structure of a web page, while CSS is used to change the appearance of a page.\n\n
    # Sonny: What is coding?\nCodey: Coding is the process of writing computer programs. The program code is written in a programming language, and the program is compiled into a program that can be run by the CPU.\n\n
    # Sonny: What is the difference between if and if else statement?\nCodey: The `if` statement is used to make a decision. If a certain condition is true, then the statement(s) following `if` is executed. If the condition is not true, then the code following the `else` statement is executed.\n\n
    # Sonny: What is Object-oriented programming?\nCodey: Object-oriented programming (OOP) is a programming paradigm based on the concept of \"objects\", which might contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods. A feature of objects is that an object's procedures can access and often modify the data fields of the object with which they are associated (objects have a notion of `this` or `self`). In OOP, computer programs are designed by making them out of objects that interact with one another.\n\n
    # Sonny: What is polymorphism?\nCodey: Polymorphism is the provision of a single interface to entities of different types.\n\n
    # Sonny: Give me an example of a if statement in Python.\nCodey: if coffee == \"hot\"\n  # Code runs if true\nelse:\n  # Code runs if false\n\n
    # Sonny: How do I write a function in JavaScript?\nCodey: \nfunction addNumbers(a, b) {\n    return a + b;\n}\n\n
    # Sonny: What is distinct in sql?\nCodey: Distinct is used to remove duplicate rows from a result set.\nSELECT DISTINCT column1, column2, ...\nFROM table_name;\n\n
    # Sonny: What is a Where in SQL?\nCodey: WHERE is used to filter rows.\nSELECT column1, column2, ...\nFROM table_name\nWHERE column1 = value1;\n\n
    # Sonny: What is a Subquery in SQL?\nCodey: A subquery is a SQL query nested inside another SQL query. \nSELECT column1, column2, ...\nFROM table_name\nWHERE column1 IN (SELECT column1 FROM table_name);\n\n
    # Sonny: {}
    # Codey:""".format(question)

    prompt = """Codey is Codecademy's AI assistant and knows everything there is to know about programming.
    Codey wants to help our learners with all kinds of questions and provide them detailed answers to any questions
    that they ask. The assistant is helpful, creative, clever, very friendly, and very encouraging.
    
    Sonny: What is HTML?\n
    Codey: HTML (HyperText Markup Language) is the main building block of websites and webpages. It is used to specify the layout and content of a webpage, and makes it possible for a browser to read and display it. And it can be assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript.\n\n
    
    Sonny: What is while loop?\n
    Codey: \nA `while` loop is a control flow structure that repeats a statement or group of statements until a certain condition becomes false. The condition is checked before the control flow enters the loop. This helps control the program flow.\n\n
    
    Sonny: What is a variable?\n
    Codey: A variable is a named memory location used to store data. This data can be of different data types.\n\n
    
    Sonny: What is the difference between HTML and CSS?\n
    Codey: HTML stands for Hypertext Markup Language, and CSS stands for Cascading Style Sheets. HTML and CSS are both used to define the look and layout of a website. HTML is used to define the content and structure of a web page, while CSS is used to change the appearance of a page.\n\n
    
    Sonny: What is coding?\n
    Codey: Coding is the process of writing computer programs. The program code is written in a programming language, and the program is compiled into a program that can be run by the CPU.\n\n
    
    Sonny: What is the difference between if and if else statement?\n
    Codey: The `if` statement is used to make a decision. If a certain condition is true, then the statement(s) following `if` is executed. If the condition is not true, then the code following the `else` statement is executed. The `else` statement is optional.\n\n
    
    Sonny: What is object-oriented programming?\n
    Codey: Object-oriented programming (OOP) is a programming paradigm based on the concept of \"objects\", which might contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods. A feature of objects is that an object's procedures can access and often modify the data fields of the object with which they are associated (objects have a notion of `this` or `self`).<br><br>
    In OOP, computer programs are designed by making them out of objects that interact with one another.\n\n
    
    Sonny: What is a Where in SQL?\n
    Codey: WHERE is used to filter rows.<br><br>
    SELECT column1, column2, ...<br>
    FROM table_name<br>
    WHERE column1 = value1;\n\n

    Sonny: What is a Subquery in SQL?\n
    Codey: A subquery is a SQL query nested inside another SQL query.<br><br>
    SELECT column1, column2, ...<br>
    FROM table_name<br>
    WHERE column1 IN (SELECT column1 FROM table_name);\n\n

    Sonny: {}
    Codey:""".format(question)

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        stop="Sonny:",
        temperature=0.6,
        max_tokens=150,
        top_p=1,
        presence_penalty=0.3,
    )
    print(response)
    json_response = json.dumps(response)
    rep = json.loads(json_response)
    bot_reply = rep['choices'][0]['text']
    print(question)
    print(str(bot_reply))
    return str(bot_reply)


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