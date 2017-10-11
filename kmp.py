#!/usr/bin/python3

class KMP:
    """Class for KMP algorithm"""
    def __init__(self, p):
        # p : string with length m
        self.p = list(p)
        self.m = len(p)
        # ff : p[0..i] -> length of prefix-suffix
        self.ff = self.construct()

    def construct(self):
        p = self.p
        m = self.m
        ff = [0 for i in range(m)]
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
        m = self.m
        n = len(t)
        # q : length of match
        q = 0
        for i in range(n):
            # fall back until p[q] == t[i].
            # or q == 0.
            while q > 0 and p[q] != t[i]:
                q = ff[q-1]
            # p[q] == t[i], thus next q = q+1.
            # or q == 0.
            if q > 0 or p[q] == t[i]:
                q = q + 1
            if q == m:
                yield i-m+1
                q = ff[q-1]

    def stream(self):
        p = self.p
        ff = self.ff
        m = self.m

        # q : length of match
        q = 0
        # ret : yield value
        ret = None
        while True:
            # c : next input
            c = yield ret
            # fall back until p[q] == c.
            # or q == 0.
            while q > 0 and p[q] != c:
                q = ff[q-1]
            # p[q] == c, thus next q = q+1.
            # or q == 0.
            if q > 0 or p[q] == c:
                q = q + 1

            if q == m:
                ret = True
                q = ff[q-1]
            else:
                ret = False

    def printAll(self, t):
        for i in self.search(t):
            print(i)
