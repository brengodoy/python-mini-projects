import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import calculate_tip

def test_calculate_tip():
    assert calculate_tip(80,10,2) == (8.0,44.0)
    assert calculate_tip(100,20,3) == (20.0,40.0)
    assert calculate_tip(99.99, 15, 3) == (14.9985, (99.99 + 14.9985)/3)
    assert calculate_tip(100, 0, 2) == (0.0, 50.0)
    assert calculate_tip(50, 10, 1) == (5.0, 55.0)
    assert calculate_tip(10000, 30, 5) == (3000.0, 2600.0)
    assert calculate_tip(123.45, 18, 4) == (22.221,36.41775)