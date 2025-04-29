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
