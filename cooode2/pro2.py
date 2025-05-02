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
def shear(part, shear_factor_x=0.0, shear_factor_y=0.0):
    S = np.array([
        [1, shear_factor_x],
        [shear_factor_y, 1]
    ])
    return part @ S

def reflect(part, axis='x'):
    if axis == 'x':
        R = np.array([[1, 0], [0, -1]])
    elif axis == 'y':
        R = np.array([[-1, 0], [0, 1]])
    return part @ R

# Animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 5)
ax.set_ylim(-2, 4)
ax.set_aspect('equal')
ax.axis('off')

robot = create_robot()

def update(frame):
    ax.clear()
    ax.set_xlim(-2, 5)
    ax.set_ylim(-2, 4)
    ax.set_aspect('equal')
    ax.axis('off')

    move_x = frame * 0.03
    walk_angle = 10 * np.sin(frame * 0.3)
    jump_height = 0.5 * abs(np.sin(frame * 0.15))  # jumping effect
    shear_factor = 0.2 * np.sin(frame * 0.15)     # shearing during jump
    scale_factor = 1.0 + 0.2 * np.sin(frame * 0.2) # growing and shrinking

    transformed_robot = []
    reflected_robot = []
    for i, part in enumerate(robot):
        p = part.copy()

# Walking translation
    p = translate(p, move_x, 0)
    
    # Jumping
    p = translate(p, 0, jump_height)
    
    # Shearing
    p = shear(p, shear_factor_x=shear_factor)
    
    # Scaling
    p = scale(p, scale_factor, center=(0.5 + move_x, 1.0 + jump_height))
    
    # Limb rotations
    if i == 2:  # left leg
        p = rotate(p, walk_angle, origin=(0.475 + move_x, 1.0 + jump_height))
    if i == 3:  # right leg
        p = rotate(p, -walk_angle, origin=(0.525 + move_x, 1.0 + jump_height))
    if i == 4:  # left arm
        p = rotate(p, -walk_angle, origin=(0.4 + move_x, 1.7 + jump_height))
    if i == 5:  # right arm
        p = rotate(p, walk_angle, origin=(0.6 + move_x, 1.7 + jump_height))
    
    transformed_robot.append(p)
    
    # Reflection over x-axis (ground line at y=0)
    pr = reflect(p, axis='x')
    pr = translate(pr, 0, 0)  # optional offset if needed
    reflected_robot.append(pr)

# Draw robot
    draw_robot(ax, transformed_robot, color='cyan', alpha=1.0)

    # Draw reflection
    draw_robot(ax, reflected_robot, color='lightblue', alpha=0.3)

ani = FuncAnimation(fig, update, frames=200, interval=50)
plt.show()
