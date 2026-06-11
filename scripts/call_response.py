# set up call & response info about MNM
# have a list of things ppl can ask the robot at the event that ppl can go through & attempt,
# otherwise, have the robot interface with llm

# speech recognition
# -> preset phrase -> premade response
# -> any other phrase -> interface w/ llm

# IDEAS:
# What is Made New Makerspace?
# 2
# 3
# 4
# 5
# Self Destruct
# Introduction
# Knock Knock Joke
# Shakespeare

# introduction
def who_are_you():
    i01.speakBlocking("Hello, human! I am Bob, an InMoov robot from Made New Makerspace.")
    sleep(0.25)
    i01.speakBlocking("How are you today?")
    return

# self destruct
def selfDestructRoutine():
    # add some movement here
    i01.speakBlocking("Initiating self destruction sequence.")
    sleep(0.25)
    i01.speakBlocking("5")
    sleep(0.5)
    i01.speakBlocking("4")
    sleep(0.5)
    i01.speakBlocking("3")
    sleep(0.5)
    i01.speakBlocking("2")
    sleep(0.5)
    i01.speakBlocking("1")
    sleep(0.5)
    i01.speakBlocking("Just kidding!")
     
    i01.head.lookAt(0, 10, 0) # Look up
    return
