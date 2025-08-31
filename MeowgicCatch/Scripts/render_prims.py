# Scripts/render_prims.py
from OpenGL.GL import (
    glBegin, glEnd, glVertex3f, glColor3f, glLineWidth,
    GL_LINES
)
import Settings.config as C  

def draw_axes(length=200.0):
    glLineWidth(2.0)
    glBegin(GL_LINES)
    # X axis (red)
    glColor3f(1.0, 0.2, 0.2)
    glVertex3f(0.0, 0.0, 0.0); glVertex3f(length, 0.0, 0.0)
    # Y axis (green)
    glColor3f(0.2, 1.0, 0.2)
    glVertex3f(0.0, 0.0, 0.0); glVertex3f(0.0, length, 0.0)
    # Z axis (blue)
    glColor3f(0.2, 0.4, 1.0)
    glVertex3f(0.0, 0.0, 0.0); glVertex3f(0.0, 0.0, length)
    glEnd()

def draw_grid_lines():
    if not C.SHOW_GRID_LINES:
        return
    half = C.GRID_HALF_CELLS
    s = C.CELL_SIZE
    extent = (2*half + 1) * s * 0.5

    glLineWidth(1.0)
    glColor3f(0.25, 0.35, 0.40)
    glBegin(GL_LINES)
    # Lines parallel to X (varying Y)
    for i in range(-half, half+1):
        y = i * s
        glVertex3f(-extent, y, 0.2)
        glVertex3f( extent, y, 0.2)
    # Lines parallel to Y (varying X)
    for i in range(-half, half+1):
        x = i * s
        glVertex3f(x, -extent, 0.2)
        glVertex3f(x,  extent, 0.2)
    glEnd()
