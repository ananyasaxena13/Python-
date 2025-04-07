import Chatbot

chat = Chatbot.Chatbot()

print("Welcome to the Chatbot!")
user = input("Please enter your name: ")
while True:
    response = chat.respond(user, input("You: "))
    print("Chatbot:", response)
    if response in ["Goodbye! Have a great day!"]:
        break
