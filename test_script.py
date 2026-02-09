import os

def test_folders_exist():
    # This test checks if the required folders are there
    assert os.path.exists("input")
    assert os.path.exists("output")