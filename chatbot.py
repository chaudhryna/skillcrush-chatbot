from openai import OpenAI

client = OpenAI()

user_input = input("\nAsk something...\n\n")

model = "gpt-3.5-turbo"

messages = [
    {
        "role": "system",
        "content": "You are an AI programming assistant.",
    },
    {"role": "user", "content": user_input},
]

def set_user_input_category(user_input): 
    question_keywords = ['who', 'what', 'when', 'where', 'why', 'how', '?']
    
    for keyword in question_keywords:
        if keyword in user_input.lower():
            return "question"

def get_api_chat_response_message(model, messages):
    response = client.chat.completions.create(model=model, messages=messages)
    response_for_user = response.choices[0].message.content
    return response_for_user

response_for_user = get_api_chat_response_message(model, messages)

if set_user_input_category(user_input) == "question":
    print(f'Good question! {response_for_user}')
else:
    print(response_for_user)
    

