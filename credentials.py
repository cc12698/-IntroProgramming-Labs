
def userName():
    firstName = input('please enter your first name: ').lower()

    lastName = input('please enter your last name:').lower()

    names = [firstName,lastName]

    separator = "."

    fullName = separator.join(names)

    print(fullName)

    userName.Email = fullName


userName()

def passWord():

    password = input("please enter a password with UpperCase, LowerCase,\nand eight or more characthers: ")

    len(password)

    while True:
        if len(password) < 8:
            print("Your password is not long enough")

            password = input('please enter a password: ')

        elif password.isupper():
            print("you need a lower case letter")

            password = input('please enter a password: ')

        elif password.islower():
            print("you need upper case letter")

            password = input('please enter a password: ')

        else:
            print('your password is good')

            break

    

passWord()

print("Your new email address is", userName.Email+"@marist.edu")




