import os 
from google import genai
from google.genai import types

# Set environment variables
def get_response(word, synonyms):
    my_api_key = os.getenv('GENAI_KEY')
    genai.api_key = my_api_key
    
    # Create an genAI client using the key from our environment variable
    client = genai.Client(api_key=my_api_key)

    # Specify the model to use and the messages to send
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
        system_instruction="You are an English teacher that can find the best synonym to use in a situation and can provide examples of how to use it."
        ),
        contents="What are the advantages of pair programming?",
    )
    return(response.text)