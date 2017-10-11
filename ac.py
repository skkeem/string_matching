#!/usr/bin/python3

from functools import reduce
from collections import deque

class AC:
    """Class for Aho-Corasick algorithm"""
    def __init__(self, p):
        # p : list of pattern strings with total length m
        self.p = list(p)
        self.m = sum(len(x) for x in p)+1
        # tree : just for bookkeeping. (depth = length of prefix-suffix)
        # ff : state#, char -> state# for some pattern that is the suffix of current state#
        # of : state# -> matched patterns' numbers
        self.tree, self.ff, self.of = self.construct()

    def construct(self):
        tree = [[-1 for j in range(26)] for i in range(self.m)]
        ff = [0 for i in range(self.m)]
        of = [set() for i in range(self.m)]
        # tree construction
        #  implemented in array
        new_state = 1
        curr_state = 0
        for pi in self.p:
            curr_state = 0
            for c in pi:
                next_state = tree[curr_state][ord(c)-ord('a')]
                if next_state == -1:
                    tree[curr_state][ord(c)-ord('a')] = new_state 
                    next_state = new_state
                    new_state = new_state + 1
                curr_state = next_state
            of[curr_state] = set([pi])

        # failure function construction
        #  recursive on depth of tree
        ## base case : depth(s) <= 1. ff[s] = 0
        ## inductive case : ff[s] = ff[r]
        ##                  for some r s.t. r'-c->r, s'-c->s, ff*[s'] = r'
        ## BFS
        ## queue of depth * curr_state * char *prev_state
        que = deque([(0, 0, 0, 0)])
        while len(que) > 0:
            depth, curr, char, prev = que.popleft()
            # BFS explore
            for c in range(26):
                succ = tree[curr][c]
                if succ != -1:
                    que.append((depth+1, succ, c, curr))
            # inductive case
            if depth > 1:
                # rr is r' : state#.
                rr = ff[prev]
                # fall back until r'-c->r, s'-c->s, ff*[s'] = r'
                # or r' == 0.
                while rr > 0 and tree[rr][char] == -1:
                    rr = ff[rr]
                r = tree[rr][char]
                if r == -1:
                    r = 0
                ff[curr] = r
                of[curr] = of[curr] | of[r]
        return (tree, ff, of)

    def search(self, t):
        tree = self.tree
        ff = self.ff
        of = self.of
        n = len(t)
        # s : current state#
        s = 0
        i = 0
        while i < n:
            ss = tree[s][ord(t[i])-ord('a')]
            if ss != -1:
                s = ss
                if len(of[s]) != 0:
                    yield i, of[s]
                i = i + 1
            else:
                if s == 0:
                    i = i + 1
                else:
                    s = ff[s]

    def printAll(self, t):
        for i in self.search(t):
            print(i)
