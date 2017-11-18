# Start using in Part 1 (Markov Decision Process)
_LIST_SWITCH = True         # True returns list of resulting states and probabilities, False returns random state based on prob
                            # ...keep 'False' for part1 (mdpMain.py) and 'True' for part2 (valueIterMain.py) and part3 (policyIterMain.py)

_ACTION_TYPE = 'lateral'    # 'lateral' for lateral movements only (parts 1.1 and 1.2)
                            # 'diagonal' to include diagonal movements (part 1.3)
                            # 'else' for part 1.4 (forces .7, .1, .05 probabilities for 5 possible actions)

_COMPLETION_PROB = .8       # This is the probability of a successful movement

# Start using in Part 2 (Value Iteration)
_GOAL_REWARD = 10           # This is the reward for reaching the goal
_CORNER_REWARD = 0          # This is the reward for each corner state (that isn't a goal)
_OTHER_STATE_REWARD = 0     # This is the reward for each state that isn't a goal, or a corner
_DISCOUNT_FACTOR = 0.8      # Discount factor (lambda)
_EPSILON = .001             # Determines the limit of convergence.  Set to .001 for my report.

# Start using in Part 3 (Policy Iteration)
_POLICY_INIT = 'random'  # If 'direction', initial policy will be all one direction, if 'random', then random
_POLICY_INIT_DIR = 'd'      # Use 'u' for 3.1 and 'd' for 3.2 (just like how the actions are defined in these labs)

# Misc Parameters
_TEXT_SIZE = 8             # This changes the size of the text that pops up in the values tables