import cv2
import numpy as np
import os

# Resolve paths relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

def process_images():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith((".jpg", ".png", ".jpeg")):
            img_path = os.path.join(INPUT_DIR, file)
            img = cv2.imread(img_path)

            if img is None:
                continue

            name = os.path.splitext(file)[0]

            # Filter 1: Color Reduction
            data = img.reshape((-1, 3)).astype(np.float32)
            _, labels, centers = cv2.kmeans(
                data,
                6,
                None,
                (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
                10,
                cv2.KMEANS_RANDOM_CENTERS
            )

            reduced = centers[labels.flatten()].reshape(img.shape).astype(np.uint8)
            cv2.imwrite(
                os.path.join(OUTPUT_DIR, f"{name}_color_reduction.png"),
                reduced
            )

            # Filter 2: Contrast Enhancement 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            enhanced = cv2.equalizeHist(gray)
            cv2.imwrite(
                os.path.join(OUTPUT_DIR, f"{name}_contrast.png"),
                enhanced
            )

            print(f"Processed: {file}")

if __name__ == "__main__":
    process_images()
