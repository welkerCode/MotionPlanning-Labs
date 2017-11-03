'''

'''

import numpy as np

def getTransition(modelSwitch, currentState, desiredAction, complProb):

    # Here, I need to determine the actions that are possible and their probabilities
    if desiredAction == 'u':
        desiredState = (currentState[0], currentState[1] - 1)   # Up
        errorState1  = (currentState[0] - 1, currentState[1])   # Left
        errorState2  = (currentState[0] + 1, currentState[1])   # Right
    elif desiredAction == 'd':
        desiredState = (currentState[0], currentState[1] + 1)   # Down
        errorState1  = (currentState[0] + 1, currentState[1])   # Right
        errorState2  = (currentState[0] - 1, currentState[1])   # Left
    elif desiredAction == 'l':
        desiredState = (currentState[0] - 1, currentState[1])   # Left
        errorState1  = (currentState[0], currentState[1] + 1)   # Down
        errorState2  = (currentState[0], currentState[1] - 1)   # Up
    else:
        desiredState = (currentState[0] + 1, currentState[1])   # Right
        errorState1  = (currentState[0], currentState[1] - 1)   # Up
        errorState2  = (currentState[0], currentState[1] + 1)   # Down

    errorStateProb = (1 - complProb) / 2    # Calculate the probability of each errorState

    if modelSwitch == True:
        # If we enter this loop, we will return a list of 2-tuples holding the states and probability

        returnList = []
        returnList.append((desiredState, complProb))
        returnList.append((errorState1, errorStateProb))
        returnList.append((errorState2, errorStateProb))
        return returnList
    else:
        # If we enter this loop, we will return a random state

        randomInt = np.random.randint(0, 99, 1) # Create a random number generator
        randProb = randomInt / 100.0              # Scale the random number between 0 and 99
        if randProb < complProb:
            # If we fall in the range of the desired action's probability, return the desired state
            return desiredState
        elif complProb < randProb < (complProb + errorStateProb):
            # If we fall in the range of the first error state, return that state
            return errorState1
        else:
            # Otherwise, if we fall in the range of the second error state, return that state
            return errorState2

        return None