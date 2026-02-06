import cv2
import numpy as np
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def process_images():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Base pipeline – no filters applied yet.")

if __name__ == "__main__":
    process_images()