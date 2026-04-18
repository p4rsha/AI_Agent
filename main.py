# For grabbing the API Key
import os
from dotenv import load_dotenv
from prompts import system_prompt

# To make genai client 
from google import genai

# To give roles

from google.genai import types

# Grabbing Functions Schema and Call Function function
from functions.call_function import available_functions , call_function


# To allow for prompmt in the CLI
import argparse

# Grabbing API key from env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("API Key not found you dumbass")


# client object
client = genai.Client(api_key=api_key)




#initlize parser object => Yoink it's method => Easy life

parser = argparse.ArgumentParser(description= "This program is a an AI chatbot based on Gemini 2.5 Flash!")
parser.add_argument("user_prompt", type= str, help= "The prompt sent our to Gemini")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output you dumbass")
args = parser.parse_args()


#doing what here???

messeges = [types.Content(role="user" , parts=[(types.Part(text=args.user_prompt))])]

def main():
    print("Hello from Gemini!")

    response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents= messeges,
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt))


    #failsafe for metadata 
    if response.usage_metadata is None :
        raise RuntimeError("Response Metadata not found you dumbass")


    # meta-data about tokens

    prompt_token_count = response.usage_metadata.prompt_token_count
    response_token_count = response.usage_metadata.candidates_token_count

    

    #Output block
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {prompt_token_count}")
        print(f"Response tokens: {response_token_count}")

    if response.function_calls:

        #We need this later if checks pass
        function_call_result_list = []

        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
            function_call_result = call_function(function_call, verbose=args.verbose)


            # CHECK : DID WE ACTUALLY GET A RESPONSE ? __ Gemini boiler plate stuff and object structure
    
            if not function_call_result.parts:
                raise Exception("Function call result has no parts")
            
            if function_call_result.parts[0].function_response is None:
                raise Exception("Missing function_response in result")

            if function_call_result.parts[0].function_response.response is None:
                raise Exception("Missing response in function_response")
            
            function_call_result_list.append(function_call_result.parts[0])

            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")



    else:
       print(response.text)

if __name__ == "__main__":
    main()
