
# Settings/config.py
# Central knobs for the whole game (keep numbers here so tuning is painless).

WINDOW_TITLE = "Meowgic Catch — Basic Environment"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

FOV_Y = 70.0
Z_NEAR = 0.1
Z_FAR  = 2000.0

# Grid definition (units are arbitrary; treat 1.0 as one cell)
CELL_SIZE = 60.0
GRID_HALF_CELLS = 8  # total grid size ~ (2*GRID_HALF_CELLS+1) cells per side

# Time-of-day cycle
TIME_OF_DAY_DURATION_SEC = 30.0  # morning -> afternoon -> evening -> morning ...

# Colors (RGB 0..1)
COLOR_MORNING_SKY   = (0.65, 0.80, 1.00)
COLOR_AFTERNOON_SKY = (0.40, 0.70, 1.00)
COLOR_EVENING_SKY   = (0.05, 0.05, 0.10)

COLOR_MORNING_FLOOR   = (0.80, 0.90, 0.85)
COLOR_AFTERNOON_FLOOR = (0.70, 0.85, 0.80)
COLOR_EVENING_FLOOR   = (0.30, 0.35, 0.40)

# Camera defaults
CAM_DISTANCE = 900.0  # distance from origin
CAM_YAW_DEG  = 35.0
CAM_PITCH_DEG= 45.0

# Debug flags
SHOW_AXES = True
SHOW_GRID_LINES = True
