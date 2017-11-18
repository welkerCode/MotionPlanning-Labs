from graph_search import *
from policyIter import *

# Create a gridmap object for each map
gm0 = GridMap("map0.txt")
gm1 = GridMap("map1.txt")
gm2 = GridMap("map2.txt")

#prevIterTable = initTable(gm0)          # Fill the prevIteration Dictionary with the initial reward values
#gm0.display_ValueIterMap(prevIterTable)

policyIter(gm0)