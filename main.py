from openai import OpenAI
import os
import colorama
from dotenv import dotenv_values

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv_values = dotenv_values(dotenv_path)

if "OPENAI_API_KEY" not in dotenv_values:
    raise ValueError("Missing OPENAI_API_KEY in .env file")

# Initialize colorama
colorama.init()

# Set up OpenAI API credentials
api_key = dotenv_values['OPENAI_API_KEY']
client = OpenAI(api_key=api_key)

def generate_response(history):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=history
    )
    return completion.choices[0].message

if __name__ == "__main__":
    while True:
        print(colorama.Fore.GREEN + "Welcome to \"two-ais-walk-into-a-bar\"! (hit ctrl-c at any point to exit)\n")
        
        ai_name_one = input("Give the first AI a name: ")
        system_prompt_one = input("Give the first AI a prompt: ")
        
        ai_name_two = input("Give the second AI a name: ")
        system_prompt_two = input("Give the second AI a prompt: ")
        
        print("\n\nStarting the conversation between " + ai_name_one + " and " + ai_name_two + "...\n\n" + colorama.Style.RESET_ALL)
        
        history1 = [
            {"role": "system", "content": system_prompt_one},
        ]
        history2 = [
            {"role": "system", "content": system_prompt_two},
        ]
        
        # Give user option to continue the conversation each time with Enter key
        while True:
            continue_str = input(colorama.Fore.CYAN + "Press Enter to continue the conversation...\n\n" + colorama.Style.RESET_ALL)
            if continue_str != "":
                break
            
            response1 = generate_response(history1)
            history1.append({"role": "assistant", "content": response1.content})
            history2.append({"role": "user", "content": response1.content})
            print(colorama.Fore.BLUE + ai_name_one + ": " + response1.content + colorama.Style.RESET_ALL + "\n")
            
            response2 = generate_response(history2)
            history2.append({"role": "assistant", "content": response2.content})
            history1.append({"role": "user", "content": response2.content})
            print(colorama.Fore.MAGENTA + ai_name_two + ": " + response2.content + colorama.Style.RESET_ALL + "\n")