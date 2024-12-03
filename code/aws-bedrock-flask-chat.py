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

# global variables
messages=[]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/infer', methods=['POST'])
def infer():
    input_text = request.form.get('input_text')
    output_text = bedrock.generate_response(input_text)
    #print(output_text)
    return jsonify({'output': output_text})

@app.route('/reset', methods=['POST'])
def reset():
    bedrock.reset_conversation()
    return jsonify({'success': True})

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)