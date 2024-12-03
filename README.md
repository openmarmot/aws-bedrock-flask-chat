AWS Bedrock Flask Chat

This is a simple Flask web app to demonstrate using AWS Bedrock for AI inference.  

The bedrock code uses bedrock.converse and a message array to maintain a conversation history
across api calls.  
All of the AWS Bedrock specific code is contained in bedrock.py so other AI endpoints 
could be easily swapped in.

![screenshot](/screenshots/screenshot-12-3-2024.png "Flask App")

###To use :
- Setup the AWS CLI on your system
- Associate the AWS CLI with a AWS API key for a user with permissions for AWS Bedrock
- pip install the modules in the requirements.txt
- In AWS Bedrock enable the model you want under 'Model Access' 
- Adjust 'model_id' in bedrock.py to match your preferred model
- run with : python aws-bedrock-flask-chat.py
- navigate to http://127.0.0.1:5000 with your web browser

