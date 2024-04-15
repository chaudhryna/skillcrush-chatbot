from openai import OpenAI

client = OpenAI()

# user_input = input("\nAsk something...\n\n")

model = "gpt-3.5-turbo"

plot_title = "The Forgotten House"

plot_description = """In the heart of the bustling metropolis of Astoria, the old Henderson House stands as a silent sentinel, its imposing facade a stark contrast to the modern skyscrapers that surround it. Once a grand mansion, it now sits abandoned, its windows broken, its once-luxurious gardens now a tangle of weeds and ivy. The house is said to be haunted, its halls echoing with the whispers of a tragic past.
 
When seventeen-year-old Mia Alvarez moves to Astoria with her family, she is immediately drawn to the mystery of the old house. Despite the warnings of her new friends, Mia becomes determined to uncover the truth behind the rumors that surround it."""

plot_prompt = f"""
Summarize the text, {plot_description}, in no more than 100 words.

Write this as one paragraph, make sure the title, {plot_title}, is in the summary and make the summarization exciting. This text will be used to promote the launch of a new book.
"""

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    },
    {"role": "user", "content": plot_prompt},
]

# def set_user_input_category(user_input):
#     question_keywords = ['who', 'what', 'when', 'where', 'why', 'how', '?']

#     for keyword in question_keywords:
#         if keyword in user_input.lower():
#             return "question"

def get_api_chat_response_message(model, messages):
    response = client.chat.completions.create(model=model, messages=messages)
    book_summary = response.choices[0].message.content
    return book_summary

book_summary = get_api_chat_response_message(model, messages)

# if set_user_input_category(user_input) == "question":
#     print(f"Good question! {book_summary}")
# else:

print(book_summary)
