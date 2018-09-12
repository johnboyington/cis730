import sys
from utils import branch_and_bound
from ai_graph import AIGraph

graph = AIGraph(sys.argv[1])
sol = branch_and_bound(graph)
print(sol)