#Design a simple chatbot that responds differently based on user input (e.g., greetings, questions, or farewell messages).

class Chatbot:

    def respond(self,user, input):

        if input.lower() in ["hi", "hello", "hey"]:
            return f"Hello {user}, how can I assist you today?"
        elif input.lower() in ["how are you?", "how's it going?"]:
            return "I'm just a program, but I'm here to help you!"
        elif input.lower() in ["Can you help me with this?", "describe the topic?"]:
            return "Sure! What topic would you like to know more about?"
        elif input.lower() in ["bye", "goodbye", "see you later"]:
            return "Goodbye! Have a great day!"
        else:
            return "I'm not sure how to respond to that. Can you ask something else?"
        
    

