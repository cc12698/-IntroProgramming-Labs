animalAns = {'cow','Cow', 'COW', 'cOw', 'coW', 'CoW', 'cOW', 'COw'}


yes = {'yes'}

no = {'no'}

Thinking = "the computer is thinking on an animal"

leave = "if you would like to exit type quit"

print(Thinking)
print(leave)

guess = "can you guess the animal? "

congratulations = "that is the correct animal, thanks for playing"

sorry = "sorry that is not the correct animal"

like = "do you like the animal?"

while True:
    guess = (input('can you guess the animal? '))
    if guess in animalAns:
        print (congratulations)
        like = (input('do you like the animal?'))
        if like in yes:
            print("Great!")
            break
        elif like in no:
            print("Thats too bad.")
            break
        else:
            print("that is not an answer")
    elif guess[0]== "q":
        break
    elif guess[0]== "Q":
        break
    else:
        print (sorry)
        
    
