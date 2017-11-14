from graph_search import *
from graph_search import _ACTIONS
from graph_search import _ACTIONS_2
from mdp import *
from param import _LIST_SWITCH
from param import _ACTION_TYPE
from param import _COMPLETION_PROB

# Create a gridmap object for each map
gm0 = GridMap("map0.txt")
gm1 = GridMap("map1.txt")
gm2 = GridMap("map2.txt")

# Run a BFS on each map
if _ACTION_TYPE == 'lateral':
    plan0 = bfs_search_map(gm0.init_pos, gm0.transition, gm0.is_goal, _ACTIONS)
    plan1 = bfs_search_map(gm1.init_pos, gm1.transition, gm1.is_goal, _ACTIONS)
    plan2 = bfs_search_map(gm2.init_pos, gm2.transition, gm2.is_goal, _ACTIONS)
else:
    plan0 = bfs_search_map(gm0.init_pos, gm0.transition, gm0.is_goal, _ACTIONS_2)
    plan1 = bfs_search_map(gm1.init_pos, gm1.transition, gm1.is_goal, _ACTIONS_2)
    plan2 = bfs_search_map(gm2.init_pos, gm2.transition, gm2.is_goal, _ACTIONS_2)

print("--------------------")
print("Map0:\n")
# Run plan0 through the mdp
for iter in range(0,5):
    nextState0 = gm0.init_pos
    for action in plan0[0][1]:
        nextState0 = getTransition(_LIST_SWITCH, _ACTION_TYPE, nextState0, gm0.transition, action, _COMPLETION_PROB)
    print(nextState0)

print("--------------------")
print("Map1:\n")

# Run plan1 through the mdp
for iter in range(0,5):
    nextState1 = gm1.init_pos
    for action in plan1[0][1]:
        nextState1 = getTransition(_LIST_SWITCH, _ACTION_TYPE, nextState1, gm1.transition, action, _COMPLETION_PROB)
    print(nextState1)

if plan2:
    print("--------------------")
    print("Map2:\n")

    # Run plan1 through the mdp
    for iter in range(0,5):
        nextState2 = gm2.init_pos
        for action in plan2[0][1]:
            nextState2 = getTransition(_LIST_SWITCH, _ACTION_TYPE, nextState2, gm2.transition, action, _COMPLETION_PROB)
        print(nextState2)

