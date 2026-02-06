import cv2
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

def process_images():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith((".jpg", ".png", ".jpeg")):
            img = cv2.imread(os.path.join(INPUT_DIR, file))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            enhanced = cv2.equalizeHist(gray)

            cv2.imwrite(
                os.path.join(
                    OUTPUT_DIR,
                    f"{os.path.splitext(file)[0]}_contrast.png"
                ),
                enhanced
            )

if __name__ == "__main__":
    process_images()
