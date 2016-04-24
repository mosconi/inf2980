import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from permutation import permutation

class test_permutation(unittest.TestCase):
    sz = 4

    def SetUp(self):
        pass

    def test_00_identity(self):
        id=permutation(self.sz,complete=True)
        self.assertTrue(all(id[i] == i for i in range(self.sz)))

    def test_10_new_from_list(self):
        perm_list = [ 0, 1 ]
        perm = permutation(self.sz,perm_list)
        self.assertEqual(perm[0],1)
        self.assertEqual(perm[1],0)
        self.assertTrue(all(perm[i] == i for i in range(2,self.sz)))

    def test_30_permutate_list(self):
        perm_list = [ 0, 1 ]
        perm = permutation(self.sz,perm_list)
        a = [ i for i in range(self.sz) ]
        b = perm(a)
        self.assertEqual(b[0],1)
        self.assertEqual(b[1],0)
        self.assertTrue(all(b[i] == i for i in range(2,self.sz)))

    def test_20_new_from_dict_1(self):
        perm_dict = { 0:1, 1:0,}
        perm = permutation(self.sz,perm_dict)
        self.assertEqual(perm[0],1)
        self.assertEqual(perm[1],0)
        self.assertTrue(all(perm[i] == i for i in range(2,self.sz)))

    def test_20_new_from_dict_2(self):
        perm_dict = { 0:1, 1:0,2:3, 3:2}
        perm = permutation(self.sz,perm_dict)
        self.assertEqual(perm[0],1)
        self.assertEqual(perm[1],0)
        self.assertEqual(perm[2],3)
        self.assertEqual(perm[3],2)
        self.assertTrue(all(perm[i] == i for i in range(4,self.sz)))



    def test_40_permutate_dict_2(self):
        perm_ = {0:1, 1:0, 2:3, 3:2}
        perm = permutation(self.sz,perm_)
        a = ['a', 'b', 'c', 'd'] 
        b = perm(a)
        self.assertEqual(b[0],'b')
        self.assertEqual(b[1],'a')
        self.assertEqual(b[2],'d')
        self.assertEqual(b[3],'c')

    def test_50_permutate_permutation(self):
        perm_list = [ 0, 1 ]
        id = permutation(self.sz)
        perm1 = permutation(self.sz,perm_list)
        a = perm1(perm1)
        self.assertEqual(a, id)

    def test_50_permutate_permutation2(self):
        id = permutation(self.sz)
        perm_list = [ 0, 1 ]
        perm1 = permutation(self.sz,perm_list)

        perm_list = [ 1, 2 ]
        perm2 = permutation(self.sz,perm_list)

        perm_list = [ 0 ,2 , 1]
        perm3 = permutation(self.sz,perm_list)

        perm_list = [ 0, 1, 2 ]
        perm4 = permutation(self.sz,perm_list,complete=True)

        a = perm1(perm2)
        self.assertEqual(a, perm3)

        b = perm2(perm1)
        self.assertEqual(b, perm4)

    def test_50_permutate_permutation3(self):
        id = permutation(self.sz)
        perm_d = {0:1,1:0,2:3,3:2}
        perm = permutation(self.sz,perm_d)

        perm_list = [ 0, 1 ]
        perm1 = permutation(self.sz,perm_list)

        perm_list = [ 2 , 3]
        perm2 = permutation(self.sz,perm_list)

        a = perm1(perm2)
        a = perm1(perm2)

        self.assertEqual(a, perm)

        b = perm2(perm1)
        self.assertEqual(b, perm)

        self.assertEqual(a,b)


    def test_15_new_form_list(self):
        """ por definicao, (1 2 3) == (2 3 1) == (3 1 2)"""

        a=permutation(self.sz, [1, 2, 3])
        b=permutation(self.sz, [2, 3, 1])
        c=permutation(self.sz, [3, 1, 2])

        self.assertEqual(a,b)
        self.assertEqual(b,c)
        self.assertEqual(a,c) # redundante, por transitividade



    def test_80_expand(self):
        id = permutation(self.sz)
        id.expand()
        for i in range(id.maxsize):
            self.assertTrue(id.permutation.has_key(i),msg='{} should be present '.format(i))
            self.assertEqual(id.permutation[i],i)


    def test_80_collapse(self):
        id = permutation(self.sz,complete=True)
        id.collapse()
        for i in range(id.maxsize):
            self.assertFalse(id.permutation.has_key(i),msg='{} should not be present '.format(i))

    def test_90_exception_list_size_1(self):
        perm_list = [ 0, 1 ]
        perm = permutation(self.sz,perm_list)
        a = [ i for i in range(self.sz-1) ]
        with self.assertRaises(Exception):
            perm(a)

    def test_90_exception_list_size_2(self):
        perm_list = [ 0, 1 ]
        perm = permutation(self.sz,perm_list)
        a = [ i for i in range(self.sz+1) ]
        with self.assertRaises(Exception):
            perm(a)
        
        

if __name__ == '__main__':
    unittest.main()
