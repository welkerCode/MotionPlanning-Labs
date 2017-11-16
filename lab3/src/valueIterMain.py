from graph_search import *
from graph_search import _ACTIONS
from graph_search import _ACTIONS_2
from mdp import *
from param import _LIST_SWITCH
from param import _ACTION_TYPE
from param import _COMPLETION_PROB
from valueIter import *

# Create a gridmap object for each map
gm0 = GridMap("map0.txt")
gm1 = GridMap("map1.txt")
gm2 = GridMap("map2.txt")

#prevIterTable = initTable(gm0)          # Fill the prevIteration Dictionary with the initial reward values
#gm0.display_ValueIterMap(prevIterTable)

valueIter(gm1)