import numpy as np
from param import _POLICY_INIT
from param import _POLICY_INIT_DIR
from param import _COMPLETION_PROB
from param import _ACTION_TYPE
from param import _LIST_SWITCH
from param import _DISCOUNT_FACTOR
from mdp import getTransition
from valueIter import getPolicyDict
from valueIter import initValueTable
from graph_search import *

# This function runs the valueIteration on the specified map
def policyIter(gm):

    # Create the two dictionaries
    origTable = initValueTable(gm)

    if _POLICY_INIT == 'direction':
        initPolicyDict = initDirPolicy(gm, _POLICY_INIT_DIR)
    else:
        initPolicyDict = initRandomPolicy(gm)

    gm.display_PolicyMap(initPolicyDict)


    initValDict = initValueTable(gm)
    prevPolicyDict = initPolicyDict
    prevValueDict = initValueTable(gm)


    convergence = False
    iterationCount = 0

    # while converge is false
    while convergence == False:
        iterationCount += 1 # Increment iteration counter

        # Perform policy evaluation
        newValueDict = computeValue(gm, prevPolicyDict, prevValueDict, initValDict)    # Compute value function when following policy

        # Perform policy improvement
        newPolicyDict = getPolicyDict(newValueDict, gm) # Find new optimal policy using the values computed

        # Check convergence
        convergence = checkPolicyConvergence(gm, prevPolicyDict, newPolicyDict)

        # Update dictionaries
        prevValueDict = newValueDict
        prevPolicyDict = newPolicyDict

    # Print final policy and value maps
    print("Number of iterations: ", iterationCount)
    gm.display_ValueIterMap(prevValueDict)
    gm.display_PolicyMap(prevPolicyDict)



def initDirPolicy(gm, initialDirection):
    initPolicyDict = {}
    # For every location in the map that isn't occupied
    for y in range(0, gm.cols):
        for x in range(0, gm.rows):
            if gm.occupancy_grid[x][y] == False:
                # Set the action to the initialDirection in the initial policy dictionary
                initPolicyDict[(x,y)] = initialDirection
    # Return the dictionary
    return initPolicyDict

def initRandomPolicy(gm):
    initPolicyDict = {}
    # For every location in the map that isn't occupied
    for y in range(0, gm.cols):
        for x in range(0, gm.rows):
            if gm.occupancy_grid[x][y] == False:
                # Generate a random value
                randInt = np.random.randint(0,99,1)
                randVal = randInt / 100.0
                # Define the action
                if randVal < .25:
                    action = 'u'
                elif randVal < .5:
                    action = 'd'
                elif randVal < .75:
                    action = 'l'
                else:
                    action = 'r'

                # Add it to the dictionary
                initPolicyDict[(x,y)] = action
    # Return the initial policy dictionary
    return initPolicyDict

def computeValue(gm, policyDictionary, prevValDict, initalValDict):
    newValDict = {}
    # For every location in the map that isn't occupied
    for y in range(0, gm.cols):
        for x in range(0, gm.rows):
            if gm.occupancy_grid[x][y] == False:
                # Get the action
                desiredAction = policyDictionary.get((x,y))

                # value = sum_of_all(probability * reward for new state) + old reward of current state
                # getTransition(modelSwitch, actionType, currentState, transition, desiredAction, complProb)
                transList = getTransition(_LIST_SWITCH, _ACTION_TYPE, (x,y), gm.transition, desiredAction, _COMPLETION_PROB)

                sumOfTransition = 0 # The sum of all possible transitions
                r_s = initalValDict.get((x,y))    # Original reward value
                for eligibleAction in transList:
                    futureReward = prevValDict.get(eligibleAction[0])
                    probability = eligibleAction[1]
                    sumOfTransition += futureReward*probability
                newValDict[(x,y)] = _DISCOUNT_FACTOR*sumOfTransition + r_s   # Get the final value and add it to the dictionary
    return newValDict

def checkPolicyConvergence(gm, prevPolDict, newPolDict):
    converged = True    # Set a boolean as the response

    # For every location in the map that isn't occupied
    for y in range(0, gm.cols):
        for x in range(0, gm.rows):
            if gm.occupancy_grid[x][y] == False:
                if prevPolDict.get((x,y)) != newPolDict.get((x,y)):
                    converged = False
    return converged