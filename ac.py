#!/usr/bin/python3

from functools import reduce

class AC:
    """Class for Aho-Corasick module"""
    def __init__(self, p):
        # k : number of patterns
        self.k = len(p)
        # p : list of pattern strings with total length m
        self.p = list(p)
        self.m = sum(len(x) for x in p)
        # alphabet : unique alphabets in p
        self.alphabet = list(reduce(lambda x, y : x | y, [set(x) for x in p]))
        # tree : just for bookkeeping. (depth = length of prefix-suffix)
        # ff : state#, char -> state# for some pattern that is the suffix of current state#
        # of : state# -> matched patterns' numbers
        self,tree, self.ff, self.of = self.construct()

    def construct(self):
        p = self.p
        max_d = max(len(x) for x in p)

        p = self.p
        m = len(p)
        ff = [0 for i in range(0, m)]
        # k : guessed length of prefix-suffix except p[q]
        k = 0
        # recursive structure for ff
        ## case 1 : p[k] == p[q]
        ##  ff[q] = k + 1
        ## case 2 : p[k] != p[q]
        ##  fallback with k = ff[k-1]
        ## starts with ff[q-1], ends with k == 0
        #  p[0..q]
        for q in range(1, m):
            # fall back until p[k] == p[q].
            # or k == 0.
            while k > 0 and p[k] != p[q]:
                k = ff[k-1]
            # p[k] == p[q], thus next k = k+1.
            # or k == 0.
            if k > 0 or p[k] == p[q]:
                k = k + 1
            ff[q] = k
        return ff

    def search(self, t):
        p = self.p
        ff = self.ff
        n = len(t)
        m = len(p)
        # q : length of match
        q = 0
        for i in range(0, n):
            # fall back until p[q] == t[i].
            # or q == 0.
            while q > 0 and p[q] != t[i]:
                q = ff[q-1]
            # p[q] == t[i], thus next q = q+1.
            # or q == 0.
            if q > 0 or p[q] == t[i]:
                q = q + 1
            if q == m:
                yield (i-m+1, [])
                q = ff[q-1]

    def printAll(self, t):
        for i in self.search(t):
            print(i)
