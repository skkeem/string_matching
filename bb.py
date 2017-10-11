#!/usr/bin/python3

from ac import AC

class BB:
    """Class for Baker-Bird algorithm"""
    def __init__(self, p):
        # p : m by m sized pattern.
        self.p = list(p)
        self.m = len(p)
        # ac : Aho-Corasick instance for p
        ac = AC(p)
        # dr : pi[1..m] -> distinct row number.
        # pp : p converted in to sequence of distinct row #s.
        self.dr, self.pp = self.construct()
        # R : distinct row #[1..n, 1..n] for match.
        # !!this is constructed row by row to reduce space usage.

    def construct(self):
        dr = {}
        pp = []
        row_num = 1
        for pi in self.p:
            if not pi in dr:
                dr[pi] = row_num
                row_num = row_num + 1
            pp.append(dr[pi])
        return (dr, pp)

    def search(self, t):
        n = len(t)
        assert (m <= n)

        ac = self.ac
        for i in range(n):
            # r : current row of R matrix
            r = [0 for i in range(n)]
            # ac returns (index, output)
            for j, s in ac.search(t[i]):
                r[j] = dr[s.pop()]

    def printAll(self, t):
        for i in self.search(t):
            print(i)
