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

def num():
    global num1, num2
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except:
        num()
    

def doLoop():
 while True:
     cmd = input("What computation do you want to perform? ")
     if cmd.lower() == "add":
         num()
         result = num1 + num2
         print("The result is " + str(result) + ".\n")
     elif cmd.lower() == "sub":
         num()
         result = num1 - num2
         print("The result is " + str(result) + ".\n")
     elif cmd.lower() == "mult":
         num()
         result = num1 * num2
         print("The result is " + str(result) + ".\n")
     elif cmd.lower() == "div":
         num()
         try:
             result = num1 // num2
             print("The result is " + str(result) + ".\n")
         except:
             print("Unable to divide by zero!")
             continue
         
     elif cmd.lower() == "quit":
         break
     else:
         print("I'm sorry that is not a valid response")

     
 
def main():
 showIntro()
 doLoop()
 showOutro()
main()
