# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 16:31:04 2021

@author: pierr
"""

def test_sum() :
    assert sum([1,2,3])==6, "should be 6"
    
def test_sum_tuple():
    assert sum((1,2,2))==6, "should be 6 !"

if __name__=="__main__" :
    test_sum()
    test_sum_tuple()
    print("everything passed")