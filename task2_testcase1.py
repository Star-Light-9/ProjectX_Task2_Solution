import cv2 as cv
from google.colab.patches import cv2_imshow
import numpy as np

from google.colab import files
uploaded = files.upload()

# Import image into variable img
Bhaskar = cv.imread("Bhaskar.jpg")
Chintan = cv.imread("Chintan.jpg")
Ganshyam = cv.imread("Ganshyam.jpg")
Raghav = cv.imread("Raghav.jpg")
Omkar = cv.imread("Omkar.jpg")
Yash = cv.imread("Yash.jpg")


# Save height and width for traversal
height, width = Bhaskar.shape[:2]

# White base image
white_img1 = 255 * np.ones((height, width, 3), dtype=np.uint8)

# Accessing pixels and merging images
for i in range(height):
  for j in range(width):
    if (Bhaskar[i,j] == (0, 0, 0)).all() and (Raghav[i,j] == (0, 0, 0)).all() and (Ganshyam[i,j] == (0, 0, 0)).all() :
      white_img1[i,j] = (0, 0, 0)
    else:
      b1, g1, r1 = Bhaskar[i,j]
      b2, g2, r2 = Raghav[i,j]
      b3, g3, r3 = Ganshyam[i,j]

      b = (int(b1) + int(b2) + int(b3)) // 3
      g = (int(g1) + int(g2) + int(g3)) // 3
      r = (int(r1) + int(r2) + int(r3)) // 3

      white_img1[i,j] = (b, g, r)

cv2_imshow(white_img1)
cv.waitKey(0)
cv.destroyAllWindows()

# Copy image
img1 = white_img1[:]

# Decide number of rows and columns
num_rows = 10
num_cols = 7

# Calculate spacing
row_height = height // num_rows
col_width = width // num_cols

# Draw horizontal lines
for r in range(1, num_rows):
    y = r * row_height
    cv.line(img1, (0, y), (width, y), color=(0, 255, 0), thickness=1)

# Draw vertical lines
for c in range(1, num_cols):
    x = c * col_width
    cv.line(img1, (x, 0), (x, height), color=(0, 255, 0), thickness=1)


# To store (row, col) of all filled cells
filled_cells = []

# Access pixels cell by cell
for i in range(num_rows):
    for j in range(num_cols):

        # Starting pixel of cell
        x1 = j * col_width
        y1 = i * row_height

        # Ending pixels of cell
        x2 = (j + 1) * col_width
        y2 = (i + 1) * row_height
        
        # Store pixels of one cell
        cell = img1[y1:y2, x1:x2]

        # Mask of non-black pixels
        non_black_mask = np.any(cell != [0, 0, 0], axis=2)

        # Count non-black pixels
        non_black_pixels = np.count_nonzero(non_black_mask)
        total_pixels = cell.shape[0] * cell.shape[1]

        # Check threshold
        if non_black_pixels > total_pixels * 0.33:
            filled_cells.append((i, j))  # Store the cell's row and col

# Print all found cells:
for (row, col) in filled_cells:
    if col == 1:
        print(f"{row} A")
    elif col == 3:
        print(f"{row} B")
    elif col == 5:
        print(f"{row} C")
    elif col == 6:
        print(f"{row} D")

