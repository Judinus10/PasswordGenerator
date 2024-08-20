import random  

# Function to generate passwords based on the specified lengths
def generatePassword(pwLeangth):

    alphabet = "abcdefghijklmnopqrstuvwxyz"  # String containing all lowercase letters
    
    password_list = []  # List to store the generated passwords

    # Loop through each desired password length
    for i in pwLeangth:

        password = ""  # Initialize an empty string for the password

        # Generate a random sequence of characters based on the length
        for j in range(i):

            nextLetterIndex = random.randrange(len(alphabet))  # Get a random index
            
            password = password + alphabet[nextLetterIndex]  # Append the corresponding letter
        
        password = replaceWithNum(password)  # Replace some characters with numbers
        password = replacewithUpperCase(password)  # Replace some characters with uppercase letters

        password_list.append(password)  # Add the generated password to the list

    return password_list  # Return the list of generated passwords

# function to replace some characters with numbers
def replaceWithNum(password):
    pass

# function to replace some characters with uppercase letters
def replacewithUpperCase(password):
    pass

# Main function to interact with the user and generate the passwords
def main():
    numPassWord = int(input("Enter the number of passwords you want to generate: "))

    print("Generating " + str(numPassWord) + " passwords.")

    passwordLeangth = []  # List to store the desired lengths of each password

    print("Minimum length of password should be 4")

    # Loop to collect the desired length for each password
    for i in range(numPassWord):
        length = int(input("Enter the length of Password #" + str(i + 1) + " : "))
        if length < 4:  # Ensure the minimum password length is 4
            length = 4
        passwordLeangth.append(length)

    # Generate the passwords
    password = generatePassword(passwordLeangth)

    # Print each generated password
    for i in range(numPassWord):
        print("Password #" + str(i + 1) + " = " + password[i])

# Entry point of the program
main() 
