class Settings:
    SW_default = 800
    SH_default = 600
    FPS_default = 60
    def __init__(self):
        self.screen_width = self.SW_default
        self.screen_height = self.SH_default
        self.screen_dimensions = (self.screen_width, self.screen_height)

        self.FPS = self.FPS_default
        self.note_leniency = self.screen_height / 40

class Config:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0) # Neon Green
    BLUE = (0, 0, 255)

    # Note: Standard DDR colours are Sky-Blue, Orange, Yellow, and Green
    def __init__(self):
        pass