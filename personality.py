
intro = "welcome to personality AI, please type in something in and the AI will respond."

anger = 0
disgust = 1
fear = 2
happiness = 3
sadness = 4
surprise = 5

               #0          1          2             3 
personality = [#reward     punish     threaten      joke
              [surprise  , None     , None        , happiness]#anger    0-
             ,[surprise  , fear     , fear        , None]#disgust       1-
             ,[surprise  , None     , None        , surprise]#fear      2
             ,[None      , anger    , fear        , None]#happiness     3-
             ,[happiness , fear     , None        , happiness]#sadness  4-
             ,[happiness , sadness  , anger       , happiness]#surprise 5-
            ]

responses = ["I'm mad at you",
            "oh thats nasty",   
            "you're scaring me...",
            "Today is a good day",
            "I'm sad...",
            "Wow!"]
                


def loop():
    currEmotion = happiness
    question = "what would you like to do? "
    response = input(question).lower()

    if currEmotion == fear:
        if response == "reward":
            print(responses[5:])
            currEmotion = surprise
            print(response)
        elif response == "punish":
            print(responses[2:3])
            currEmotion = fear
            print(response)
        elif response == "threaten":
            print(response[2:3])
            currEmotion = fear
            print(response)
        elif response == "joke":
            print(response[5:0])
            currEmotion = surprise
            print(response)
        else:
            print("that is not a valid input")
            print(response)
    
    if currEmotion == anger:
        if response == "reward":
            print(responses[5:])
            currEmotion = surprise
            print(response)
        elif response == "punish":
            print(responses[4:5])
            currEmotion = anger
            print(response)
        elif response == "threaten":
            print(response[0:1])
            currEmotion = anger
            print(response)
        elif response == "joke":
            print(response[3:4])
            currEmotion = happiness
            print(response)
        else:
            print("that is not a valid input")
            print(response)
            
    if currEmotion == surprise:
        if response == "reward":
            print(responses[3:4])
            currEmotion = happiness
            print(response)
        elif response == "punish":
            print(responses[4:5])
            currEmotion = sadness
            print(response)
        elif response == "threaten":
            print(response[0:1])
            currEmotion = anger
            print(response)
        elif response == "joke":
            print(response[3:4])
            currEmotion = happiness
            print(response)
        else:
            print("that is not a valid input")
            print(response)
            
    if currEmotion == disgust:
        if response == "reward":
            print(responses[5:0])
            currEmotion = surprise
            print(response)
        elif response == "punish":
            print(responses[2:3])
            currEmotion = fear
            print(response)
        elif response == "threaten":
            print(response[2:3])
            currEmotion = fear
            print(response)
        elif response == "joke":
            print(response[3:4])
            currEmotion = disgust
            print(response)
        else:
            print("that is not a valid input")
            print(response)


    if currEmotion == happiness:
        if response == "reward":
             print(responses[3:4])
             currEmotion = happiness
             print(response)
        elif response == "punish":
             print(responses[0:1])
             currEmotion = anger
             print(response)
        elif response == "threaten":
             print(response[2:3])
             currEmotion = fear
             print(response)
        elif response == "joke":
             print(response[3:4])
             currEmotion = happiness
             print(response)
        else:
             print("that is not a valid input")
             print(response)

    if currEmotion == sadness:
        if response == "reward":
            print(responses[3:4])
            currEmotion = happiness
            print(response)
        elif response == "punish":
            print(responses[2:3])
            currEmotion = fear
            print(response)
        elif response == "threaten":
            print(response[2:3])
            currEmotion = fear
            print(response)
        elif response == "joke":
            print(response[3:4])
            currEmotion = happiness
            print(response)
        else:
            print("that is not a valid input")
            print(response)
    
        
        
    

loop()
