
def userName():
    firstName = input('please enter your first name: ').lower()

    lastName = input('please enter your last name:').lower()

    names = [firstName,lastName]

    separator = "."

    fullName = separator.join(names)

    print(fullName)

    


userName()






