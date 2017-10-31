
intro = "welcome to personality AI, please type in something in and the AI will respond."

anger = 0
disgust = 1
fear = 2
happiness = 3
sadness = 4
surprise = 5

               #0          1          2             3 
personality = [#reward     punish     threaten      joke
              [surprise  , None     , None        , happiness]#anger    0
             ,[surprise  , fear     , fear        , None]#disgust       1
             ,[surprise  , None     , None        , surprise]#fear      2
             ,[None      , anger    , fear        , None]#happiness     3
             ,[happiness , fear     , None        , happiness]#sadness  4
             ,[happiness , sadness  , anger       , happiness]#surprise 5
            ]

responses = ["I'm mad at you",
            "oh thats nasty",   
            "you're scaring me...",
            "Today is a good day",
            "I'm sad...",
            "Wow!"]
                


def loop():
    currEmotion = happiness

    action = getInteraction() 
    currEmotion = lookupEmotion(currEmotion, action)
    showEmotion(currEmotion)
    
    response = input("what would you like to do? ").lower()
    if response == "reward":
        print(responses[3:4])
    if response == "punish":
        print(responses[0:1])
    if response == "threaten":
        print(response[2:3])
    if response == "joke":
        print(response[3:4])
    else:
        print("that is not a valid input")
        
        
    

loop()
