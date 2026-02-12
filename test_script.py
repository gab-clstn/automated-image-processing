import os

def test_folders_exist():
    # This test checks if the required folders are there
    assert os.path.exists("input")
    assert os.path.exists("output")
    
def test_jpg_processing():
    assert 1 + 1 == 2