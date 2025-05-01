import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create robot parts
def create_robot():
    head = np.array([[0.4, 1.8], [0.6, 1.8], [0.6, 2.0], [0.4, 2.0]])
    body = np.array([[0.45, 1.0], [0.55, 1.0], [0.55, 1.8], [0.45, 1.8]])
    left_leg = np.array([[0.45, 0.0], [0.5, 0.0], [0.5, 1.0], [0.45, 1.0]])
    right_leg = np.array([[0.5, 0.0], [0.55, 0.0], [0.55, 1.0], [0.5, 1.0]])
    left_arm = np.array([[0.35, 1.2], [0.45, 1.2], [0.45, 1.7], [0.35, 1.7]])
    right_arm = np.array([[0.55, 1.2], [0.65, 1.2], [0.65, 1.7], [0.55, 1.7]])
    return [head, body, left_leg, right_leg, left_arm, right_arm]

# Draw robot on the plot
def draw_robot(ax, robot_parts, color='cyan', alpha=1.0):
    for part in robot_parts:
        polygon = plt.Polygon(part, closed=True, edgecolor='black', facecolor=color, alpha=alpha)
        ax.add_patch(polygon)

# Transformations
def translate(part, dx, dy):
    return part + np.array([dx, dy])

def rotate(part, angle_deg, origin=(0.5, 1.0)):
    angle_rad = np.deg2rad(angle_deg)
    R = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad), np.cos(angle_rad)]
    ])
    return (part - origin) @ R + origin

def scale(part, scale_factor, center=(0.5, 1.0)):
    return (part - center) * scale_factor + center
