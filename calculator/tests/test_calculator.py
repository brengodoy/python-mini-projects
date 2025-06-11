import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import addition, subtraction, multiply, division

def test_addition():
    assert addition(1,1) == 2
    assert addition(1,-1) == 0

def test_subtraction():
    assert subtraction(2,1) == 1
    assert subtraction(1,1) == 0
    
def test_multiply():
    assert multiply(1,2) == 2
    assert multiply(3,3) == 9
    
def test_division():
    assert division(5,2) == 2.5
    assert division(3,3) == 1