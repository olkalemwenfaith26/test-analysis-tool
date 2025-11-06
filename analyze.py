# Welcome User
def welcomeUser():
 print("\nwelcome to the text analyze tool, i will mine and analyze a body of text from a file you give me!")

#Get Username
def getUsername():
    #print message prompting user to input name
    UsernameFromInput = input("\nTo begin, please enter your Username:\n")
    return UsernameFromInput

# Greet the user
def greetUser(name):
    print("Hello, " + name)

welcomeUser()
username = getUsername()
greetUser(username)
