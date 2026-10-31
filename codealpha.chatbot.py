
# Basic Rule-Based Chatbot

def chatbot():
    print("===== WELCOME TO PYTHON CHATBOT =====")
    print("Type 'bye' to exit the chatbot.")

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: I'm a Python chatbot.")

        elif user_input == "what can you do":
            print("Bot: I can answer simple questions.")

        elif user_input == "thank you":
            print("Bot: You're welcome!")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()

