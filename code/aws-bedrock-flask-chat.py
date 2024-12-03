'''
module : aws-bedrock-flask-chat.py
language : Python 3.x
email : andrew@openmarmot.com
notes :
github : https://github.com/openmarmot/aws-bedrock-flask-chat
'''

# external imports 
from flask import Flask, render_template, request, jsonify

# local imports
import bedrock 

app = Flask(__name__)

# Mock function for AI inference
def ai_inference(text):
    return f"AI response to: '{text}'"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/infer', methods=['POST'])
def infer():
    input_text = request.form.get('input_text')
    output_text = ai_inference(input_text)  # Here you would call your actual AI function
    return jsonify({'output': output_text})

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)