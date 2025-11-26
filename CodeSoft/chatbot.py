# Simple Chatbot 
def chatbot_response(user_input):

    user_input = user_input.lower() 

    # Greeting chatbot responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    # Ask chatbot's name
    elif "your name" in user_input:
        return "I am a simple rule-based chatbot system ."

    # Ask about weather
    elif "weather" in user_input:
        return "I cannot check real-time weather, but it’s always a good time weather"

    # Asking about time
    elif "time" in user_input:
        return "I can't tell the exact time, but it's always a good time to learn something new!"
    
    # Ask chatbot's inventor name 
    elif "inventor_name" in user_input:
        return "I don't know who is my inventor. can you try different something question to ask ? "
                 
    # Farewell
    elif "bye" in user_input or "goodbye" in user_input:
        return " Goodbye! Have a good day with new technology and ideas!"

    # Default response
    else:
        return "Sorry, I didn't understand that. Can you repeated this sentence ?"

# Running
print("Chatbot: Hello! Type something to begin (type 'bye' to exit).")

while True:
    user_text = input("You: ")

    if "bye" in user_text.lower():
        print("Chatbot: Goodbye!")
        break

    response = chatbot_response(user_text)
    print("Chatbot:", response)

