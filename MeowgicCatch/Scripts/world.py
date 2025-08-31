# Scripts/world.py
from OpenGL.GL import (
    glClearColor, glBegin, glEnd, glColor3f, glVertex3f, glNormal3f, GL_QUADS
)
import Settings.config as C                  
import Scripts.render_prims as rp            

class World:
    def __init__(self):
        self.time_s = 0.0
        self.phase = "morning"  # 'morning' | 'afternoon' | 'evening'

    def update(self, dt):
        self.time_s += dt
        T = C.TIME_OF_DAY_DURATION_SEC
        cycle = (self.time_s % (3*T))
        if cycle < T:
            self.phase = "morning"
        elif cycle < 2*T:
            self.phase = "afternoon"
        else:
            self.phase = "evening"

    def apply_clear_color(self):
        r, g, b = self._sky_color()
        glClearColor(r, g, b, 1.0)

    def draw(self):
        self._draw_floor()
        rp.draw_grid_lines()
        if C.SHOW_AXES:
            rp.draw_axes(200.0)

    def _sky_color(self):
        if self.phase == "morning":
            return C.COLOR_MORNING_SKY
        if self.phase == "afternoon":
            return C.COLOR_AFTERNOON_SKY
        return C.COLOR_EVENING_SKY

    def _floor_color(self):
        if self.phase == "morning":
            return C.COLOR_MORNING_FLOOR
        if self.phase == "afternoon":
            return C.COLOR_AFTERNOON_FLOOR
        return C.COLOR_EVENING_FLOOR

    def _draw_floor(self):
        half = C.GRID_HALF_CELLS * C.CELL_SIZE
        z = 0.0
        r, g, b = self._floor_color()
        glBegin(GL_QUADS)
        glColor3f(r, g, b)
        glNormal3f(0.0, 0.0, 1.0)
        glVertex3f(-half, -half, z)
        glVertex3f( half, -half, z)
        glVertex3f( half,  half, z)
        glVertex3f(-half,  half, z)
        glEnd()
