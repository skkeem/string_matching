#!/usr/bin/python3

from ac import AC
from kmp import KMP

class BB:
    """Class for Baker-Bird algorithm"""
    def __init__(self, p):
        # p : m by m sized pattern.
        self.p = list(p)
        self.m = len(p)
        # dr : pi[1..m] -> distinct row number.
        # pp : p converted in to sequence of distinct row #s.
        self.dr, self.pp = self.construct()
        # ac : Aho-Corasick instance for p (row-matching)
        self.ac = AC(self.dr.keys())
        # kmp : KMP instance for pp (column-matching)
        self.kmp = KMP(self.pp)
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
        assert (self.m <= n)

        ac = self.ac
        kmp = self.kmp
        dr = self.dr
        nkmp = [kmp.stream() for i in range(n)]
        for k in nkmp:
            next(k)
        for i in range(n):
            # r : current row of R matrix.
            r = [0 for x in range(n)]
            # ac returns (index, output).
            for j, s in ac.search(t[i]):
                r[j] = dr[(list(s)[0])]
            # single step n KMPs.
            for j in range(n):
                if nkmp[j].send(r[j]):
                    yield (i, j)

    def printAll(self, t):
        for p in self.search(t):
            print(p)
