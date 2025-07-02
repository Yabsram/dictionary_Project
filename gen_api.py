import os 
from google import genai
from google.genai import types

# Set environment variables
def get_response(content):
    my_api_key = os.getenv('GENAI_KEY')
    genai.api_key = my_api_key
    
    # Create an genAI client using the key from our environment variable
    client = genai.Client(api_key=my_api_key)

    # Specify the model to use and the messages to send
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
        system_instruction="""
        With the knowledge of an English professor, you'll be referred to as the 
        helper for a program that specializes in finding the best synonym to use 
        in a situation and giving examples of how to use it in a sentence.
        The slogan of the program is "What's on the Tip of Your Tongue?" 
        """),
        contents=content,
    )

    return(response.text)