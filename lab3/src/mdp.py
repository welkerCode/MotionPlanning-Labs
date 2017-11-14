'''

'''

import numpy as np

def getTransition(modelSwitch, actionType, currentState, transition, desiredAction, complProb):
    # Here, I need to determine the actions that are possible and their probabilities
    if actionType == "lateral":
        if desiredAction == 'u':
            desiredState = transition(currentState, 'u')    # Up
            errorState1  = transition(currentState, 'l')    # Left
            errorState2  = transition(currentState, 'r')    # Right
        elif desiredAction == 'd':
            desiredState = transition(currentState, 'd')   # Down
            errorState1  = transition(currentState, 'r')   # Right
            errorState2  = transition(currentState, 'l')   # Left
        elif desiredAction == 'l':
            desiredState = transition(currentState, 'l')   # Left
            errorState1  = transition(currentState, 'd')   # Down
            errorState2  = transition(currentState, 'u')   # Up
        else:
            desiredState = transition(currentState, 'r')   # Right
            errorState1  = transition(currentState, 'u')   # Up
            errorState2  = transition(currentState, 'd')   # Down
        errorStateProb = (1 - complProb) / 2  # Calculate the probability of each errorState

    elif actionType == "diagonal":
        if desiredAction == 'u':
            desiredState = transition(currentState, 'u')    # Up
            errorState1  = transition(currentState, 'nw')   # NorthWest
            errorState2  = transition(currentState, 'ne')   # NorthEast
        elif desiredAction == 'd':
            desiredState = transition(currentState, 'd')    # Down
            errorState1  = transition(currentState, 'se')   # SouthEast
            errorState2  = transition(currentState, 'sw')   # SouthWest
        elif desiredAction == 'l':
            desiredState = transition(currentState, 'l')    # Left
            errorState1  = transition(currentState, 'nw')   # NorthWest
            errorState2  = transition(currentState, 'sw')   # SouthWest
        elif desiredAction == 'r':
            desiredState = transition(currentState, 'r')    # Right
            errorState1  = transition(currentState, 'ne')   # NorthEast
            errorState2  = transition(currentState, 'se')   # SouthEast
        elif desiredAction == 'nw':
            desiredState = transition(currentState, 'nw')   # NorthWest
            errorState1  = transition(currentState, 'l')    # Left
            errorState2  = transition(currentState, 'u')    # Up
        elif desiredAction == 'ne':
            desiredState = transition(currentState, 'ne')   # NorthEast
            errorState1  = transition(currentState, 'u')    # Up
            errorState2  = transition(currentState, 'r')    # Right
        elif desiredAction == 'sw':
            desiredState = transition(currentState, 'sw')   # Southwest
            errorState1  = transition(currentState, 'd')    # Down
            errorState2  = transition(currentState, 'l')    # Left
        elif desiredAction == 'se':
            desiredState = transition(currentState, 'se')   # SouthEast
            errorState1 = transition(currentState, 'r')     # Right
            errorState2 = transition(currentState, 'd')     # Down
        errorStateProb = (1 - complProb) / 2  # Calculate the probability of each errorState

    else:
        if desiredAction == 'u':
            desiredState = transition(currentState, 'u')    # Up
            errorState1  = transition(currentState, 'nw')   # NorthWest
            errorState2  = transition(currentState, 'ne')   # NorthEast
            errorState3  = transition(currentState, 'l')    # Left
            errorState4  = transition(currentState, 'r')    # Right
        elif desiredAction == 'd':
            desiredState = transition(currentState, 'd')    # Down
            errorState1  = transition(currentState, 'se')   # SouthEast
            errorState2  = transition(currentState, 'sw')   # SouthWest
            errorState3  = transition(currentState, 'r')    # Right
            errorState4  = transition(currentState, 'l')    # Left
        elif desiredAction == 'l':
            desiredState = transition(currentState, 'l')    # Left
            errorState1  = transition(currentState, 'nw')   # NorthWest
            errorState2  = transition(currentState, 'sw')   # SouthWest
            errorState3  = transition(currentState, 'd')    # Down
            errorState4  = transition(currentState, 'u')    # Up
        elif desiredAction == 'r':
            desiredState = transition(currentState, 'r')    # Right
            errorState1  = transition(currentState, 'ne')   # NorthEast
            errorState2  = transition(currentState, 'se')   # SouthEast
            errorState3  = transition(currentState, 'u')    # Up
            errorState4  = transition(currentState, 'd')    # Down
        elif desiredAction == 'nw':
            desiredState = transition(currentState, 'nw')   # NorthWest
            errorState1  = transition(currentState, 'l')    # Left
            errorState2  = transition(currentState, 'u')    # Up
            errorState3  = transition(currentState, 'sw')   # SouthWest
            errorState4  = transition(currentState, 'ne')   # NorthEast
        elif desiredAction == 'ne':
            desiredState = transition(currentState, 'ne')   # NorthEast
            errorState1  = transition(currentState, 'u')    # Up
            errorState2  = transition(currentState, 'r')    # Right
            errorState3  = transition(currentState, 'nw')   # NorthWest
            errorState4  = transition(currentState, 'se')   # SouthEast
        elif desiredAction == 'sw':
            desiredState = transition(currentState, 'sw')   # Southwest
            errorState1  = transition(currentState, 'd')    # Down
            errorState2  = transition(currentState, 'l')    # Left
            errorState3  = transition(currentState, 'se')   # SouthEast
            errorState4  = transition(currentState, 'nw')   # NorthWest
        elif desiredAction == 'se':
            desiredState = transition(currentState, 'se')   # SouthEast
            errorState1  = transition(currentState, 'r')    # Right
            errorState2  = transition(currentState, 'd')    # Down
            errorState3  = transition(currentState, 'ne')   # NorthEast
            errorState4  = transition(currentState, 'sw')   # Southwest
        errorStateProb = .1    # Calculate the probability of each errorState
        errorStateProb2 = .05

    returnStates = {}   # Create a dictionary to hold the potential states that we could be in with their probabilities
    returnStates[desiredState] = complProb  # Add the desired state to the dictionary
    returnStates[errorState1] = returnStates.get(errorState1, 0) + errorStateProb # Add the other options.  If they result
    returnStates[errorState2] = returnStates.get(errorState2, 0) + errorStateProb #...in a repeat state, add probabilities

    if actionType != "lateral" and actionType != 'diagonal':
        returnStates[errorState3] = returnStates.get(errorState3, 0) + errorStateProb2  # Do the same for secondary error states
        returnStates[errorState4] = returnStates.get(errorState4, 0) + errorStateProb2

    if modelSwitch == True:
        # If we enter this loop, we will return a list of 2-tuples holding the states and probability
        returnList = []
        for key in returnStates.keys():                         # For every possible key
            returnList.append((key, returnStates.get(key)))     # Add the key and its probability to the list
        return returnList                                       # When that is done, return the list
    else:
        # If we enter this loop, we will return a random state
        randomInt = np.random.randint(0, 99, 1)     # Create a random number generator
        randProb = randomInt / 100.0                # Scale the random number between 0 and .99

        curProbSum = 0                              # This will hold the sum against which we will be comparing randProb

        for key in returnStates.keys():             # Get every key that can be returned
            curProbSum += returnStates.get(key)     # Add its probability to the sum
            if randProb < curProbSum:               # If the randProb is now lower than the sum
                return key                          # Return it


