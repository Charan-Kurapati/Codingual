

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# PART 1: Set up folder paths

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)

INPUT_DIR = os.path.join(PROJECT_DIR, "original_images")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "output_images")

# Create output folder if it does not exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Check whether input folder exists
if not os.path.isdir(INPUT_DIR):
    raise FileNotFoundError(
        f"Input folder not found: {INPUT_DIR}\n"
        "Please create the 'original_images' folder."
    )

# PART 2: Find image files

supported_exts = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp")

image_files = [
    f for f in os.listdir(INPUT_DIR)
    if f.lower().endswith(supported_exts)
]

if not image_files:
    raise FileNotFoundError(
        f"No images found in '{INPUT_DIR}'.\n"
        "Please place at least one JPG, PNG, BMP or TIFF image in this folder."
    )

# Select the first image
image_path = os.path.join(INPUT_DIR, sorted(image_files)[0])

print(f"[INFO] Loading image: {image_path}")

image = cv2.imread(image_path)

if image is None:
    raise IOError(
        f"OpenCV could not read '{image_path}'. "
        "The file may be corrupt or unsupported."
    )

print(f"[INFO] Image loaded - shape: {image.shape}, dtype: {image.dtype}")


# PART 3: Convert image to grayscale

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("[INFO] Converted to grayscale.")

plt.figure(figsize=(6, 5))
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.tight_layout()
plt.show()


# PART 4: Crop the image

h, w = image.shape[:2]

# Choose a crop region while staying inside image boundaries
row_start = min(100, h - 1)
row_end = min(300, h)

col_start = min(200, w - 1)
col_end = min(400, w)

# Correct image slicing
cropped_image = image[row_start:row_end, col_start:col_end]

if cropped_image.size == 0:
    raise ValueError("The cropped image is empty.")

print(
    f"[INFO] Cropped region "
    f"[{row_start}:{row_end}, {col_start}:{col_end}] "
    f"- shape: {cropped_image.shape}"
)


# PART 5: Rotate the image

center = (w // 2, h // 2)

angle_degrees = 45
scale = 1.0

rotation_matrix = cv2.getRotationMatrix2D(
    center, angle_degrees, scale
)

# Specify the output size (width, height)
rotated_image = cv2.warpAffine(
    image, rotation_matrix, (w, h)
)

print(f"[INFO] Image rotated by {angle_degrees} degrees.")


# PART 6: Increase brightness

brightness_increment = 50

brightness_matrix = np.ones(
    image.shape, dtype="uint8"
) * brightness_increment

bright_image = cv2.add(image, brightness_matrix)

print(f"[INFO] Brightness increased by {brightness_increment}.")


# PART 7: Save transformed images

outputs = {
    "grayscale.jpg": gray_image,
    "cropped.jpg": cropped_image,
    "rotated.jpg": rotated_image,
    "brightened.jpg": bright_image
}

for filename, img in outputs.items():

    save_path = os.path.join(OUTPUT_DIR, filename)

    success = cv2.imwrite(save_path, img)

    if success:
        print(f"[INFO] Saved: {save_path}")
    else:
        print(f"[ERROR] Could not save: {save_path}")


# PART 8: Display final message

print("\n[DONE] All transformations complete!")
print(f"Check your output folder: {OUTPUT_DIR}")
