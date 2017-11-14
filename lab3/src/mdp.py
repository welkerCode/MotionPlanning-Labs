'''

'''

import numpy as np

def getTransition(modelSwitch, actionType, currentState, desiredAction, complProb):

    # Here, I need to determine the actions that are possible and their probabilities
    if actionType == "lateral":
        if desiredAction == 'u':
            desiredState = (currentState[0], currentState[1] + 1)   # Up
            errorState1  = (currentState[0] + 1, currentState[1])   # Left
            errorState2  = (currentState[0] - 1, currentState[1])   # Right
        elif desiredAction == 'd':
            desiredState = (currentState[0], currentState[1] - 1)   # Down
            errorState1  = (currentState[0] - 1, currentState[1])   # Right
            errorState2  = (currentState[0] + 1, currentState[1])   # Left
        elif desiredAction == 'l':
            desiredState = (currentState[0] + 1, currentState[1])   # Left
            errorState1  = (currentState[0], currentState[1] - 1)   # Down
            errorState2  = (currentState[0], currentState[1] + 1)   # Up
        else:
            desiredState = (currentState[0] - 1, currentState[1])   # Right
            errorState1  = (currentState[0], currentState[1] + 1)   # Up
            errorState2  = (currentState[0], currentState[1] - 1)   # Down
        errorStateProb = (1 - complProb) / 2  # Calculate the probability of each errorState

    elif actionType == "diagonal":
        if desiredAction == 'u':
            desiredState = (currentState[0], currentState[1] + 1)       # Up
            errorState1  = (currentState[0] + 1, currentState[1] + 1)   # NorthWest
            errorState2  = (currentState[0] - 1, currentState[1] + 1)   # NorthEast
        elif desiredAction == 'd':
            desiredState = (currentState[0], currentState[1] - 1)       # Down
            errorState1  = (currentState[0] - 1, currentState[1] - 1)   # SouthEast
            errorState2  = (currentState[0] + 1, currentState[1] - 1)   # SouthWest
        elif desiredAction == 'l':
            desiredState = (currentState[0] + 1, currentState[1])       # Left
            errorState1  = (currentState[0] + 1, currentState[1] - 1)   # NorthWest
            errorState2  = (currentState[0] + 1, currentState[1] + 1)   # SouthWest
        elif desiredAction == 'r':
            desiredState = (currentState[0] - 1, currentState[1])       # Right
            errorState1  = (currentState[0] - 1, currentState[1] + 1)   # NorthEast
            errorState2  = (currentState[0] - 1, currentState[1] - 1)   # SouthWest
        elif desiredAction == 'nw':
            desiredState = (currentState[0] + 1, currentState[1] + 1)   # NorthWest
            errorState1  = (currentState[0] + 1, currentState[1])       # West
            errorState2  = (currentState[0], currentState[1] + 1)       # North
        elif desiredAction == 'ne':
            desiredState = (currentState[0] - 1, currentState[1] + 1)   # NorthEast
            errorState1  = (currentState[0], currentState[1] + 1)       # North
            errorState2  = (currentState[0] - 1, currentState[1])       # East
        elif desiredAction == 'sw':
            desiredState = (currentState[0] + 1, currentState[1] - 1)   # Southwest
            errorState1  = (currentState[0], currentState[1] - 1)       # South
            errorState2  = (currentState[0] + 1, currentState[1])       # West
        elif desiredAction == 'se':
            desiredState = (currentState[0] - 1, currentState[1] - 1)   # SouthEast
            errorState1 = (currentState[0] - 1, currentState[1])        # East
            errorState2 = (currentState[0], currentState[1] - 1)        # South
        errorStateProb = (1 - complProb) / 2  # Calculate the probability of each errorState

    else:
        if desiredAction == 'u':
            desiredState = (currentState[0], currentState[1] + 1)       # Up
            errorState1  = (currentState[0] + 1, currentState[1] + 1)   # NorthWest
            errorState2  = (currentState[0] - 1, currentState[1] + 1)   # NorthEast
            errorState3  = (currentState[0] + 1, currentState[1])       # Left
            errorState4  = (currentState[0] - 1, currentState[1])       # Right
        elif desiredAction == 'd':
            desiredState = (currentState[0], currentState[1] - 1)       # Down
            errorState1  = (currentState[0] - 1, currentState[1] - 1)   # SouthEast
            errorState2  = (currentState[0] + 1, currentState[1] - 1)   # SouthWest
            errorState3  = (currentState[0] - 1, currentState[1])       # Right
            errorState4  = (currentState[0] + 1, currentState[1])       # Left
        elif desiredAction == 'l':
            desiredState = (currentState[0] + 1, currentState[1])       # Left
            errorState1  = (currentState[0] + 1, currentState[1] - 1)   # NorthWest
            errorState2  = (currentState[0] + 1, currentState[1] + 1)   # SouthWest
            errorState3  = (currentState[0], currentState[1] - 1)       # Down
            errorState4  = (currentState[0], currentState[1] + 1)       # Up
        elif desiredAction == 'r':
            desiredState = (currentState[0] - 1, currentState[1])       # Right
            errorState1  = (currentState[0] - 1, currentState[1] + 1)   # NorthEast
            errorState2  = (currentState[0] - 1, currentState[1] - 1)   # SouthWest
            errorState3  = (currentState[0], currentState[1] + 1)       # Up
            errorState4  = (currentState[0], currentState[1] - 1)       # Down
        elif desiredAction == 'nw':
            desiredState = (currentState[0] + 1, currentState[1] + 1)   # NorthWest
            errorState1 = (currentState[0] + 1, currentState[1])        # West
            errorState2 = (currentState[0], currentState[1] + 1)        # North
            errorState3 = (currentState[0] - 1, currentState[1] - 1)    # SouthWest
            errorState4 = (currentState[0] - 1, currentState[1] + 1)    # NorthEast
        elif desiredAction == 'ne':
            desiredState = (currentState[0] - 1, currentState[1] + 1)   # NorthEast
            errorState1 = (currentState[0], currentState[1] + 1)        # North
            errorState2 = (currentState[0] - 1, currentState[1])        # East
            errorState3 = (currentState[0] + 1, currentState[1] + 1)    # NorthWest
            errorState4 = (currentState[0] - 1, currentState[1] - 1)    # SouthEast
        elif desiredAction == 'sw':
            desiredState = (currentState[0] + 1, currentState[1] - 1)   # Southwest
            errorState1 = (currentState[0], currentState[1] - 1)        # South
            errorState2 = (currentState[0] + 1, currentState[1])        # West
            errorState3 = (currentState[0] - 1, currentState[1] - 1)    # SouthEast
            errorState4 = (currentState[0] + 1, currentState[1] + 1)    # NorthWest
        elif desiredAction == 'se':
            desiredState = (currentState[0] - 1, currentState[1] - 1)   # SouthEast
            errorState1 = (currentState[0] - 1, currentState[1])        # East
            errorState2 = (currentState[0], currentState[1] - 1)        # South
            errorState3 = (currentState[0] - 1, currentState[1] + 1)    # NorthEast
            errorState4 = (currentState[0] + 1, currentState[1] - 1)    # Southwest
        errorStateProb = .1    # Calculate the probability of each errorState
        errorStateProb2 = .05

    if modelSwitch == True:
        # If we enter this loop, we will return a list of 2-tuples holding the states and probability
        returnList = []
        returnList.append((desiredState, complProb))
        returnList.append((errorState1, errorStateProb))
        returnList.append((errorState2, errorStateProb))
        if actionType == "both":
            returnList.append((errorState3, errorStateProb2))
            returnList.append((errorState3, errorStateProb2))
        return returnList
    else:
        # If we enter this loop, we will return a random state
        randomInt = np.random.randint(0, 99, 1) # Create a random number generator
        randProb = randomInt / 100.0              # Scale the random number between 0 and 99

        if actionType != "both":
            if randProb < complProb:
                # If we fall in the range of the desired action's probability, return the desired state
                return desiredState
            elif complProb < randProb < (complProb + errorStateProb):
                # If we fall in the range of the first error state, return that state
                return errorState1
            else:
                # Otherwise, if we fall in the range of the second error state, return that state
                return errorState2
        else:
            if randProb < complProb:
                return desiredState
            elif randProb < randProb < complProb + errorStateProb:
                return errorState1
            elif randProb < complProb + errorStateProb < randProb < complProb + (2*errorStateProb):
                return errorState2
            elif randProb < complProb + errorStateProb < complProb + (2 * errorStateProb) < randProb < complProb + (2 * errorStateProb) + errorStateProb2:
                return errorState3
            else:
                return errorState4


def getTransitionModified(modelSwitch, actionType, currentState, transition, desiredAction, complProb):

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
            errorState1  = transition(currentState, 'w')    # West
            errorState2  = transition(currentState, 'n')    # North
        elif desiredAction == 'ne':
            desiredState = transition(currentState, 'ne')   # NorthEast
            errorState1  = transition(currentState, 'n')    # North
            errorState2  = transition(currentState, 'e')    # East
        elif desiredAction == 'sw':
            desiredState = transition(currentState, 'sw')   # Southwest
            errorState1  = transition(currentState, 's')    # South
            errorState2  = transition(currentState, 'w')    # West
        elif desiredAction == 'se':
            desiredState = transition(currentState, 'se')   # SouthEast
            errorState1 = transition(currentState, 'e')     # East
            errorState2 = transition(currentState, 's')     # South
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
            errorState1  = transition(currentState, 'w')    # West
            errorState2  = transition(currentState, 'n')    # North
            errorState3  = transition(currentState, 'sw')   # SouthWest
            errorState4  = transition(currentState, 'ne')   # NorthEast
        elif desiredAction == 'ne':
            desiredState = transition(currentState, 'ne')   # NorthEast
            errorState1  = transition(currentState, 'n')    # North
            errorState2  = transition(currentState, 'e')    # East
            errorState3  = transition(currentState, 'nw')   # NorthWest
            errorState4  = transition(currentState, 'se')   # SouthEast
        elif desiredAction == 'sw':
            desiredState = transition(currentState, 'sw')   # Southwest
            errorState1  = transition(currentState, 's')    # South
            errorState2  = transition(currentState, 'w')    # West
            errorState3  = transition(currentState, 'se')   # SouthEast
            errorState4  = transition(currentState, 'nw')   # NorthWest
        elif desiredAction == 'se':
            desiredState = transition(currentState, 'se')   # SouthEast
            errorState1  = transition(currentState, 'e')    # East
            errorState2  = transition(currentState, 's')    # South
            errorState3  = transition(currentState, 'ne')   # NorthEast
            errorState4  = transition(currentState, 'sw')   # Southwest
        errorStateProb = .1    # Calculate the probability of each errorState
        errorStateProb2 = .05

    returnStates = {}
    returnStates[desiredState] = complProb
    returnStates[errorState1] = returnStates.get(errorState1, 0)
    returnStates[errorState2] = returnStates.get(errorState2, 0)

    if actionType != "lateral" and actionType != 'diagonal':
        returnStates[errorState3] = returnStates.get(errorState3, 0)
        returnStates[errorState4] = returnStates.get(errorState4, 0)

    if modelSwitch == True:
        for key in returnStates.keys():
            print(key)


        # If we enter this loop, we will return a list of 2-tuples holding the states and probability
        returnList = []
        returnList.append((desiredState, complProb))
        returnList.append((errorState1, errorStateProb))
        returnList.append((errorState2, errorStateProb))
        if actionType == "both":
            returnList.append((errorState3, errorStateProb2))
            returnList.append((errorState3, errorStateProb2))
        return returnList
    else:
        # If we enter this loop, we will return a random state
        randomInt = np.random.randint(0, 99, 1) # Create a random number generator
        randProb = randomInt / 100.0              # Scale the random number between 0 and 99

        if actionType != "both":
            if randProb < complProb:
                # If we fall in the range of the desired action's probability, return the desired state
                return desiredState
            elif complProb < randProb < (complProb + errorStateProb):
                # If we fall in the range of the first error state, return that state
                return errorState1
            else:
                # Otherwise, if we fall in the range of the second error state, return that state
                return errorState2
        else:
            if randProb < complProb:
                return desiredState
            elif randProb < randProb < complProb + errorStateProb:
                return errorState1
            elif randProb < complProb + errorStateProb < randProb < complProb + (2*errorStateProb):
                return errorState2
            elif randProb < complProb + errorStateProb < complProb + (2 * errorStateProb) < randProb < complProb + (2 * errorStateProb) + errorStateProb2:
                return errorState3
            else:
                return errorState4
