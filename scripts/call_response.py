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
# 6
# 7
# 8
# 9

i01.ear.addCommand("wave your hand", "i01.rightArm", "wave")
i01.ear.addCommand("self destruct", "python", "selfDestructRoutine")

def selfDestructRoutine():
    i01.mouth.speak("Initiating self destruction sequence. Just kidding!")
    i01.head.lookAt(0, 10, 0) # Look up