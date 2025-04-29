import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# === Cube Creation ===
def create_cube():
    vertices = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ])
    return vertices

def get_faces(vertices):
    faces = [
        [vertices[j] for j in [0,1,2,3]],
        [vertices[j] for j in [4,5,6,7]],
        [vertices[j] for j in [0,1,5,4]],
        [vertices[j] for j in [2,3,7,6]],
        [vertices[j] for j in [1,2,6,5]],
        [vertices[j] for j in [4,7,3,0]]
    ]
    return faces
def apply_transformation(vertices, matrix):
    ones = np.ones((vertices.shape[0], 1))
    vertices_homogeneous = np.hstack([vertices, ones])
    transformed_vertices = vertices_homogeneous @ matrix.T
    return transformed_vertices[:, :3]

# === Transformations ===
def scale(event):
    sx, sy, sz = float(scale_x_box.text), float(scale_y_box.text), float(scale_z_box.text)
    matrix = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    transform_cube(matrix)

def translate(event):
    tx, ty, tz = float(trans_x_box.text), float(trans_y_box.text), float(trans_z_box.text)
    matrix = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])
    transform_cube(matrix)

def reflect(event):
    rx, ry, rz = float(reflect_x_box.text), float(reflect_y_box.text), float(reflect_z_box.text)
    matrix = np.array([
        [rx, 0, 0, 0],
        [0, ry, 0, 0],
        [0, 0, rz, 0],
        [0, 0, 0, 1]
    ])
    transform_cube(matrix)



def shear(event):
    shx, shy, shz = float(shear_x_box.text), float(shear_y_box.text), float(shear_z_box.text)
    matrix = np.array([
        [1, shx, shx, 0],
        [shy, 1, shy, 0],
        [shz, shz, 1, 0],
        [0, 0, 0, 1]
    ])
    transform_cube(matrix)

def rotate(event):
    angle = np.deg2rad(float(rotate_angle_box.text))
    cos_theta, sin_theta = np.cos(angle), np.sin(angle)
    matrix = np.array([
        [cos_theta, -sin_theta, 0, 0],
        [sin_theta, cos_theta,  0, 0],
        [0,         0,          1, 0],
        [0,         0,          0, 1]
    ])
    transform_cube(matrix)

def reset(event):
    global cube_vertices
    cube_vertices = create_cube()
    update_plot()

def transform_cube(matrix):
    global cube_vertices
    cube_vertices = apply_transformation(cube_vertices, matrix)
    update_plot()

def update_plot():
    faces = get_faces(cube_vertices)
    cube_poly.set_verts(faces)
    fig.canvas.draw_idle()


# === Main Plot ===
fig = plt.figure(figsize=(14, 8))

# --- 3D Axis (Cube)
ax = fig.add_axes([0.3, 0.1, 0.65, 0.8], projection='3d')
cube_vertices = create_cube()
faces = get_faces(cube_vertices)
cube_poly = Poly3DCollection(faces, facecolors='deepskyblue', edgecolors='black', linewidths=1, alpha=0.9)
ax.add_collection3d(cube_poly)

ax.set_xlim(-2, 3)
ax.set_ylim(-2, 3)
ax.set_zlim(-2, 3)
ax.set_box_aspect([1, 1, 1])
ax.set_title("Interactive 3D Cube", fontsize=16, pad=10)

