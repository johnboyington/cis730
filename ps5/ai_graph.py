import numpy as np
import pickle


class AIGraph(object):
    '''A class that stores information on an AIGraph given an input filename.
    Also has the ability to pickle the cost matrix for use in other classes,
    and can print different aig formatted outputs.'''
    def __init__(self, filename):
        self.filename = filename
        self.parse_input()

    def parse_input(self):
        '''Parses the input of an aig file.'''
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
        '''Parses data if in the #list format'''
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
        '''Parses data if in the #matrix format'''
        for i, row in enumerate(data):
            row = row.split()
            for j, val in enumerate(row):
                if val == '*':
                    pass
                else:
                    val = int(val)
                    self.cost[i, j] = val
        return

    def print_list(self):
        '''Prints data if in the list format'''
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
        '''Prints data if in the matrix format'''
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

    def store_table(self):
        '''Pickles lookup table data'''
        self.lookup_table = {}
        for i, row in enumerate(self.cost):
            self.lookup_table[i] = []
            for j, c in enumerate(row):
                if c != -1:
                    self.lookup_table[i].append((j, c))
        pickle.dump(self.lookup_table, open(self.filename[:-4] + '.p', 'wb'))

    def store_h(self):
        '''Stores heuristic data.'''
        np.save('h.npy', self.h)
        return
