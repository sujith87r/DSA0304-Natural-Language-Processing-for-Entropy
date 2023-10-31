import random
import re

# Define your patterns and responses
patterns = [
    (r'.* computer .*', ['Have you tried turning it off and on again?', 'Is your computer plugged in?', 'Tell me more about your computer issue.']),
    (r'.* internet .*', ['Have you checked your Wi-Fi connection?', 'Is your internet service provider having issues?', 'Please describe the internet problem in more detail.']),
    (r'.*', ['Could you please elaborate on that?', 'Tell me more, I see. Please go on.'])
]

# Define the respond function
def respond(input_text):
    input_text = input_text.lower()  # Convert input to lowercase for matching
    for pattern, responses in patterns:
        if re.match(pattern, input_text):
            response = random.choice(responses)
            return response
    return "I'm sorry, I don't understand. Can you rephrase your question?"

# Start the conversation
print("Tech Support Bot: Hi, how can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Tech Support Bot: Goodbye!")
        break
    response = respond(user_input)
    print("Tech Support Bot:", response)
