from graph_search import *
from mdp import *

gm = GridMap("map0.txt")
results = getTransition(False, gm.goals[0], 'd', .8)

print(results)