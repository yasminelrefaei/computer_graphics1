import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Paper plane shape (triangle)
plane = np.array([
    [0, 1, 0.5, 0],   # x-coordinates
    [0, 0, 1, 0]      # y-coordinates
])

# Bird shape (simple V)
bird = np.array([
    [-0.2, 0, 0.2], 
    [0, 0.2, 0]
])

# Cloud shape (just circles)
cloud_centers = [
    (-5, 4), (0, 5), (5, 4)
]

# Set up figure
fig, ax = plt.subplots()

def draw_sun():
    sun = plt.Circle((7, 7), 1, color='yellow')
    ax.add_artist(sun)

def draw_cloud(x, y):
    cloud = plt.Circle((x, y), 0.8, color='lightgrey')
    ax.add_artist(cloud)
    cloud2 = plt.Circle((x + 0.6, y + 0.2), 0.6, color='lightgrey')
    ax.add_artist(cloud2)
    cloud3 = plt.Circle((x - 0.6, y + 0.2), 0.6, color='lightgrey')
    ax.add_artist(cloud3)
