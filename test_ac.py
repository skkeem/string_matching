import unittest
import ac

class TestAC(unittest.TestCase):
    p1 = ["he", "she", "his", "hers"]
    p2 = ["cacbaa", "acb", "aba", "acbab", "ccbab"]
    a1 = ac.AC(p1)
    a2 = ac.AC(p2)
    p = ["ababa", "aabba", "aaabb"]
    a = ac.AC(p)

    def test_m(self):
        self.assertEqual(self.a1.m, 13)
        self.assertEqual(self.a2.m, 23)
        self.assertEqual(self.a.m, 16)

    def test_ff(self):
        self.assertEqual(self.a1.ff, [0,0,0,0,1,2,0,3,0,3,0,0,0])
        self.assertEqual(self.a2.ff, [0,0,7,8,9,12,7,0,1,0,0,7,7,10,1,0,7,10,0,0,0,0,0])
        self.assertEqual(self.a.ff, [0,0,0,1,2,3,1,2,0,1,6,7,8,0,0,0])

    def test_of(self):
        self.assertEqual(self.a1.of[2], set(["he"]))
        self.assertEqual(self.a1.of[5], set(["she", "he"]))
        self.assertEqual(self.a1.of[7], set(["his"]))
        self.assertEqual(self.a1.of[9], set(["hers"]))

        self.assertEqual(self.a2.of[6], set(["cacbaa"]))
        self.assertEqual(self.a2.of[9], set(["acb"]))
        self.assertEqual(self.a2.of[11], set(["aba"]))
        self.assertEqual(self.a2.of[13], set(["acbab"]))
        self.assertEqual(self.a2.of[17], set(["ccbab"]))

        self.assertEqual(self.a.of[5], set(["ababa"]))
        self.assertEqual(self.a.of[9], set(["aabba"]))
        self.assertEqual(self.a.of[12], set(["aaabb"]))

    def test_search(self):
        ans = [(3, set(["she", "he"])), (5, set(["hers"]))]
        self.assertEqual([p for p in self.a1.search("ushers")], ans)

        ans1 = [(4, set(["aabba"])), (8, set(["aaabb"])), (9, set(["aabba"]))]
        ans2 = [(4, set(["aaabb"])), (5, set(["aabba"])), (9, set(["aaabb"]))]
        ans3 = [(4, set(["ababa"])), (9, set(["ababa"]))]
        ans4 = [(4, set(["aabba"])), (8, set(["aaabb"])), (9, set(["aabba"]))]
        ans5 = [(4, set(["aaabb"])), (5, set(["aabba"])), (9, set(["aaabb"]))]
        ans6 = [(5, set(["aaabb"])), (6, set(["aabba"]))]
        ans7 = [(5, set(["ababa"])), (9, set(["aabba"]))]
        ans8 = [(4, set(["aaabb"])), (5, set(["aabba"])), (9, set(["aaabb"]))]
        ans9 = [(5, set(["aaabb"])), (6, set(["aabba"]))]
        self.assertEqual([p for p in self.a.search("aabbaaabba")], ans1)
        self.assertEqual([p for p in self.a.search("aaabbaaabb")], ans2)
        self.assertEqual([p for p in self.a.search("ababaababa")], ans3)
        self.assertEqual([p for p in self.a.search("aabbaaabba")], ans4)
        self.assertEqual([p for p in self.a.search("aaabbaaabb")], ans5)
        self.assertEqual([p for p in self.a.search("baaabbabab")], ans6)
        self.assertEqual([p for p in self.a.search("aababaabba")], ans7)
        self.assertEqual([p for p in self.a.search("aaabbaaabb")], ans8)
        self.assertEqual([p for p in self.a.search("baaabbaaab")], ans9)

if __name__ == '__main__':
    unittest.main()
