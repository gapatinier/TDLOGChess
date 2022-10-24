import dataclasses
import enum
from typing import Optional

class Color(enum.Enum):
    """
    The two possible colors of a pawn.
    """
    
    BLACK = "black"
    WHITE = "white"
    
