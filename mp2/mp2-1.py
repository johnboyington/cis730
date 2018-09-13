import sys
from ai_graph import AIGraph


# read in aig file and call the associated print functions for output display
example = AIGraph(sys.argv[1])
example.print_list()
example.print_matrix()
