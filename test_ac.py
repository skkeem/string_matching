import unittest
import ac

class TestAC(unittest.TestCase):
    p1 = ["he", "she", "his", "hers"]
    p2 = ["cacbaa", "acb", "aba", "acbab", "ccbab"]
    a1 = ac.AC(p1)
    a2 = ac.AC(p2)

    def test_m(self):
        self.assertEqual(self.a1.m, 13)
        self.assertEqual(self.a2.m, 23)

    def test_ff(self):
        self.assertEqual(self.a1.ff, [0,0,0,0,1,2,0,3,0,3,0,0,0])
        self.assertEqual(self.a2.ff, [0,0,7,8,9,12,7,0,1,0,0,7,7,10,1,0,7,10,0,0,0,0,0])

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

    def test_search(self):
        ii = [3, 5]
        ss = [set(["she", "he"]), set(["hers"])]
        k = 0
        for i,s in self.a1.search("ushers"):
            self.assertEqual(i, ii[k])
            self.assertEqual(s, ss[k])
            k = k + 1

if __name__ == '__main__':
    unittest.main()
