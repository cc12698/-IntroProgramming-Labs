animalAns = {'cow'}

Thinking = "the computer is thinking on an animal"

print(Thinking)

guess = "can you guess the animal? "

congratulations = "that is the correct animal, thanks for playing"

sorry = "sorry that is not the correct animal"

while True:
    guess = (input('can you guess the animal? '))
    if guess in animalAns:
        print (congratulations)
        break
    else:
        print (sorry)
        
    
