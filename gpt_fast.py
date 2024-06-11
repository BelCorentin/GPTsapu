import os
import sys
from openai import OpenAI

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def gpt4_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content

def main():
    if len(sys.argv) > 1:
        prompt = ' '.join(sys.argv[1:])
        response = gpt4_response(prompt)
        gpt_reply = response
        print(f"{bcolors.OKCYAN} \n GPT: {gpt_reply}  {bcolors.ENDC}")
    else:
        print("Please provide a prompt")

if __name__ == "__main__":
    main()