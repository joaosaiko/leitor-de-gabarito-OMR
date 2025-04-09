import aspose.pydrawing
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable
from enum import Enum

class PrivateFontCollection:
    
    def __init__(self):
        ...
    
    def add_font_file(self, filename: str) -> None:
        ...
    
    @property
    def families(self) -> list[aspose.pydrawing.FontFamily]:
        ...
    
    ...

class FontCollection:
    
    @property
    def families(self) -> list[aspose.pydrawing.FontFamily]:
        ...
    
    ...

class InstalledFontCollection:
    
    def __init__(self):
        ...
    
    @property
    def families(self) -> list[aspose.pydrawing.FontFamily]:
        ...
    
    ...

class GenericFontFamilies(Enum):
    
    SERIF: int
    
    SANS_SERIF: int
    
    MONOSPACE: int
    

class HotkeyPrefix(Enum):
    
    NONE: int
    
    SHOW: int
    
    HIDE: int
    

class TextRenderingHint(Enum):
    
    SYSTEM_DEFAULT: int
    
    SINGLE_BIT_PER_PIXEL_GRID_FIT: int
    
    SINGLE_BIT_PER_PIXEL: int
    
    ANTI_ALIAS_GRID_FIT: int
    
    ANTI_ALIAS: int
    
    CLEAR_TYPE_GRID_FIT: int
    

