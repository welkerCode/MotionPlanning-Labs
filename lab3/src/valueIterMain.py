from graph_search import *
from graph_search import _ACTIONS
from graph_search import _ACTIONS_2
from mdp import *

# Create a gridmap object for each map
gm0 = GridMap("map0.txt")
gm1 = GridMap("map1.txt")
gm2 = GridMap("map2.txt")

results = getTransition(False, True, gm0.goals[0], 'd', .8)

# Run a BFS on each map
plan0 = bfs_search_map(gm0.init_pos, gm0.transition, gm0.is_goal, _ACTIONS_2)
plan1 = bfs_search_map(gm1.init_pos, gm1.transition, gm1.is_goal, _ACTIONS_2)
plan2 = bfs_search_map(gm2.init_pos, gm2.transition, gm2.is_goal, _ACTIONS_2)

modelSwitch = False
lateralAction = False
completionProb = .7
print("--------------------")
# Run plan0 through the mdp
for iter in range(0,5):
    nextState0 = gm0.init_pos
    for action in plan0[0][1]:
        nextState0 = getTransition2(False, 'else', nextState0, action, completionProb)
    print(nextState0)

print("--------------------")

# Run plan1 through the mdp
for iter in range(0,5):
    nextState1 = gm1.init_pos
    for action in plan1[0][1]:
        nextState1 = getTransition2(False, 'else', nextState1, action, completionProb)
    print(nextState1)

print("--------------------")

# Run plan1 through the mdp
for iter in range(0,5):
    nextState2 = gm2.init_pos
    for action in plan2[0][1]:
        nextState2 = getTransition2(False, 'else', nextState2, action, completionProb)
    print(nextState2)

