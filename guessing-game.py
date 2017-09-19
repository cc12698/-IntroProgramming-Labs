animalAns = {'cow','Cow', 'COW', 'cOw', 'coW', 'CoW', 'cOW', 'COw'}

leaveGame = {'Quit', 'quit', 'QUIT'}

Thinking = "the computer is thinking on an animal"

leave = "if you would like to exit type quit"

print(Thinking)
print(leave)

guess = "can you guess the animal? "

congratulations = "that is the correct animal, thanks for playing"

sorry = "sorry that is not the correct animal"

while True:
    guess = (input('can you guess the animal? '))
    if guess in animalAns:
        print (congratulations)
        break
    elif guess in leaveGame:
        break
    else:
        print (sorry)
        
    
