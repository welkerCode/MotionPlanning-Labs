
# For Part 1:
_LIST_SWITCH = True         # True returns list of resulting states and probabilities, False returns random state based on prob
                            # ...keep 'False' for part1 (mdpMain.py) and 'True' for part2 (valueIterMain.py)

_ACTION_TYPE = 'else'   # 'lateral' for lateral movements only (parts 1.1 and 1.2)
                            # 'diagonal' to include diagonal movements (part 1.3)
                            # 'else' to include both lateral and diagonal movements (part 1.4)

_COMPLETION_PROB = .8       # This is the probability of a successful movement
_GOAL_REWARD = 10           #
_CORNER_REWARD = -1
_OTHER_STATE_REWARD = -1
_DISCOUNT_FACTOR = 0.8      # Lambda (discount factor)
_NUM_ITER = 10
_EPSILON = .001