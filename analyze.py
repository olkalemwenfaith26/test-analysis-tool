from random_username.generate import generate_username

# Welcome User
def welcomeUser():
 print("\nwelcome to the text analyze tool, i will mine and analyze a body of text from a file you give me!")

#Get Username
def getUserName():

    maxAttempts = 3
    attempts = 0

    while attempts < maxAttempts:

        #print message prompting user to input name
        inputPrompt = ""
        if attempts == 0:
            inputPrompt = "\nTo begin, please enter your Username:\n"
        else:     
         inputPrompt = "\nPlease try again:\n"
        userNameFromInput = input(inputPrompt)

        #validate username
        if len(userNameFromInput) < 5 or not userNameFromInput.isidentifier():
         print("Your Username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9), have no spaces, and cannot start with a number!")
        else:
            return userNameFromInput

        attempts += 1

    print("\nExhausted all " + str(maxAttempts) + "  attempts, assiging username instead...")
    return generate_username()[0]
      
    
                        
# Greet the user
def greetUser(name):
    print("Hello, " + name)

welcomeUser()
userName = getUserName()
greetUser(userName)
