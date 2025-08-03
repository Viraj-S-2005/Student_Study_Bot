print("Welcome to Study Assistant ChatBot!")
print("Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == 'exit':
        print("ChatBot: Bye! All the best for your studies! 😊")
        break

    elif "study tips" in user_input:
        print("ChatBot: Study for 25 minutes, then take a 5-minute break. Use the Pomodoro method!")

    elif "motivation" in user_input:
        print("ChatBot: Believe in yourself! Consistency is the key to success.")

    elif "time table" in user_input:
        print("ChatBot: Make a daily plan — Morning: Study core subjects, Evening: Practice coding.")

    else:
        print("ChatBot: Sorry, I don't understand that. Try asking something else.")
