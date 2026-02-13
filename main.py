import os
import sys
import argparse
from google import genai
from dotenv import load_dotenv
from google.genai import types
from functions.get_files_info import get_files_info as gfi

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    system_args = sys.argv

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    prompt = args.user_prompt

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages
    )
    print(response.text)

    if response is None or response.usage_metadata is None:
        print("Resposta esta malformada")
        return 
    
    if args.verbose:
        print(f'User prompt: {messages}')
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count} ")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count} ")

print(gfi("calculator.py"))
#main()