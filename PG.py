import random

def generatePassword():
    pass
def replaceWithNum():
    pass
def replacewithUpperCase():
    pass
def main():
    numPassWord = int(input("Enter the No. Of do you want to generate : "))

    print("Generating "+numPassWord+" Passwords.")

    passwordLeangth = []

    print("Minimum length of password should be 4")

    for i in range(numPassWord):
        length = int(input("Enter the leangth of the Password #"+str(i+1)+" : "))
        if length<4:
            length=4
        passwordLeangth.append(length)

    password = generatePassword(passwordLeangth)

    for i in range (numPassWord):
        print("Password #"+str(i+1)+" = "+password[i])