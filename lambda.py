import json
import boto3

def lambda_handler(event, context):
    # 1. Initialize Bedrock Client
    client = boto3.client(service_name='bedrock-agent-runtime', region_name='us-east-1')
    
    # 2. Hardcoded IDs (Double check these!)
    K_BASE_ID = 'ZKTLUKDCA6' 
    MODEL_ARN = 'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-5-sonnet-20240620-v1:0'

    try:
        # 3. Parse Input from API Gateway
        # API Gateway sends the payload as a string in event['body']
        if 'body' in event and event['body']:
            body_data = json.loads(event['body'])
            user_query = body_data.get('search_query', "Recommend a popular movie")
        else:
            user_query = "Recommend a popular movie"
    
        movie_prompt = """You are an enthusiastic, passionate movie critic.
        You give movie recommendations based ONLY on the provided search results.
        NEVER use robotic phrases like 'Based on the search results' or 'Here are some options.
        Instead, sound like you are talking to a friend about a fantastic film! Be engaging and fun.

        CRITICAL INSTRUCTIONS:
        1. Provide EXACTLY 3 movie recommendations from the search reults(if atleast 3 exist). If fewer exists, enthusiastically provide what you have.
        2. For EACH movie, write a detailed paragraph of exactly 5 to 6 lines.
        3. In this descriptio, include the basic plot, the vibe/genre, and a passionate reason why they must watch it.
        4. Format your repsonse with clear, bold headings for each movie title so it looks great on a screen.
        
        Search Results:
        $search_results$
        """

        # 4. Call Bedrock Knowledge Base
        response = client.retrieve_and_generate(
            input={'text': user_query},
            retrieveAndGenerateConfiguration={
                'type': 'KNOWLEDGE_BASE',
                'knowledgeBaseConfiguration': {
                    'knowledgeBaseId': K_BASE_ID,
                    'modelArn': MODEL_ARN,
                    'generationConfiguration':{
                    'promptTemplate': {
                        'textPromptTemplate': movie_prompt
                        }
                    }
                }
            }
        )
        
        answer = response['output']['text']

        # 5. THE RESPONSE (This must be exactly in this format for 502 to go away)
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',  # Required for browser access
                'Access-Control-Allow-Methods': 'OPTIONS,POST',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'recommendation': answer})
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }