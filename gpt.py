import openai


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


conversation = [{"role": "system", "content": "You are a helpful assistant."}]


print(f"{bcolors.WARNING} \n HAL: \n I am ready to hear your query \n {bcolors.ENDC}")

while True:
    user_input = input("")
    conversation.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=conversation
    )

    conversation.append(
        {"role": "assistant", "content": response["choices"][0]["message"]["content"]}
    )
    gpt_reply = "\n" + response["choices"][0]["message"]["content"] + "\n"

    print(f"{bcolors.WARNING} \n HAL: {gpt_reply}  {bcolors.ENDC}")
