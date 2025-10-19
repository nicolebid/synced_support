# from .studentview_callbacks import register_callbacks as studentview_callbacks
from .taskview_callbacks import register_callbacks as taskview_callbacks
from src.universal_callbacks import register_callbacks as universal_callbacks

def register_callbacks(app):
    # studentview_callbacks(app)
    taskview_callbacks(app)
    universal_callbacks(app)
