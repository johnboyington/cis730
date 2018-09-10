import numpy as np
import sys


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

        # remove comment lines and empty lines
        lines = [x for x in lines if '|' not in x and x != '']

        # grab metadata and trim list
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
        if '#' in lines[0]:
            self.kind = lines[0][1:]
            lines = lines[1:]

        # grab data and heuristic vector
        data = lines[:self.N]
        self.h = np.array(lines[-self.N:]).astype(int)
        self.cost = np.ones((self.N, self.N)) * -1
        if self.kind == 'list':
            self.parse_list(data)
        elif self.kind == 'matrix':
            self.parse_matrix(data)
        return

    def parse_list(self, data):
        for i, row in enumerate(data):
            row = row.split('-')
            for val in row:
                if '!' in val:
                    break
                else:
                    val = val.split('.')
                    j, cost = int(val[0]), int(val[1])
                    self.cost[i, j] = cost
        return

    def parse_matrix(self, data):
        for i, row in enumerate(data):
            row = row.split(' ')
            for j, val in enumerate(row):
                if val == '*':
                    pass
                else:
                    val = int(val)
                    self.cost[i, j] = val
        return

    def print_list(self):
        s = ''
        for i, row in enumerate(self.cost):
            for j, val in enumerate(row):
                if val == -1:
                    pass
                else:
                    s += str(int(j)) + '.' + str(int(val)) + ' - '
            s += '!\n'
        print(s)
        return

    def print_matrix(self):
        s = ''
        for i, row in enumerate(self.cost):
            for j, val in enumerate(row):
                if val == -1:
                    s += '* '
                else:
                    s += str(int(val)) + ' '
            s += '\n'
        print(s)
        return

if __name__ == '__main__':
    example = AIGraph(sys.argv[1])
    example.print_list()
    example.print_matrix()
