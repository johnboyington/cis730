import sys
import numpy as np
from ai_graph import AIGraph
from code import multi_g


# create aigraph
graph = AIGraph(sys.argv[1])

# convert stdin to np.array for use in g(), and output result
s = sys.stdin.read().replace('\n', '')
s = s.split(' ')
nodes = np.array(s).astype(int)
print(multi_g(graph, nodes))
