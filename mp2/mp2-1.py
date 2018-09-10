import sys
from ai_graph import AIGraph


if __name__ == '__main__':
    example = AIGraph(sys.argv[1])
    example.print_list()
    example.print_matrix()
