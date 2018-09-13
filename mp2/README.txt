# CIS 730 Artificial Intelligence
Fall 2018
Homework 2 of 10: Machine Problem (MP2)

The problem scripts can be used in the following way:
Problem 1: `python mp2-1.py graph.aig`
Problem 2: `python mp2-2.py graph.aig < seq.txt`
Problem 3: `python mp2-2.py graph.aig`
Problems 4 and 5: `python mp2-2.py -flag graph.aig`

where `graph.aig` is any aig v3 file, `seq.txt` is a sequence of nodes passed to standard input, and `-flag` is one of the following:
`-bnb` for branch and bound search,
`-gbfs` for greedy search and
`-a` for A* search


Notes about this repository:
Code was used from the aima-python github repository, found at: https://github.com/aimacode/aima-python
The code here is written entirely in python, and therefore requires no compilation and runtime is ~0.016ms for small graphs (N=5). Runtime will scale up with larger graphs.
