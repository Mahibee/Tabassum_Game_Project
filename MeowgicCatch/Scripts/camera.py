# Scripts/camera.py
from math import sin, cos, radians
from OpenGL.GL import glMatrixMode, glLoadIdentity, GL_PROJECTION, GL_MODELVIEW
from OpenGL.GLU import gluPerspective, gluLookAt
import Settings.config as C  

class Camera:
    def __init__(self):
        self.distance = C.CAM_DISTANCE
        self.yaw_deg  = C.CAM_YAW_DEG
        self.pitch_deg= C.CAM_PITCH_DEG
        self.aspect   = C.WINDOW_WIDTH / max(1, C.WINDOW_HEIGHT)
        self.target   = (0.0, 0.0, 0.0)

    def resize(self, w, h):
        self.aspect = (w / max(1, h))

    def apply_perspective(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(C.FOV_Y, self.aspect, C.Z_NEAR, C.Z_FAR)

        eye = self._calc_eye()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(eye[0], eye[1], eye[2],
        self.target[0], self.target[1], self.target[2],
        0.0, 0.0, 1.0)

    def _calc_eye(self):
        r = self.distance
        yaw = radians(self.yaw_deg)
        pitch = radians(self.pitch_deg)
        x = r * cos(pitch) * cos(yaw)
        y = r * cos(pitch) * sin(yaw)
        z = r * sin(pitch)
        return (x, y, z)
