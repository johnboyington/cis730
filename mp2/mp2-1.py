import numpy as np


class AIGraph(object):
    '''
    A class that stores information on an AIGraph given an input filename.
    '''
    def __init__(self, filename):
        self.filename = filename
        self.parse_input()

    def parse_input(self):
        with open(self.filename, 'r') as F:
            lines = F.read().split('\n')
        self.N = int(lines[0])
        lines = lines[1:]
        if 'S' in lines[0]:
            self.S = int(lines[0][:-2])
            lines = lines[1:]
        if 'G' in lines[0]:
            self.G = int(lines[0][:-2])
            lines = lines[1:]
        if '#' not in lines[0]:
            self.J = int(lines[0])
            lines = lines[1:]
        else:
            self.kind = lines[0][1:]
            lines = lines[1:]
        if self.kind == 'list':
            self.parse_list(lines)
        elif self.kind == 'matrix':
            self.parse_matrix(lines)

    def parse_list(self, lines):
        print('doit')


if __name__ == '__main__':
    example = AIGraph('Output.aig')
