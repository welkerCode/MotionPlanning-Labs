import numpy as np

# This function runs the valueIteration on the specified map
def policyIter(gm):
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

    if _POLICY_INIT == 'direction':
        initPolicyDict = initDirPolicy(gm, _POLICY_INIT_DIR)
    else:
        initPolicyDict = initRandomPolicy(gm)

    prevPolicyDict = initPolicyDict
    prevValueDict = initValueTable(gm)
    newPolicyDict = {}
    newValueDict = {}


    convergence = False
    iterationCount = 0

    # while converge is false
        # Increment iteration counter
        # Perform policy evaluation
            # Compute value function when following policy
        # Perform policy improvement
            # Find new optimal policy using the values computed
        # Check convergence
        # Update dictionaries

    # Print final policy and value maps


def initDirPolicy(gridMap, initialDirection):
    # For every state in the gridmap that isn't occupied
        # Set the action to the initialDirection in the initial policy dictionary
    # Return the dictionary

def initRandomPolicy(gridMap):

    # For every state in the gridmap that isn't occupied
        # Generate a random value
        # Define the action
        # Add it to the dictionary
    # Return the initial policy dictionary

def computeValue():

def updatePolicy():
    

