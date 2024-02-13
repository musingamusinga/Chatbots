from flask import Flask, render_template, request
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

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = chatbot.respond(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
