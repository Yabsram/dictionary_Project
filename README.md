# What's on the Tip of Your Tongue?

A synonym tool that helps users find the best word to complete a sentence using natural language APIs. 
When the program runs, the user inputs a sentence with a blank (_) and some words, and the software suggests the best fitting synonym in context.

## Problem Statement

Many people struggle to recall the "perfect" word in a given context. This software solves that by suggesting a synonym that fits naturally in a setence, using Words API to get the synoyms and Gemini API to complete the sentence.

According to studies, the tip-of-the-tongue phenomenon is universal, and most languages use the same metaphor to describe the sensation of having a word on the tip of one's tongue.

## How It Works

- User enters a sentence with a blank (_)
- User provides a list of words they’re considering
- The software fetches synonyms for each word via [WordsAPI](https://www.wordsapi.com/)
- Synonyms and the sentence are stored in an SQLite database
- Gemini (Google’s GenAI) uses the context to suggest the best synonym
- Final sentence suggestion and a list of the top 5 synonnyms that can be used in that context is printed

## Technologies Used

- Python
- SQLite (via SQLAlchemy)
- [WordsAPI](https://www.wordsapi.com/) — for synonyms
- [Gemini GenAI](https://aistudio.google.com/app/apikey) - for sentence completion
- Environment variables for API keys

## Setup Instructions

1. Clone this repository: ```git clone https://github.com/Yabsram/dictionary_Project.git``` ```cd dictionary_Project```
2. Install dependencies: ```pip install -r requirements.txt```
3. Add your API keys in a ``.env`` file or directly set environment variables
   - ```export GENAI_KEY="your_gemini_api_key"```
   - ```export WORDSAPI_KEY="your_wordsapi_key"```
4. Then run, ```python3 main.py``` in the terminal


## Team Members

- Soliat A. ``` WordsAPI Integration ```
- Yabsra M. ``` Database logic ```
- Royal I.  ``` GeminiAPI Integration ```
   
     
