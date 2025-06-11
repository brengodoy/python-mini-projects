import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import add_task, update_status, search_item, remove_task, tasks

@pytest.fixture(autouse=True)
def setup_function():
    tasks.clear()
    tasks.extend([
        {"name": "Sacar al perro", "done": False},
        {"name": "Ir al super", "done": False},
        {"name": "Entrenar", "done": True},
        {"name": "Estudiar", "done": False}
    ])

def test_add_task():
    add_task("Ordenar la pieza")
    assert tasks[-1] ==	{"name": "Ordenar la pieza","done": False}
    
def test_update_status():
    update_status(0)
    assert tasks[0]["done"] == True
    
def test_search_item():
    assert search_item("Entrenar") == 2
    
def test_remove_task():
    remove_task(0)
    assert tasks == [
 	{"name": "Ir al super","done": False},
	{"name": "Entrenar","done": True},
	{"name": "Estudiar","done": False},
]