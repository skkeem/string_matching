import unittest
import bb

class TestBB(unittest.TestCase):
    p = ["aabba", "aaabb", "ababa", "aabba", "aaabb"]
    b = bb.BB(p)
    t = ["aabbaaabba", "aaabbaaabb", "ababaababa", "aabbaaabba", "aaabbaaabb", "baaabbabab", "aababaabba", "aaabbaaabb", "baaabbaaab", "aaaaaaaaaa"]

    def test_dr(self):
        self.assertEqual(self.b.dr["aabba"], 1)
        self.assertEqual(self.b.dr["aaabb"], 2)
        self.assertEqual(self.b.dr["ababa"], 3)
    def test_pp(self):
        self.assertEqual(self.b.pp, [1,2,3,1,2])

    def test_ac(self):
        ac = self.b.ac
        pass

    def test_search(self):
        self.assertEqual([p for p in self.b.search(self.t)], [(4,4), (4,9), (8,5)])

if __name__ == '__main__':
    unittest.main()
