# CMPT 120 - Lab #6
# YOUR NAME
# DD-MMM-YYYY
###
def showIntro():
 print("Welcome to the Arithmetic Engine!")
 print("=================================\n")
 print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")
def showOutro():
 print("\nThank you for using the Arithmetic Engine…")
 print("\nPlease come back again soon!")
def doLoop():
 while True:
     cmd = input("What computation do you want to perform? ")
     num1 = int(input("Enter the first number: "))
     num2 = int(input("Enter the second number: "))
     if cmd.lower == "add":
         result = num1 + num2
         print("The result is " + str(result) + ".\n")
     elif cmd.lower == "sub":
         result = num1 - num2
         print("The result is " + str(result) + ".\n")
     elif cmd.lower == "mult":
         result = num1 * num2
         print("The result is " + str(result) + ".\n")
     elif cmd.lower == "div":
         result = num1 // num2
         print("The result is " + str(result) + ".\n")
     elif cmd.lower == "quit":
         break
 
def main():
 showIntro()
 doLoop()
 showOutro()
main()
