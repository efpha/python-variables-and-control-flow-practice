# User enter input repeatedly until they type exit (not case sensitive)

def requestUserInput():
    while True:
        userInput = input("Enter an input: ")
        print(userInput)

        # Avoid case sensitivity
        lowerCase_userInput = userInput.lower()

        if lowerCase_userInput == "exit":
            break


requestUserInput()
