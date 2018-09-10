import sys
import numpy as np
from ai_graph import AIGraph
from g import g


if __name__ == '__main__':
    graph = AIGraph(sys.argv[1])
    s = sys.stdin.read().replace('\n', '')
    s = s.split(' ')
    nodes = np.array(s).astype(int)
    print(g(graph, nodes))
