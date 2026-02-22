import os
import sys
import argparse
from google import genai
from dotenv import load_dotenv
from google.genai import types
from call_function import config

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
        model='gemini-3-flash-preview', 
        contents=messages,
        config=config
    )
    
    if response is None or response.usage_metadata is None:
        print("Resposta esta malformada")
        return 
    
    if args.verbose:
        print(f'User prompt: {messages}')
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count} ")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count} ")

    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(response.text)

main()