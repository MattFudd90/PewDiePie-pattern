from perlin_noise import PerlinNoise
import numpy as np
import matplotlib.pyplot as plt
import random

# Create Perlin noise generator
noise = PerlinNoise(octaves=3, seed=random.randint(0, 1000))

# Image size
width, height = 1000, 1000

# Create noise grid
grid = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        grid[i][j] = noise([i / height, j / width])

# Plot contour lines with black background
plt.figure(figsize=(8, 8), facecolor='black')
plt.contour(
    grid,
    levels=12,              
    colors="red",
    linewidths=3,       
    linestyles="solid"
)
plt.gca().set_facecolor("black")  # black background for axes

# Clean look
plt.axis("off")
plt.tight_layout()
plt.show()

