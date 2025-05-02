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

def init():
    ax.set_xlim(-10, 10)
    ax.set_ylim(-2, 10)
    ax.set_aspect('equal')
    ax.set_facecolor('skyblue')
    return []

def animate(frame):
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-2, 10)
    ax.set_aspect('equal')
    ax.set_facecolor('skyblue')

    draw_sun()

    # Move clouds
    for cx, cy in cloud_centers:
        draw_cloud(cx + frame*0.05 % 20 - 10, cy)

    # Paper plane transformations
        scale_factor = 1 + frame * 0.01
        rotate_angle = np.deg2rad(frame)
        shear_factor = 0.001 * frame
    
        S = np.array([
            [scale_factor, 0, 0],
            [0, scale_factor, 0],
            [0, 0, 1]
        ])
    
        R = np.array([
            [np.cos(rotate_angle), -np.sin(rotate_angle), 0],
            [np.sin(rotate_angle), np.cos(rotate_angle), 0],
            [0, 0, 1]
        ])
    
        Sh = np.array([
            [1, shear_factor, 0],
            [shear_factor, 1, 0],
            [0, 0, 1]
        ])
    
        T = np.array([
            [1, 0, frame * 0.05],
            [0, 1, frame * 0.03],
            [0, 0, 1]
        ])
