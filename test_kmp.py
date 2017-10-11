import unittest
import kmp

class TestKMP(unittest.TestCase):
    k1 = kmp.KMP("ababaca")
    k2 = kmp.KMP("aabbaab")
    k3 = kmp.KMP("aab")
    k4 = kmp.KMP([1,2,3,1])

    def test_p(self):
        self.assertEqual(''.join(self.k1.p), "ababaca")
        self.assertEqual(''.join(self.k2.p), "aabbaab")

    def test_ff_construction(self):
        self.assertEqual(self.k1.ff, [0,0,1,2,3,0,1])
        self.assertEqual(self.k2.ff, [0,1,0,0,1,2,3])

    def test_search(self):
        a = [0, 4]
        k = 0
        for i in self.k2.search("aabbaa"):
            raise Exception
        for i in self.k3.search("aabbaab"):
            self.assertEqual(i, a[k])
            k = k+1

    def test_stream(self):
        c = self.k4.stream()
        next(c)
        self.assertEqual(c.send(0), False)
        self.assertEqual(c.send(1), False)
        self.assertEqual(c.send(2), False)
        self.assertEqual(c.send(1), False)
        self.assertEqual(c.send(2), False)
        self.assertEqual(c.send(3), False)
        self.assertEqual(c.send(1), True)
        self.assertEqual(c.send(2), False)
        self.assertEqual(c.send(3), False)
        self.assertEqual(c.send(1), True)

if __name__ == '__main__':
    unittest.main()
