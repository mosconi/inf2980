import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from permutation import permutation

class test_permutation(unittest.TestCase):
    sz = 3

    def SetUp(self):
        pass

    def test_identity_3(self):
        id=permutation(self.sz,complete=True)
        self.assertTrue(all(id[i] == i for i in range(self.sz)))

    def test_new_from_list(self):
        perm_list = [ 0, 1 ]
        perm = permutation(self.sz,perm_list)
        self.assertEqual(perm[0],1)
        self.assertEqual(perm[1],0)
        self.assertTrue(all(perm[i] == i for i in range(2,self.sz)))

    def test_permutate_list(self):
        perm_list = [ 0, 1 ]
        perm = permutation(self.sz,perm_list)
        a = [ i for i in range(self.sz) ]
        b = perm(a)
        self.assertEqual(b[0],1)
        self.assertEqual(b[1],0)
        self.assertTrue(all(b[i] == i for i in range(self.sz)))

if __name__ == '__main__':
    unittest.main()
