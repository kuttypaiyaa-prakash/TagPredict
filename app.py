from flask import Flask
from flask import render_template, jsonify, request
from tag_predictor  import getTags

app = Flask(__name__)
action=''

@ app.route('/')
def index():
    if action=="submit":
        return "Autonomous Tagging of Stack Overflow"
    return render_template('index.html')
    # route to get Text Summary

# # #route to get Text Summary
@app.route('/predict', methods = ['POST', 'GET'])

def predict():
    question=[]
    question.append(request.form['question'])
    print(question)
    tags = getTags(question)[0]
    return jsonify(tags)

if __name__ == "__main__":
    app.run(debug=True)
