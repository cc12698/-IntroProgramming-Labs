n = int(input("what number place would you like to find? ")

current,previous = 1,1

for i in range (n-2)
        current,previous = current+previous, current

print (current)
