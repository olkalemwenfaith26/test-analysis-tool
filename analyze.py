from random_username.generate import generate_username

# Welcome User
def welcomeUser():
 print("\nwelcome to the text analyze tool, i will mine and analyze a body of text from a file you give me!")

#Get Username
def getUserName():
    #print message prompting user to input name
    userNameFromInput = input("\nTo begin, please enter your Username:\n")

    if len(userNameFromInput) < 5 or not userNameFromInput.isidentifier():
        print("Your Username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9), have no spaces, and cannot start with a number!")
        userNameFromInput = generate_username()[0]
        print(userNameFromInput)
        print("Assiging new Username: " + userNameFromInput)
        return userNameFromInput
    return userNameFromInput       
  
# Greet the user
def greetUser(name):
    print("Hello, " + name)

welcomeUser()
userName = getUserName()
greetUser(userName)
