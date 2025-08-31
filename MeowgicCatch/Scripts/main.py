# Scripts/main.py
import os, sys, time
# Add project root to sys.path so absolute imports work when running this file directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import Settings.config as C                    
from Scripts.camera import Camera              
from Scripts.world import World                
from Scripts import hud                        

window_id = None
cam = Camera()
world = World()
last_time = None
fps_accum = 0.0
fps_frames = 0
fps_value = 0.0

def init_gl():
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    # Basic light for subtle shading (comment out if not allowed by course rules)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION,  (0.0, 0.0, 1000.0, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE,   (0.9, 0.9, 0.9, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR,  (0.2, 0.2, 0.2, 1.0))

def display():
    world.apply_clear_color()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    cam.apply_perspective()

    # Draw the world (floor, grid, axes)
    world.draw()

    # HUD (phase, FPS, controls)
    hud.begin_ortho(C.WINDOW_WIDTH, C.WINDOW_HEIGHT)
    hud.draw_text(10, C.WINDOW_HEIGHT - 20, f"Phase: {world.phase}")
    hud.draw_text(10, C.WINDOW_HEIGHT - 40, f"FPS: {fps_value:.1f}")
    hud.draw_text(10, C.WINDOW_HEIGHT - 60, "Keys: [1/2] yaw  [3/4] pitch  [+/-] zoom  [Esc] quit")
    hud.end_ortho()

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    cam.resize(w, h)

def update_timer(value):
    global last_time, fps_accum, fps_frames, fps_value
    now = time.time()
    if last_time is None:
        last_time = now
    dt = now - last_time
    last_time = now
    dt = max(0.0, min(dt, 0.1))  # clamp

    world.update(dt)

    # FPS
    fps_accum += dt
    fps_frames += 1
    if fps_accum >= 0.5:
        fps_value = fps_frames / fps_accum
        fps_accum, fps_frames = 0.0, 0

    glutPostRedisplay()
    glutTimerFunc(16, update_timer, 0)  # ~60 FPS

def on_keyboard(key, x, y):
    k = key.decode("utf-8") if isinstance(key, (bytes, bytearray)) else key
    if k == '\x1b':  # ESC  <-- fixed literal
        if hasattr(glutLeaveMainLoop, "__call__"):
            glutLeaveMainLoop()
        else:
            sys.exit(0)
    elif k == '+':
        cam.distance = max(100.0, cam.distance - 30.0)
    elif k == '-':
        cam.distance = min(2000.0, cam.distance + 30.0)
    elif k == '1':
        cam.yaw_deg -= 5.0
    elif k == '2':
        cam.yaw_deg += 5.0
    elif k == '3':
        cam.pitch_deg = max(10.0, cam.pitch_deg - 3.0)
    elif k == '4':
        cam.pitch_deg = min(85.0, cam.pitch_deg + 3.0)

def main():
    global window_id
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(C.WINDOW_WIDTH, C.WINDOW_HEIGHT)
    glutInitWindowPosition(100, 100)
    window_id = glutCreateWindow(C.WINDOW_TITLE.encode("utf-8"))

    init_gl()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(on_keyboard)
    glutTimerFunc(0, update_timer, 0)

    glutMainLoop()

if __name__ == "__main__":
    main()
