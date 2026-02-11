# Group 6 - Automated Image Processing with CI/CD Pipeline

## Overview

This program applies an automated image processing system using Python and OpenCV, combined with a Continuous Integration (CI) pipeline through GitHub Actions. The system automatically processes images, runs automated tests, and manages outputs on every GitHub update to demonstrate DevOps workflow, automation, and collaborative software development.

It shows how image processing tasks can be integrated with CI practices to ensure reliability and consistency in modern software development. This project simulates a real-world development environment where automation, collaboration, and reliability are essential.

---

## Project Objectives

- Apply image processing techniques using Python and OpenCV  
- Implement a Continuous Integration (CI) pipeline using GitHub Actions  
- Practice collaborative software development using GitHub  
- Understand DevOps workflow and automation concepts  

---

## How to Run the Program (Local Execution)

Follow these steps to run the program on your local machine:

### 1. Prerequisites

Make sure you have installed:

- Python 3.10 or higher  
- Git  
- Visual Studio Code (recommended)  

---

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add Input Images

Place the images you want to process inside the `input/` directory.

**Supported formats:**
- `.jpg`
- `.png`
- `.jpeg`

---

### 5. Push Changes to Trigger the CI Pipeline

After adding images, commit and push your changes:

```bash
git add .
git commit -m "Added new input images"
git push origin main
```

Every push or pull request to the `main` branch automatically triggers the GitHub Actions CI pipeline.

---

### 6. Pull the Generated Output

Once the pipeline finishes successfully, run:

```bash
git pull origin main
```

The processed images will automatically be saved in the `output/` directory.

---

## Image Processing Techniques (Filters Used)

The system automatically detects image files in the `input/` directory and applies the following filters:

### 1. Color Reduction
Reduces the number of colors in the image to simplify visual information and lower complexity. This is useful for stylization and preprocessing.

### 2. Contrast Enhancement
Improves the visibility of details by increasing the difference between light and dark regions of the image.

### 3. Image Sharpening
Enhances edges and fine details to make the image appear clearer and more defined.

### 4. Sobel Edge Detection
Applies the Sobel operator to detect edges by calculating gradients in horizontal and vertical directions.

### 5. Edge Thickening
Enhances detected edges by increasing their thickness, making them more prominent and easier to visualize.

All processed images are automatically saved in the `output/` directory.

---

## Continuous Integration (CI) Pipeline

The CI pipeline runs automatically on:

- Every push to `main`
- Every pull request to `main`

The pipeline performs the following steps:

1. Checks out the repository  
2. Sets up Python 3.10  
3. Installs project dependencies  
4. Runs the image processing script  
5. Executes automated tests using PyTest  
6. Archives processed images as artifacts  
7. Automatically commits and pushes updated output files  

This ensures automation, reliability, and consistent results across all updates.

---

## DevOps and Automation Concepts Applied

- Continuous Integration (CI)
- Automated testing with PyTest
- Workflow automation using GitHub Actions
- Version control tracking using Git commits
- Automatic artifact generation and output management

---

## Group Members and Roles

- **Celestino, Gabriella Mae A.** – Image Processing Lead  
- **Daulo, Carljan** – DevOps Engineer  
- **Borral, Jaira Mae U.** – Tester  
- **Cruz, Eliana Wendy DC.** – Documenter / Presenter  

---

## License

This project was developed strictly for educational purposes as part of an academic requirement. It is intended to demonstrate concepts in image processing, continuous integration, DevOps workflows, and collaborative software development using GitHub.
