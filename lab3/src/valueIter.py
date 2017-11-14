def calcStateVal(lambda, transitionModel):
    '''
    for every possible new state
        find the probability of going to that state
        find the reward of going to that state (0 if not goal)
        Add the product to the sum
    multiply that sum by lambda
    store that value...somewhere that can be read from again
    table of states?


    :param transitionModel:
    :return:
    '''

stateVal = {}

