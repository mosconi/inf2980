import unittest
import test_permutation

def my_module_suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_permutation)
    return suite
