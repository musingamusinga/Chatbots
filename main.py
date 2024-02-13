import nltk
import random
from nltk.chat.util import Chat, reflections

# Define responses for the chatbot
responses = {
    "hi": "Hello!",
    "how are you": "I'm doing well, thank you!",
    "what's your name": "I'm a chatbot!",
    "default": "Sorry, I didn't understand that."
}

# Define patterns for the chatbot
patterns = [
    (r"hi|hello|hey", ["Hi there!", "Hello!", "Hey!"]),
    (r"how are you|how's it going", ["I'm doing well, thank you!"]),
    (r"what's your name|who are you", ["I'm a chatbot!"]),
]

# Create a chatbot using NLTK's Chat class
chatbot = Chat(patterns, responses)

# Define main function to interact with the chatbot
def main():
    print("Welcome! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Bot:", response)

# Run the main function
if __name__ == "__main__":
    main()
