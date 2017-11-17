from param import _GOAL_REWARD
from param import _CORNER_REWARD
from param import _OTHER_STATE_REWARD
from param import _DISCOUNT_FACTOR
from param import _NUM_ITER
from param import _LIST_SWITCH
from param import _COMPLETION_PROB
from param import _ACTION_TYPE
from param import _EPSILON
from graph_search import _ACTIONS
from graph_search import _ACTIONS_2
from mdp import getTransition

import numpy as np

# This function is called before entering any iterations; it sets up the initial table
def initTable(gm):

    d = {}  # Create a new dictionary

    for x in range(0, gm.rows):
        for y in range(0, gm.cols):

            # For every spot on the map
            if not gm.occupancy_grid[x][y]:
                startingVal = getStartingReward((x,y), gm)  # Get the starting reward value for that spot
                d[(x,y)] = startingVal                      # Add it to the dictionary

    return d    # Return the dictionary when you are done


# This function runs the valueIteration on the specified map
def valueIter(gm):
    '''

    Pseudocode:
        create 2 dictionaries, one for the previous iteration's data, and one to hold the new data
        for every iteration
            for every state in the dictionary
                calculate vg
                update the dictionary
                    dictionary{state:reward}
            advance the dictionaries
            print the table
        print the final table
    '''

    # Create the two dictionaries
    origTable = initTable(gm)
    prevIterTable = initTable(gm)   # Fill the prevIteration Dictionary with the initial reward values
    newIterTable = {}               # Initialize a new, empty dictionary

    convergence = False
    iterationCount = 0

    if _ACTION_TYPE == 'lateral':
        actions = _ACTIONS
    else:
        actions = _ACTIONS_2

    while convergence == False:
        # For every iteration up to the limit we specified
        iterationCount += 1
        for y in range(0, gm.cols):
            for x in range(0, gm.rows):
                # For every location in the map
                if gm.occupancy_grid[x][y] == False:
                    maxVg = None
                    for action in actions:
                        # For every possible action at that location?????????

                        transList = getTransition(_LIST_SWITCH,_ACTION_TYPE,(x,y),gm.transition,action,_COMPLETION_PROB) # Get the transition model
                        vgnew = calcStateVal((x,y),transList, prevIterTable, origTable) # Calculate Vg
                        if maxVg is None or maxVg < vgnew:
                            maxVg = vgnew
                    newIterTable[(x,y)] = maxVg                        # Add the Vg to the dictionary that holds new information for the current iteration

        # After going through all of the states on the map for that iteration, check the epsilon change for convergence
        convergence = True
        for state in prevIterTable:
            oldVal = prevIterTable.get(state)
            newVal = newIterTable.get(state)
            # If we find a state that hasn't converged yet
            if np.abs(oldVal - newVal) > _EPSILON:
                convergence = False     # Stay in the loop
        # Update the two dictionaries
        prevIterTable = newIterTable    # Set the recently completed dictionary as the old dictionary
        newIterTable = {}               # Initialize a new dictionary

    print("Number of Iterations: ", iterationCount)
    gm.display_ValueIterMap(prevIterTable)



    # Now, I have to determine the policy of each state on the map
    policyDict = getPolicyDict(prevIterTable, gm)
    gm.display_PolicyMap(policyDict)

def calcStateVal(currentState, transitionModel, stateDictionary, origStateDictionary):
    '''
    for every possible new state
        find the probability of going to that state
        find the reward of going to that state (0 if not goal)
        Add the product to the sum
    multiply that sum by lambda
    store that value...somewhere that can be read from again
    table of states?



    Vs = rs + lambda*sum(prob + reward)

    rs = LAST ITER VALUE
    sumOfIter = 0
    for transition in transitionModel:
        state = transition[0]
        prob = transition[1]
        reward = getReward(state, gm)
        sumOfIter += prob*reward
    Vg = rs + _DISCOUNT_FACTOR*sumOfIter
    return Vg or store in dictionary


    :param transitionModel:
    :return:
    '''
    rs = origStateDictionary.get(currentState)
    sumOfIter = 0
    for transition in transitionModel:
        newState = transition[0]
        prob = transition[1]
        reward = stateDictionary.get(newState)
        sumOfIter += prob*reward

    vg = rs + _DISCOUNT_FACTOR*sumOfIter
    return vg

def getPolicyDict(previousIterTable, gm):
    policyDict = {}

    if _ACTION_TYPE == 'lateral':
        actions = _ACTIONS
    else:
        actions = _ACTIONS_2

    for y in range(0, gm.cols):
        for x in range(0, gm.rows):
            # For every location in the map
            if gm.occupancy_grid[x][y] == False:
                desiredAction = None
                desiredActionVal = None
                for action in actions:
                    newState = gm.transition((x,y),action)
                    newActionVal = previousIterTable.get(newState)
                    if desiredAction == None or desiredActionVal == None or desiredActionVal < newActionVal:
                        desiredActionVal = newActionVal
                        desiredAction = action
                policyDict[(x,y)] = desiredAction
    return policyDict

# This calculates the starting reward based upon the location of the state
def getStartingReward(state, gridMap):
    if gridMap.is_goal(state):
        return _GOAL_REWARD
    elif state == (0,0) or state == (0, gridMap.cols - 1) or state == (gridMap.rows - 1, 0) or state == (gridMap.rows - 1, gridMap.cols - 1):
        return _CORNER_REWARD
    else:
        return _OTHER_STATE_REWARD

stateVal = {}

