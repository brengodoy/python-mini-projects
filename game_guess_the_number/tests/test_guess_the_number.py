import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import verify_correct_number

def test_verify_correct_number():
    assert verify_correct_number(1,1) is True
    assert verify_correct_number(1,3) is False