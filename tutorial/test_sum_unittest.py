# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 16:42:09 2021

@author: pierr
"""

import unittest


class TestSum(unittest.TestCase) :
    
    def test_sum(self):
        self.assertEqual(sum([1,2,3]),6,"Should be 6")
        
    def test_sum_tuple(self):
        self.assertEqual(sum((1,2,2)),5, "should be 6 !")
        
if __name__=='__main__':
    unittest.main()