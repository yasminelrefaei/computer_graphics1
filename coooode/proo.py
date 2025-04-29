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

def apply_transformation(vertices, matrix):
    ones = np.ones((vertices.shape[0], 1))
    vertices_homogeneous = np.hstack([vertices, ones])
    transformed_vertices = vertices_homogeneous @ matrix.T
    return transformed_vertices[:, :3]
