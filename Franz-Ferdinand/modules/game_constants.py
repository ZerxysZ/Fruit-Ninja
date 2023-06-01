# ---------
# CONSTANTS
# ---------

DEFAULT_WINDOW_SIZE = (1920, 1080) # All images and movement will be scaled according to this window size

GAME_OVER_WAIT_TICKS = 180 # Number of ticks to show the game over screen

# PyGame settings
FULLSCREEN = True
WINDOW_SIZE = (960, 540)        # This is ignored if FULLSCREEN is set to True

SHOW_BACKGROUND_IMAGE = True
HIDE_MOUSE = False
GAME_FPS = 60
SHOW_FPS = True

# Colors
BLUE = (0, 0, 255)
LIGHT_BLUE = (164,219,232)
DARK_BLUE = (0,20,64)
BLACK = BG_COLOR = (0, 0, 0)

# Trail settings
MAX_LEN_TRAIL = 40
TRAIL_CIRCLE_WIDTH = 15
TRAIL_COLOR_SCHEME = (DARK_BLUE, BLUE, LIGHT_BLUE)