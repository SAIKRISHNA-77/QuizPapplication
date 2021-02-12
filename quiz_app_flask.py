import os
from flask import Flask, render_template, request
import json
import random
app = Flask(__name__)

quiz_host = os.environ.get('FLASK_HOST')
quiz_port = os.environ.get('FLASK_PORT')



f = open('data.json') # Reading data of questions and answers file
data = json.load(f) # returns JSON object as a dictionary

original_questions = data["original_questions"] # Questions dict
answers = data["answers"] # Answers dict used for validation
ans_mapping = data["ans_mapping"] # Answers mapping to numerical index

qns_list = list(original_questions.keys()) # getting all question numbers for shuffling
random.shuffle(qns_list) #shuffling the questions
d={}
c=1
questions=[]
for qns in qns_list:
	d["id"] = c
	d["question"] = "What is {} ?".format(original_questions[qns]['qns'])
	d["answers"] = ["a.{} b.{} c.{} d.{} ".format(original_questions[qns]["ans"][0], original_questions[qns]["ans"][1],
										original_questions[qns]["ans"][2], original_questions[qns]["ans"][3])]
	d["correct"] = answers[qns]+"."+original_questions[qns]['ans'][ans_mapping[answers[qns]]]
	questions.append(d)
print (questions)

@app.route("/", methods=['POST', 'GET'])
def quiz():
    if request.method == 'GET':
        return render_template("index.html", data=questions)
    else:
        result = 0
        total = 0
        for question in questions:
            if request.form[question.get('id')] == question.get('correct'):
                result += 1
            total += 1
        return render_template('results.html', total=total, result=result)


if __name__ == "__main__":
    app.run(host=quiz_host, port=quiz_port)
