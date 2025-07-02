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
        Complete the sentence only and list the top 5 synonyms from the options that can complete the sentence." 
        """),
        contents=content,
    )

    return response.text

def complete_sentence(sentence, synonym_dict):
    prompt = f"""Complete this sentence using the best-fitting synonym for the blank(_):\n\n"{sentence}"\n\nOptions: {synonym_dict}"""
    return get_response(prompt)