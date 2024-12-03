'''
module : bedrock.py
language : Python 3.x
email : andrew@openmarmot.com
notes :
github : https://github.com/openmarmot/aws-bedrock-flask-chat
'''

# ref : 
# https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-examples.html
# https://aws.amazon.com/bedrock/pricing/


# external imports 
import boto3

# setup global variables 
model_id="anthropic.claude-3-5-haiku-20241022-v1:0"
system_prompts = [{"text": "You are a super smart engineer"}]
bedrock_client = boto3.client(service_name='bedrock-runtime')
messages=[]

def generate_response(input_text):
    ''' generate a AI response. handles all formatting. returns the full conversation'''
    # input_text : a string 

    global model_id,system_prompts,bedrock_client,messages

    # format input 
    input_format = {
        "role": "user",
        "content": [{"text": input_text}]
    }

    messages.append(input_format)

    # Inference parameters to use.
    temperature = 0.5
    top_k = 200

    inference_config = {"temperature": temperature}
    additional_model_fields = {"top_k": top_k}

    # Send the message.
    response = bedrock_client.converse(
        modelId=model_id,
        messages=messages,
        system=system_prompts,
        inferenceConfig=inference_config,
        additionalModelRequestFields=additional_model_fields
    )
    #print(response)
    output_format=response['output']['message']

    messages.append(output_format)

    # Log token usage.
    token_usage = response['usage']
    print("Input tokens: %s", token_usage['inputTokens'])
    print("Output tokens: %s", token_usage['outputTokens'])
    print("Total tokens: %s", token_usage['totalTokens'])
    print("Stop reason: %s", response['stopReason'])

    return response['output']['message']['content'][0]['text']

def reset_conversation():
    '''get ready to start a new conversation'''
    global messages
    messages=[]