from aspose.pydrawing import text
from aspose.pydrawing import drawing2d
from aspose.pydrawing import design
from aspose.pydrawing import printing
from aspose.pydrawing import imaging
import aspose.pydrawing
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable
from enum import Enum
from typing import Any


def get_pyinstaller_hook_dirs() -> Any:
    """Function required by PyInstaller. Returns paths to module
    PyInstaller hooks. Not intended to be called explicitly."""
...

class KnownColor:
    '''Known system colors (enumeration).'''
    ACTIVE_BORDER: KnownColor
    ACTIVE_CAPTION: KnownColor
    ACTIVE_CAPTION_TEXT: KnownColor
    ALICE_BLUE: KnownColor
    ANTIQUE_WHITE: KnownColor
    APP_WORKSPACE: KnownColor
    AQUA: KnownColor
    AQUAMARINE: KnownColor
    AZURE: KnownColor
    BEIGE: KnownColor
    BISQUE: KnownColor
    BLACK: KnownColor
    BLANCHED_ALMOND: KnownColor
    BLUE: KnownColor
    BLUE_VIOLET: KnownColor
    BROWN: KnownColor
    BURLY_WOOD: KnownColor
    BUTTON_FACE: KnownColor
    BUTTON_HIGHLIGHT: KnownColor
    BUTTON_SHADOW: KnownColor
    CADET_BLUE: KnownColor
    CHARTREUSE: KnownColor
    CHOCOLATE: KnownColor
    CONTROL: KnownColor
    CONTROL_DARK: KnownColor
    CONTROL_DARK_DARK: KnownColor
    CONTROL_LIGHT: KnownColor
    CONTROL_LIGHT_LIGHT: KnownColor
    CONTROL_TEXT: KnownColor
    CORAL: KnownColor
    CORNFLOWER_BLUE: KnownColor
    CORNSILK: KnownColor
    CRIMSON: KnownColor
    CYAN: KnownColor
    DARK_BLUE: KnownColor
    DARK_CYAN: KnownColor
    DARK_GOLDENROD: KnownColor
    DARK_GRAY: KnownColor
    DARK_GREEN: KnownColor
    DARK_KHAKI: KnownColor
    DARK_MAGENTA: KnownColor
    DARK_OLIVE_GREEN: KnownColor
    DARK_ORANGE: KnownColor
    DARK_ORCHID: KnownColor
    DARK_RED: KnownColor
    DARK_SALMON: KnownColor
    DARK_SEA_GREEN: KnownColor
    DARK_SLATE_BLUE: KnownColor
    DARK_SLATE_GRAY: KnownColor
    DARK_TURQUOISE: KnownColor
    DARK_VIOLET: KnownColor
    DEEP_PINK: KnownColor
    DEEP_SKY_BLUE: KnownColor
    DESKTOP: KnownColor
    DIM_GRAY: KnownColor
    DODGER_BLUE: KnownColor
    FIREBRICK: KnownColor
    FLORAL_WHITE: KnownColor
    FOREST_GREEN: KnownColor
    FUCHSIA: KnownColor
    GAINSBORO: KnownColor
    GHOST_WHITE: KnownColor
    GOLD: KnownColor
    GOLDENROD: KnownColor
    GRADIENT_ACTIVE_CAPTION: KnownColor
    GRADIENT_INACTIVE_CAPTION: KnownColor
    GRAY: KnownColor
    GRAY_TEXT: KnownColor
    GREEN: KnownColor
    GREEN_YELLOW: KnownColor
    HIGHLIGHT: KnownColor
    HIGHLIGHT_TEXT: KnownColor
    HONEYDEW: KnownColor
    HOT_PINK: KnownColor
    HOT_TRACK: KnownColor
    INACTIVE_BORDER: KnownColor
    INACTIVE_CAPTION: KnownColor
    INACTIVE_CAPTION_TEXT: KnownColor
    INDIAN_RED: KnownColor
    INDIGO: KnownColor
    INFO: KnownColor
    INFO_TEXT: KnownColor
    IVORY: KnownColor
    KHAKI: KnownColor
    LAVENDER: KnownColor
    LAVENDER_BLUSH: KnownColor
    LAWN_GREEN: KnownColor
    LEMON_CHIFFON: KnownColor
    LIGHT_BLUE: KnownColor
    LIGHT_CORAL: KnownColor
    LIGHT_CYAN: KnownColor
    LIGHT_GOLDENROD_YELLOW: KnownColor
    LIGHT_GRAY: KnownColor
    LIGHT_GREEN: KnownColor
    LIGHT_PINK: KnownColor
    LIGHT_SALMON: KnownColor
    LIGHT_SEA_GREEN: KnownColor
    LIGHT_SKY_BLUE: KnownColor
    LIGHT_SLATE_GRAY: KnownColor
    LIGHT_STEEL_BLUE: KnownColor
    LIGHT_YELLOW: KnownColor
    LIME: KnownColor
    LIME_GREEN: KnownColor
    LINEN: KnownColor
    MAGENTA: KnownColor
    MAROON: KnownColor
    MEDIUM_AQUAMARINE: KnownColor
    MEDIUM_BLUE: KnownColor
    MEDIUM_ORCHID: KnownColor
    MEDIUM_PURPLE: KnownColor
    MEDIUM_SEA_GREEN: KnownColor
    MEDIUM_SLATE_BLUE: KnownColor
    MEDIUM_SPRING_GREEN: KnownColor
    MEDIUM_TURQUOISE: KnownColor
    MEDIUM_VIOLET_RED: KnownColor
    MENU: KnownColor
    MENU_BAR: KnownColor
    MENU_HIGHLIGHT: KnownColor
    MENU_TEXT: KnownColor
    MIDNIGHT_BLUE: KnownColor
    MINT_CREAM: KnownColor
    MISTY_ROSE: KnownColor
    MOCCASIN: KnownColor
    NAVAJO_WHITE: KnownColor
    NAVY: KnownColor
    OLD_LACE: KnownColor
    OLIVE: KnownColor
    OLIVE_DRAB: KnownColor
    ORANGE: KnownColor
    ORANGE_RED: KnownColor
    ORCHID: KnownColor
    PALE_GOLDENROD: KnownColor
    PALE_GREEN: KnownColor
    PALE_TURQUOISE: KnownColor
    PALE_VIOLET_RED: KnownColor
    PAPAYA_WHIP: KnownColor
    PEACH_PUFF: KnownColor
    PERU: KnownColor
    PINK: KnownColor
    PLUM: KnownColor
    POWDER_BLUE: KnownColor
    PURPLE: KnownColor
    REBECCA_PURPLE: KnownColor
    RED: KnownColor
    ROSY_BROWN: KnownColor
    ROYAL_BLUE: KnownColor
    SADDLE_BROWN: KnownColor
    SALMON: KnownColor
    SANDY_BROWN: KnownColor
    SCROLL_BAR: KnownColor
    SEA_GREEN: KnownColor
    SEA_SHELL: KnownColor
    SIENNA: KnownColor
    SILVER: KnownColor
    SKY_BLUE: KnownColor
    SLATE_BLUE: KnownColor
    SLATE_GRAY: KnownColor
    SNOW: KnownColor
    SPRING_GREEN: KnownColor
    STEEL_BLUE: KnownColor
    TAN: KnownColor
    TEAL: KnownColor
    THISTLE: KnownColor
    TOMATO: KnownColor
    TRANSPARENT: KnownColor
    TURQUOISE: KnownColor
    VIOLET: KnownColor
    WHEAT: KnownColor
    WHITE: KnownColor
    WHITE_SMOKE: KnownColor
    WINDOW: KnownColor
    WINDOW_FRAME: KnownColor
    WINDOW_TEXT: KnownColor
    YELLOW: KnownColor
    YELLOW_GREEN: KnownColor

class Color:
    '''Represents an ARGB color.'''

    @property
    def a(self) -> int:
        '''Gets the alpha component value.'''
        ...

    @property
    def r(self) -> int:
        '''Gets the red component value.'''
        ...

    @property
    def g(self) -> int:
        '''Gets the green component value.'''
        ...

    @property
    def b(self) -> int:
        '''Gets the blue component value.'''
        ...

    @property
    def name(self) -> str:
        '''Gets the name of this Color.'''
        ...

    @property
    def is_empty(self) -> bool:
        '''Returns True if this is uninitialized color.'''
        ...

    @property
    def is_known_color(self) -> bool:
        '''Returns True if this is a predefined color.'''
        ...

    @property
    def is_named_color(self) -> bool:
        '''Returns True if this is a named color.'''
        ...

    @property
    def is_system_color(self) -> bool:
        '''Returns True if this is a system color.'''
        ...

    empty: Color

    alice_blue: Color
    antique_white: Color
    aqua: Color
    aquamarine: Color
    azure: Color
    beige: Color
    bisque: Color
    black: Color
    blanched_almond: Color
    blue: Color
    blue_violet: Color
    brown: Color
    burly_wood: Color
    cadet_blue: Color
    chartreuse: Color
    chocolate: Color
    coral: Color
    cornflower_blue: Color
    cornsilk: Color
    crimson: Color
    cyan: Color
    dark_blue: Color
    dark_cyan: Color
    dark_goldenrod: Color
    dark_gray: Color
    dark_green: Color
    dark_khaki: Color
    dark_magenta: Color
    dark_olive_green: Color
    dark_orange: Color
    dark_orchid: Color
    dark_red: Color
    dark_salmon: Color
    dark_sea_green: Color
    dark_slate_blue: Color
    dark_slate_gray: Color
    dark_turquoise: Color
    dark_violet: Color
    deep_pink: Color
    deep_sky_blue: Color
    dim_gray: Color
    dodger_blue: Color
    firebrick: Color
    floral_white: Color
    forest_green: Color
    fuchsia: Color
    gainsboro: Color
    ghost_white: Color
    gold: Color
    goldenrod: Color
    gray: Color
    green: Color
    green_yellow: Color
    honeydew: Color
    hot_pink: Color
    indian_red: Color
    indigo: Color
    ivory: Color
    khaki: Color
    lavender: Color
    lavender_blush: Color
    lawn_green: Color
    lemon_chiffon: Color
    light_blue: Color
    light_coral: Color
    light_cyan: Color
    light_goldenrod_yellow: Color
    light_gray: Color
    light_green: Color
    light_pink: Color
    light_salmon: Color
    light_sea_green: Color
    light_sky_blue: Color
    light_slate_gray: Color
    light_steel_blue: Color
    light_yellow: Color
    lime: Color
    lime_green: Color
    linen: Color
    magenta: Color
    maroon: Color
    medium_aquamarine: Color
    medium_blue: Color
    medium_orchid: Color
    medium_purple: Color
    medium_sea_green: Color
    medium_slate_blue: Color
    medium_spring_green: Color
    medium_turquoise: Color
    medium_violet_red: Color
    midnight_blue: Color
    mint_cream: Color
    misty_rose: Color
    moccasin: Color
    navajo_white: Color
    navy: Color
    old_lace: Color
    olive: Color
    olive_drab: Color
    orange: Color
    orange_red: Color
    orchid: Color
    pale_goldenrod: Color
    pale_green: Color
    pale_turquoise: Color
    pale_violet_red: Color
    papaya_whip: Color
    peach_puff: Color
    peru: Color
    pink: Color
    plum: Color
    powderblue: Color
    purple: Color
    rebecca_purple: Color
    red: Color
    rosy_brown: Color
    royal_blue: Color
    saddle_brown: Color
    salmon: Color
    sandy_brown: Color
    sea_green: Color
    sea_shell: Color
    sienna: Color
    silver: Color
    sky_blue: Color
    slate_blue: Color
    slate_gray: Color
    snow: Color
    spring_green: Color
    steel_blue: Color
    tan: Color
    teal: Color
    thistle: Color
    tomato: Color
    transparent: Color
    turquoise: Color
    violet: Color
    wheat: Color
    white: Color
    white_smoke: Color
    yellow: Color
    yellow_green: Color

    @overload
    @staticmethod
    def from_argb(value: int) -> Color:
        '''Creates a Color from a 32-bit ARGB value.'''
        ...

    @overload
    @staticmethod
    def from_argb(aplha: int, color: Color) -> Color:
        '''Creates a Color from the specified color with the new alpha value.'''
        ...

    @overload
    @staticmethod
    def from_argb(red: int, green: int, blue: int) -> Color:
        '''Creates a Color from the specified red, green, and blue components.'''
        ...

    @overload
    @staticmethod
    def from_argb(alpha: int, red: int, green: int, blue: int) -> Color:
        '''Creates a Color from the specified alpha, red, green, and blue components.'''
        ...

    @staticmethod
    def from_known_color(color: KnownColor) -> Color:
        '''Creates a Color from the specified predefined color.'''
        ...

    @staticmethod
    def from_name(name: str) -> Color:
        '''Creates a Color with the specified name.'''
        ...

    def get_brightness(self) -> float:
        '''Gets the HSL lightness value.'''
        ...

    def get_hue(self) -> float:
        '''Gets the HSL hue value.'''
        ...

    def get_saturation(self) -> float:
        '''Gets the HSL saturation value.'''
        ...

    def to_argb(self) -> int:
        '''Gets the ARGB value.'''

    def to_known_color(self) -> KnownColor:
        '''Gets the element of the KnownColor enumeration if the Color is created
        from a predefined color; otherwise, returns 0.'''
        ...

    def to_string(self) -> str:
        '''Converts this Color to a string.'''
        ...

class PointF:
    '''Pair of x and y coordinates.'''

    def __init__(self, x: float, y: float):
        '''Initialize PointF with the specified coordinates.'''
        ...

    empty: PointF

    @property
    def is_empty(self) -> bool:
        '''Returns True if x and y are 0.'''
        ...

    @property
    def x(self) -> float:
        '''Gets x-coordinate.'''
        ...

    @x.setter
    def x(self, value: float):
        '''Sets x-coordinate.'''
        ...

    @property
    def y(self) -> float:
        '''Gets y-coordinate.'''
        ...

    @x.setter
    def y(self, value: float):
        '''Sets y-coordinate.'''
        ...

    @staticmethod
    def add(point: PointF, size: SizeF) -> PointF:
        '''Moves a point by a specified offset.'''
        ...

    @staticmethod
    def subtract(point: PointF, size: SizeF) -> PointF:
        '''Moves a point by the negative of a specified offset.'''
        ...

    def to_string(self) -> str:
        '''Converts this PointF to a string.'''
        ...

class SizeF:
    '''Pair of width and height values.'''

    @overload
    def __init__(self, point: PointF):
        '''Initialize SizeF from the specified PointF.'''
        ...

    @overload
    def __init__(self, width: float, height: float):
        '''Initialize SizeF from the specified width and height values.'''
        ...

    @overload
    def __init__(self, other: SizeF):
        '''Initialize SizeF from the existing SizeF.'''
        ...

    empty: SizeF

    @property
    def is_empty(self) -> bool:
        '''Returns True if width and height are 0.'''
        ...

    @property
    def height(self) -> float:
        '''Gets the height value.'''
        ...

    @height.setter
    def height(self, value: float):
        '''Sets the height value.'''
        ...

    @property
    def width(self) -> float:
        '''Gets the width value.'''
        ...

    @width.setter
    def width(self, value: float):
        '''Sets the width value.'''
        ...

    @staticmethod
    def add(a: SizeF, b: SizeF) -> SizeF:
        '''Adds the width and height of one SizeF to the width and height of another SizeF.'''
        ...

    @staticmethod
    def substract(a: SizeF, b: SizeF) -> SizeF:
        '''Substracts the width and height of one SizeF from the width and height of another SizeF.'''
        ...

    def to_point_f(self) -> PointF:
        '''Converts this SizeF to a PointF.'''
        ...

    def to_string(self) -> str:
        '''Converts this SizeF to a string.'''
        ...

class RectangleF:
    '''Stores location and size of a rectangle.'''

    @overload
    def __init__(self, location: PointF, size: SizeF):
        '''Initialize RectangleF from the specified location and size.'''
        ...

    @overload
    def __init__(self, x: float, y: float, width: float, height: float):
        '''Initialize RectangleF from the specified location and size.'''
        ...

    empty: RectangleF

    @property
    def is_empty(self) -> bool:
        '''Returns True if x, y, width and height are 0.'''
        ...

    @property
    def bottom(self) -> float:
        '''Gets the y-coordinate of the bottom edge.'''
        ...

    @property
    def height(self) -> float:
        '''Gets the height value.'''
        ...

    @height.setter
    def height(self, value: float):
        '''Sets the height value.'''
        ...

    @property
    def left(self) -> float:
        '''Gets the x-coordinate of the left edge.'''
        ...

    @property
    def location(self) -> PointF:
        '''Gets the coordinates of the upper-left corner.'''
        ...

    @location.setter
    def location(self, value: PointF):
        '''Sets the coordinates of the upper-left corner.'''
        ...

    @property
    def right(self) -> float:
        '''Gets the x-coordinate of the right edge.'''
        ...

    @property
    def size(self) -> SizeF:
        '''Gets the size.'''
        ...

    @size.setter
    def size(self, value: SizeF):
        '''Sets the size.'''
        ...

    @property
    def top(self) -> float:
        '''Gets the y-coordinate of the top edge.'''
        ...

    @property
    def width(self) -> float:
        '''Gets the width value.'''
        ...

    @width.setter
    def width(self, value: float):
        '''Sets the width value.'''
        ...

    @property
    def x(self) -> float:
        '''Gets the x-coordinate.'''
        ...

    @x.setter
    def x(self, value: float):
        '''Sets the x-coordinate.'''
        ...

    @property
    def y(self) -> float:
        '''Gets the y-coordinate.'''
        ...

    @y.setter
    def y(self, value: float):
        '''Sets the y-coordinate.'''
        ...

    @overload
    def contains(self, point: PointF) -> bool:
        '''Checks if the specified point is inside this rectangle.'''
        ...

    @overload
    def contains(self, rectangle: RectangleF) -> bool:
        '''Checks if the specified rectangle is entirely contained within this rectangle.'''
        ...

    @overload
    def contains(self, x: float, y: float) -> bool:
        '''Checks if the specified point is inside this rectangle.'''
        ...

    @staticmethod
    def from_ltrb(left: float, top: float, right: float, bottom: float) -> RectangleF:
        '''Creates RectangleF from the specified coordinates.'''
        ...

    @overload
    def inflate(self, x: float, y: float) -> RectangleF:
        '''Enlarges rectangle by the specified size.'''
        ...

    @overload
    def inflate(self, size: SizeF) -> RectangleF:
        '''Enlarges rectangle by the specified size.'''
        ...

    def intersect(self, rect: RectangleF):
        '''Intersects this rectangle with the specified rectangle.'''
        ...

    def intersects_with(self, rect: RectangleF) -> bool:
        '''Checks if this rectangle intersects with the specified rectangle.'''
        ...

    @overload
    def offset(self, pos: PointF):
        '''Moves the position of this rectangle by the specified offset.'''
        ...

    @overload
    def offset(self, x: float, y: float):
        '''Moves the position of this rectangle by the specified offset.'''
        ...

    def to_string(self) -> str:
        '''Converts this RectangleF to a string.'''
        ...

    @staticmethod
    def union(a: RectangleF, b: RectangleF) -> RectangleF:
        '''Creates rectangle than can contains both of the specified rectangles.'''
        ...

class Point:
    '''Pair of x and y coordinates.'''

    def __init__(self, x: int, y: int):
        '''Initialize Point with the specified coordinates.'''
        ...

    empty: Point

    @property
    def is_empty(self) -> bool:
        '''Returns True if x and y are 0.'''
        ...

    @property
    def x(self) -> int:
        '''Gets x-coordinate.'''
        ...

    @x.setter
    def x(self, value: int):
        '''Sets x-coordinate.'''
        ...

    @property
    def y(self) -> int:
        '''Gets y-coordinate.'''
        ...

    @x.setter
    def y(self, value: int):
        '''Sets y-coordinate.'''
        ...

    @staticmethod
    def add(point: Point, size: Size) -> Point:
        '''Moves a point by a specified offset.'''
        ...

    @staticmethod
    def subtract(point: Point, size: Size) -> Point:
        '''Moves a point by the negative of a specified offset.'''
        ...

    def to_string(self) -> str:
        '''Converts this Point to a string.'''
        ...

class Size:
    '''Pair of width and height values.'''

    @overload
    def __init__(self, point: Point):
        '''Initialize Size from the specified Point.'''
        ...

    @overload
    def __init__(self, width: int, height: int):
        '''Initialize Size from the specified width and height values.'''
        ...

    @overload
    def __init__(self, other: Size):
        '''Initialize Size from the existing Size.'''
        ...

    empty: Size

    @property
    def is_empty(self) -> bool:
        '''Returns True if width and height are 0.'''
        ...

    @property
    def height(self) -> int:
        '''Gets the height value.'''
        ...

    @height.setter
    def height(self, value: int):
        '''Sets the height value.'''
        ...

    @property
    def width(self) -> int:
        '''Gets the width value.'''
        ...

    @width.setter
    def width(self, value: int):
        '''Sets the width value.'''
        ...

    @staticmethod
    def add(a: Size, b: Size) -> Size:
        '''Adds the width and height of one Size to the width and height of another Size.'''
        ...

    @staticmethod
    def substract(a: Size, b: Size) -> Size:
        '''Substracts the width and height of one Size from the width and height of another Size.'''
        ...

    def to_point_f(self) -> Point:
        '''Converts this Size to a Point.'''
        ...

    def to_string(self) -> str:
        '''Converts this Size to a string.'''
        ...

class Rectangle:
    '''Stores location and size of a rectangle.'''

    @overload
    def __init__(self, location: Point, size: Size):
        '''Initialize Rectangle from the specified location and size.'''
        ...

    @overload
    def __init__(self, x: int, y: int, width: int, height: int):
        '''Initialize Rectangle from the specified location and size.'''
        ...

    empty: Rectangle

    @property
    def is_empty(self) -> bool:
        '''Returns True if x, y, width and height are 0.'''
        ...

    @property
    def bottom(self) -> int:
        '''Gets the y-coordinate of the bottom edge.'''
        ...

    @property
    def height(self) -> int:
        '''Gets the height value.'''
        ...

    @height.setter
    def height(self, value: int):
        '''Sets the height value.'''
        ...

    @property
    def left(self) -> int:
        '''Gets the x-coordinate of the left edge.'''
        ...

    @property
    def location(self) -> Point:
        '''Gets the coordinates of the upper-left corner.'''
        ...

    @location.setter
    def location(self, value: Point):
        '''Sets the coordinates of the upper-left corner.'''
        ...

    @property
    def right(self) -> int:
        '''Gets the x-coordinate of the right edge.'''
        ...

    @property
    def size(self) -> Size:
        '''Gets the size.'''
        ...

    @size.setter
    def size(self, value: Size):
        '''Sets the size.'''
        ...

    @property
    def top(self) -> int:
        '''Gets the y-coordinate of the top edge.'''
        ...

    @property
    def width(self) -> int:
        '''Gets the width value.'''
        ...

    @width.setter
    def width(self, value: int):
        '''Sets the width value.'''
        ...

    @property
    def x(self) -> int:
        '''Gets the x-coordinate.'''
        ...

    @x.setter
    def x(self, value: int):
        '''Sets the x-coordinate.'''
        ...

    @property
    def y(self) -> int:
        '''Gets the y-coordinate.'''
        ...

    @y.setter
    def y(self, value: int):
        '''Sets the y-coordinate.'''
        ...

    @overload
    def contains(self, point: Point) -> bool:
        '''Checks if the specified point is inside this rectangle.'''
        ...

    @overload
    def contains(self, rectangle: Rectangle) -> bool:
        '''Checks if the specified rectangle is entirely contained within this rectangle.'''
        ...

    @overload
    def contains(self, x: int, y: int) -> bool:
        '''Checks if the specified point is inside this rectangle.'''
        ...

    @staticmethod
    def from_ltrb(left: int, top: int, right: int, bottom: int) -> Rectangle:
        '''Creates Rectangle from the specified coordinates.'''
        ...

    @overload
    def inflate(self, x: int, y: int) -> Rectangle:
        '''Enlarges rectangle by the specified size.'''
        ...

    @overload
    def inflate(self, size: Size) -> Rectangle:
        '''Enlarges rectangle by the specified size.'''
        ...

    def intersect(self, rect: Rectangle):
        '''Intersects this rectangle with the specified rectangle.'''
        ...

    def intersects_with(self, rect: Rectangle) -> bool:
        '''Checks if this rectangle intersects with the specified rectangle.'''
        ...

    @overload
    def offset(self, pos: Point):
        '''Moves the position of this rectangle by the specified offset.'''
        ...

    @overload
    def offset(self, x: int, y: int):
        '''Moves the position of this rectangle by the specified offset.'''
        ...

    def to_string(self) -> str:
        '''Converts this Rectangle to a string.'''
        ...

    @staticmethod
    def union(a: Rectangle, b: Rectangle) -> Rectangle:
        '''Creates rectangle than can contains both of the specified rectangles.'''
        ...

class Bitmap:
    
    @overload
    def __init__(self, filename: str):
        ...
    
    @overload
    def __init__(self, filename: str, use_icm: bool):
        ...
    
    @overload
    def __init__(self, stream: io.BytesIO):
        ...
    
    @overload
    def __init__(self, width: int, height: int):
        ...
    
    @overload
    def __init__(self, width: int, height: int, g: aspose.pydrawing.Graphics):
        ...
    
    @overload
    def __init__(self, width: int, height: int, format: aspose.pydrawing.Imaging.PixelFormat):
        ...
    
    @overload
    def __init__(self, original: aspose.pydrawing.Image):
        ...
    
    @overload
    def __init__(self, original: aspose.pydrawing.Image, new_size: aspose.pydrawing.Size):
        ...
    
    @overload
    def __init__(self, original: aspose.pydrawing.Image, width: int, height: int):
        ...
    
    @overload
    def __init__(self, type: object, resource: str):
        ...
    
    @overload
    def __init__(self, stream: io.BytesIO, use_icm: bool):
        ...
    
    @overload
    @staticmethod
    def from_file(filename: str) -> aspose.pydrawing.Image:
        ...
    
    @overload
    @staticmethod
    def from_file(filename: str, use_embedded_color_management: bool) -> aspose.pydrawing.Image:
        ...
    
    @overload
    @staticmethod
    def from_stream(stream: io.BytesIO) -> aspose.pydrawing.Image:
        ...
    
    @overload
    @staticmethod
    def from_stream(stream: io.BytesIO, use_embedded_color_management: bool) -> aspose.pydrawing.Image:
        ...
    
    @overload
    @staticmethod
    def from_stream(stream: io.BytesIO, use_embedded_color_management: bool, validate_image_data: bool) -> aspose.pydrawing.Image:
        ...
    
    @overload
    def save(self, filename: str) -> None:
        ...
    
    @overload
    def save(self, filename: str, format: aspose.pydrawing.Imaging.ImageFormat) -> None:
        ...
    
    @overload
    def save(self, filename: str, encoder: aspose.pydrawing.Imaging.ImageCodecInfo, encoder_params: aspose.pydrawing.Imaging.EncoderParameters) -> None:
        ...
    
    @overload
    def save(self, stream: io.BytesIO, format: aspose.pydrawing.Imaging.ImageFormat) -> None:
        ...
    
    @overload
    def save(self, stream: io.BytesIO, encoder: aspose.pydrawing.Imaging.ImageCodecInfo, encoder_params: aspose.pydrawing.Imaging.EncoderParameters) -> None:
        ...
    
    @overload
    def clone(self, rect: aspose.pydrawing.RectangleF, format: aspose.pydrawing.Imaging.PixelFormat) -> aspose.pydrawing.Bitmap:
        ...
    
    @overload
    def clone(self, rect: aspose.pydrawing.Rectangle, format: aspose.pydrawing.Imaging.PixelFormat) -> aspose.pydrawing.Bitmap:
        ...
    
    @overload
    def clone(self) -> object:
        ...
    
    @overload
    def save_add(self, encoder_params: aspose.pydrawing.Imaging.EncoderParameters) -> None:
        ...
    
    @overload
    def save_add(self, image: aspose.pydrawing.Image, encoder_params: aspose.pydrawing.Imaging.EncoderParameters) -> None:
        ...
    
    @overload
    def make_transparent(self) -> None:
        ...
    
    @overload
    def make_transparent(self, transparent_color: aspose.pydrawing.Color) -> None:
        ...
    
    @overload
    def lock_bits(self, rect: aspose.pydrawing.Rectangle, flags: aspose.pydrawing.Imaging.ImageLockMode, format: aspose.pydrawing.Imaging.PixelFormat) -> aspose.pydrawing.Imaging.BitmapData:
        ...
    
    @overload
    def lock_bits(self, rect: aspose.pydrawing.Rectangle, flags: aspose.pydrawing.Imaging.ImageLockMode, format: aspose.pydrawing.Imaging.PixelFormat, bitmap_data: aspose.pydrawing.Imaging.BitmapData) -> aspose.pydrawing.Imaging.BitmapData:
        ...
    
    def get_frame_count(self, dimension: aspose.pydrawing.Imaging.FrameDimension) -> int:
        ...
    
    def select_active_frame(self, dimension: aspose.pydrawing.Imaging.FrameDimension, frame_index: int) -> int:
        ...
    
    def rotate_flip(self, rotate_flip_type: aspose.pydrawing.RotateFlipType) -> None:
        ...
    
    def remove_property_item(self, propid: int) -> None:
        ...
    
    def get_encoder_parameter_list(self, encoder: uuid.UUID) -> aspose.pydrawing.Imaging.EncoderParameters:
        ...
    
    @staticmethod
    def is_extended_pixel_format(pixfmt: aspose.pydrawing.Imaging.PixelFormat) -> bool:
        ...
    
    @staticmethod
    def is_canonical_pixel_format(pixfmt: aspose.pydrawing.Imaging.PixelFormat) -> bool:
        ...
    
    @staticmethod
    def get_pixel_format_size(pixfmt: aspose.pydrawing.Imaging.PixelFormat) -> int:
        ...
    
    @staticmethod
    def is_alpha_pixel_format(pixfmt: aspose.pydrawing.Imaging.PixelFormat) -> bool:
        ...
    
    def get_bounds(self, page_unit: aspose.pydrawing.GraphicsUnit) -> aspose.pydrawing.RectangleF:
        ...
    
    def get_property_item(self, propid: int) -> aspose.pydrawing.Imaging.PropertyItem:
        ...
    
    def set_property_item(self, propitem: aspose.pydrawing.Imaging.PropertyItem) -> None:
        ...
    
    def unlock_bits(self, bitmapdata: aspose.pydrawing.Imaging.BitmapData) -> None:
        ...
    
    def get_pixel(self, x: int, y: int) -> aspose.pydrawing.Color:
        ...
    
    def set_pixel(self, x: int, y: int, color: aspose.pydrawing.Color) -> None:
        ...
    
    def set_resolution(self, x_dpi: float, y_dpi: float) -> None:
        ...
    
    @property
    def tag(self) -> object:
        ...
    
    @tag.setter
    def tag(self, value: object):
        ...
    
    @property
    def physical_dimension(self) -> aspose.pydrawing.SizeF:
        ...
    
    @property
    def size(self) -> aspose.pydrawing.Size:
        ...
    
    @property
    def width(self) -> int:
        ...
    
    @property
    def height(self) -> int:
        ...
    
    @property
    def horizontal_resolution(self) -> float:
        ...
    
    @property
    def vertical_resolution(self) -> float:
        ...
    
    @property
    def flags(self) -> int:
        ...
    
    @property
    def raw_format(self) -> aspose.pydrawing.Imaging.ImageFormat:
        ...
    
    @property
    def pixel_format(self) -> aspose.pydrawing.Imaging.PixelFormat:
        ...
    
    @property
    def frame_dimensions_list(self) -> list[uuid.UUID]:
        ...
    
    @property
    def palette(self) -> aspose.pydrawing.Imaging.ColorPalette:
        ...
    
    @palette.setter
    def palette(self, value: aspose.pydrawing.Imaging.ColorPalette):
        ...
    
    @property
    def property_id_list(self) -> list[int]:
        ...
    
    @property
    def property_items(self) -> list[aspose.pydrawing.Imaging.PropertyItem]:
        ...
    
    ...

class BitmapSuffixInSameAssemblyAttribute:
    
    def __init__(self):
        ...
    
    ...

class BitmapSuffixInSatelliteAssemblyAttribute:
    
    def __init__(self):
        ...
    
    ...

class BufferedGraphics:
    
    @overload
    def render(self) -> None:
        ...
    
    @overload
    def render(self, target: aspose.pydrawing.Graphics) -> None:
        ...
    
    @property
    def graphics(self) -> aspose.pydrawing.Graphics:
        ...
    
    ...

class BufferedGraphicsContext:
    
    def __init__(self):
        ...
    
    def allocate(self, target_graphics: aspose.pydrawing.Graphics, target_rectangle: aspose.pydrawing.Rectangle) -> aspose.pydrawing.BufferedGraphics:
        ...
    
    def invalidate(self) -> None:
        ...
    
    @property
    def maximum_buffer(self) -> aspose.pydrawing.Size:
        ...
    
    @maximum_buffer.setter
    def maximum_buffer(self, value: aspose.pydrawing.Size):
        ...
    
    ...

class Brushes:
    
    transparent: aspose.pydrawing.Brush
    
    alice_blue: aspose.pydrawing.Brush
    
    antique_white: aspose.pydrawing.Brush
    
    aqua: aspose.pydrawing.Brush
    
    aquamarine: aspose.pydrawing.Brush
    
    azure: aspose.pydrawing.Brush
    
    beige: aspose.pydrawing.Brush
    
    bisque: aspose.pydrawing.Brush
    
    black: aspose.pydrawing.Brush
    
    blanched_almond: aspose.pydrawing.Brush
    
    blue: aspose.pydrawing.Brush
    
    blue_violet: aspose.pydrawing.Brush
    
    brown: aspose.pydrawing.Brush
    
    burly_wood: aspose.pydrawing.Brush
    
    cadet_blue: aspose.pydrawing.Brush
    
    chartreuse: aspose.pydrawing.Brush
    
    chocolate: aspose.pydrawing.Brush
    
    coral: aspose.pydrawing.Brush
    
    cornflower_blue: aspose.pydrawing.Brush
    
    cornsilk: aspose.pydrawing.Brush
    
    crimson: aspose.pydrawing.Brush
    
    cyan: aspose.pydrawing.Brush
    
    dark_blue: aspose.pydrawing.Brush
    
    dark_cyan: aspose.pydrawing.Brush
    
    dark_goldenrod: aspose.pydrawing.Brush
    
    dark_gray: aspose.pydrawing.Brush
    
    dark_green: aspose.pydrawing.Brush
    
    dark_khaki: aspose.pydrawing.Brush
    
    dark_magenta: aspose.pydrawing.Brush
    
    dark_olive_green: aspose.pydrawing.Brush
    
    dark_orange: aspose.pydrawing.Brush
    
    dark_orchid: aspose.pydrawing.Brush
    
    dark_red: aspose.pydrawing.Brush
    
    dark_salmon: aspose.pydrawing.Brush
    
    dark_sea_green: aspose.pydrawing.Brush
    
    dark_slate_blue: aspose.pydrawing.Brush
    
    dark_slate_gray: aspose.pydrawing.Brush
    
    dark_turquoise: aspose.pydrawing.Brush
    
    dark_violet: aspose.pydrawing.Brush
    
    deep_pink: aspose.pydrawing.Brush
    
    deep_sky_blue: aspose.pydrawing.Brush
    
    dim_gray: aspose.pydrawing.Brush
    
    dodger_blue: aspose.pydrawing.Brush
    
    firebrick: aspose.pydrawing.Brush
    
    floral_white: aspose.pydrawing.Brush
    
    forest_green: aspose.pydrawing.Brush
    
    fuchsia: aspose.pydrawing.Brush
    
    gainsboro: aspose.pydrawing.Brush
    
    ghost_white: aspose.pydrawing.Brush
    
    gold: aspose.pydrawing.Brush
    
    goldenrod: aspose.pydrawing.Brush
    
    gray: aspose.pydrawing.Brush
    
    green: aspose.pydrawing.Brush
    
    green_yellow: aspose.pydrawing.Brush
    
    honeydew: aspose.pydrawing.Brush
    
    hot_pink: aspose.pydrawing.Brush
    
    indian_red: aspose.pydrawing.Brush
    
    indigo: aspose.pydrawing.Brush
    
    ivory: aspose.pydrawing.Brush
    
    khaki: aspose.pydrawing.Brush
    
    lavender: aspose.pydrawing.Brush
    
    lavender_blush: aspose.pydrawing.Brush
    
    lawn_green: aspose.pydrawing.Brush
    
    lemon_chiffon: aspose.pydrawing.Brush
    
    light_blue: aspose.pydrawing.Brush
    
    light_coral: aspose.pydrawing.Brush
    
    light_cyan: aspose.pydrawing.Brush
    
    light_goldenrod_yellow: aspose.pydrawing.Brush
    
    light_green: aspose.pydrawing.Brush
    
    light_gray: aspose.pydrawing.Brush
    
    light_pink: aspose.pydrawing.Brush
    
    light_salmon: aspose.pydrawing.Brush
    
    light_sea_green: aspose.pydrawing.Brush
    
    light_sky_blue: aspose.pydrawing.Brush
    
    light_slate_gray: aspose.pydrawing.Brush
    
    light_steel_blue: aspose.pydrawing.Brush
    
    light_yellow: aspose.pydrawing.Brush
    
    lime: aspose.pydrawing.Brush
    
    lime_green: aspose.pydrawing.Brush
    
    linen: aspose.pydrawing.Brush
    
    magenta: aspose.pydrawing.Brush
    
    maroon: aspose.pydrawing.Brush
    
    medium_aquamarine: aspose.pydrawing.Brush
    
    medium_blue: aspose.pydrawing.Brush
    
    medium_orchid: aspose.pydrawing.Brush
    
    medium_purple: aspose.pydrawing.Brush
    
    medium_sea_green: aspose.pydrawing.Brush
    
    medium_slate_blue: aspose.pydrawing.Brush
    
    medium_spring_green: aspose.pydrawing.Brush
    
    medium_turquoise: aspose.pydrawing.Brush
    
    medium_violet_red: aspose.pydrawing.Brush
    
    midnight_blue: aspose.pydrawing.Brush
    
    mint_cream: aspose.pydrawing.Brush
    
    misty_rose: aspose.pydrawing.Brush
    
    moccasin: aspose.pydrawing.Brush
    
    navajo_white: aspose.pydrawing.Brush
    
    navy: aspose.pydrawing.Brush
    
    old_lace: aspose.pydrawing.Brush
    
    olive: aspose.pydrawing.Brush
    
    olive_drab: aspose.pydrawing.Brush
    
    orange: aspose.pydrawing.Brush
    
    orange_red: aspose.pydrawing.Brush
    
    orchid: aspose.pydrawing.Brush
    
    pale_goldenrod: aspose.pydrawing.Brush
    
    pale_green: aspose.pydrawing.Brush
    
    pale_turquoise: aspose.pydrawing.Brush
    
    pale_violet_red: aspose.pydrawing.Brush
    
    papaya_whip: aspose.pydrawing.Brush
    
    peach_puff: aspose.pydrawing.Brush
    
    peru: aspose.pydrawing.Brush
    
    pink: aspose.pydrawing.Brush
    
    plum: aspose.pydrawing.Brush
    
    powder_blue: aspose.pydrawing.Brush
    
    purple: aspose.pydrawing.Brush
    
    red: aspose.pydrawing.Brush
    
    rosy_brown: aspose.pydrawing.Brush
    
    royal_blue: aspose.pydrawing.Brush
    
    saddle_brown: aspose.pydrawing.Brush
    
    salmon: aspose.pydrawing.Brush
    
    sandy_brown: aspose.pydrawing.Brush
    
    sea_green: aspose.pydrawing.Brush
    
    sea_shell: aspose.pydrawing.Brush
    
    sienna: aspose.pydrawing.Brush
    
    silver: aspose.pydrawing.Brush
    
    sky_blue: aspose.pydrawing.Brush
    
    slate_blue: aspose.pydrawing.Brush
    
    slate_gray: aspose.pydrawing.Brush
    
    snow: aspose.pydrawing.Brush
    
    spring_green: aspose.pydrawing.Brush
    
    steel_blue: aspose.pydrawing.Brush
    
    tan: aspose.pydrawing.Brush
    
    teal: aspose.pydrawing.Brush
    
    thistle: aspose.pydrawing.Brush
    
    tomato: aspose.pydrawing.Brush
    
    turquoise: aspose.pydrawing.Brush
    
    violet: aspose.pydrawing.Brush
    
    wheat: aspose.pydrawing.Brush
    
    white: aspose.pydrawing.Brush
    
    white_smoke: aspose.pydrawing.Brush
    
    yellow: aspose.pydrawing.Brush
    
    yellow_green: aspose.pydrawing.Brush
    
    ...

class CharacterRange:
    
    @overload
    def __init__(self, first: int, length: int):
        ...
    
    @overload
    def __init__(self):
        ...
    
    @property
    def first(self) -> int:
        ...
    
    @first.setter
    def first(self, value: int):
        ...
    
    @property
    def length(self) -> int:
        ...
    
    @length.setter
    def length(self, value: int):
        ...
    
    ...

class IDeviceContext:
    
    def release_hdc(self) -> None:
        ...
    
    ...

class Graphics:
    
    @overload
    def flush(self) -> None:
        ...
    
    @overload
    def flush(self, intention: aspose.pydrawing.Drawing2D.FlushIntention) -> None:
        ...
    
    @overload
    def set_clip(self, g: aspose.pydrawing.Graphics) -> None:
        ...
    
    @overload
    def set_clip(self, g: aspose.pydrawing.Graphics, combine_mode: aspose.pydrawing.Drawing2D.CombineMode) -> None:
        ...
    
    @overload
    def set_clip(self, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def set_clip(self, rect: aspose.pydrawing.Rectangle, combine_mode: aspose.pydrawing.Drawing2D.CombineMode) -> None:
        ...
    
    @overload
    def set_clip(self, rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def set_clip(self, rect: aspose.pydrawing.RectangleF, combine_mode: aspose.pydrawing.Drawing2D.CombineMode) -> None:
        ...
    
    @overload
    def set_clip(self, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        ...
    
    @overload
    def set_clip(self, path: aspose.pydrawing.Drawing2D.GraphicsPath, combine_mode: aspose.pydrawing.Drawing2D.CombineMode) -> None:
        ...
    
    @overload
    def set_clip(self, region: aspose.pydrawing.Region, combine_mode: aspose.pydrawing.Drawing2D.CombineMode) -> None:
        ...
    
    @overload
    def intersect_clip(self, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def intersect_clip(self, rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def intersect_clip(self, region: aspose.pydrawing.Region) -> None:
        ...
    
    @overload
    def exclude_clip(self, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def exclude_clip(self, region: aspose.pydrawing.Region) -> None:
        ...
    
    @overload
    def translate_clip(self, dx: float, dy: float) -> None:
        ...
    
    @overload
    def translate_clip(self, dx: int, dy: int) -> None:
        ...
    
    @overload
    def is_visible(self, x: int, y: int) -> bool:
        ...
    
    @overload
    def is_visible(self, point: aspose.pydrawing.Point) -> bool:
        ...
    
    @overload
    def is_visible(self, x: float, y: float) -> bool:
        ...
    
    @overload
    def is_visible(self, point: aspose.pydrawing.PointF) -> bool:
        ...
    
    @overload
    def is_visible(self, x: int, y: int, width: int, height: int) -> bool:
        ...
    
    @overload
    def is_visible(self, rect: aspose.pydrawing.Rectangle) -> bool:
        ...
    
    @overload
    def is_visible(self, x: float, y: float, width: float, height: float) -> bool:
        ...
    
    @overload
    def is_visible(self, rect: aspose.pydrawing.RectangleF) -> bool:
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.Drawing2D.Matrix) -> None:
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.Drawing2D.Matrix, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float) -> None:
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float) -> None:
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        ...
    
    @overload
    def rotate_transform(self, angle: float) -> None:
        ...
    
    @overload
    def rotate_transform(self, angle: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        ...
    
    @overload
    def draw_arc(self, pen: aspose.pydrawing.Pen, x: float, y: float, width: float, height: float, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def draw_arc(self, pen: aspose.pydrawing.Pen, rect: aspose.pydrawing.RectangleF, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def draw_arc(self, pen: aspose.pydrawing.Pen, x: int, y: int, width: int, height: int, start_angle: int, sweep_angle: int) -> None:
        ...
    
    @overload
    def draw_arc(self, pen: aspose.pydrawing.Pen, rect: aspose.pydrawing.Rectangle, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def draw_bezier(self, pen: aspose.pydrawing.Pen, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> None:
        ...
    
    @overload
    def draw_bezier(self, pen: aspose.pydrawing.Pen, pt1: aspose.pydrawing.PointF, pt2: aspose.pydrawing.PointF, pt3: aspose.pydrawing.PointF, pt4: aspose.pydrawing.PointF) -> None:
        ...
    
    @overload
    def draw_bezier(self, pen: aspose.pydrawing.Pen, pt1: aspose.pydrawing.Point, pt2: aspose.pydrawing.Point, pt3: aspose.pydrawing.Point, pt4: aspose.pydrawing.Point) -> None:
        ...
    
    @overload
    def draw_rectangle(self, pen: aspose.pydrawing.Pen, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def draw_rectangle(self, pen: aspose.pydrawing.Pen, x: float, y: float, width: float, height: float) -> None:
        ...
    
    @overload
    def draw_rectangle(self, pen: aspose.pydrawing.Pen, x: int, y: int, width: int, height: int) -> None:
        ...
    
    @overload
    def draw_rectangles(self, pen: aspose.pydrawing.Pen, rects: list[aspose.pydrawing.RectangleF]) -> None:
        ...
    
    @overload
    def draw_rectangles(self, pen: aspose.pydrawing.Pen, rects: list[aspose.pydrawing.Rectangle]) -> None:
        ...
    
    @overload
    def draw_ellipse(self, pen: aspose.pydrawing.Pen, rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def draw_ellipse(self, pen: aspose.pydrawing.Pen, x: float, y: float, width: float, height: float) -> None:
        ...
    
    @overload
    def draw_ellipse(self, pen: aspose.pydrawing.Pen, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def draw_ellipse(self, pen: aspose.pydrawing.Pen, x: int, y: int, width: int, height: int) -> None:
        ...
    
    @overload
    def draw_pie(self, pen: aspose.pydrawing.Pen, rect: aspose.pydrawing.RectangleF, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def draw_pie(self, pen: aspose.pydrawing.Pen, x: float, y: float, width: float, height: float, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def draw_pie(self, pen: aspose.pydrawing.Pen, rect: aspose.pydrawing.Rectangle, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def draw_pie(self, pen: aspose.pydrawing.Pen, x: int, y: int, width: int, height: int, start_angle: int, sweep_angle: int) -> None:
        ...
    
    @overload
    def draw_polygon(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def draw_polygon(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def draw_curve(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def draw_curve(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.PointF], tension: float) -> None:
        ...
    
    @overload
    def draw_curve(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.PointF], offset: int, number_of_segments: int) -> None:
        ...
    
    @overload
    def draw_curve(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.PointF], offset: int, number_of_segments: int, tension: float) -> None:
        ...
    
    @overload
    def draw_curve(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def draw_curve(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.Point], tension: float) -> None:
        ...
    
    @overload
    def draw_curve(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.Point], offset: int, number_of_segments: int, tension: float) -> None:
        ...
    
    @overload
    def draw_closed_curve(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def draw_closed_curve(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.PointF], tension: float, fillmode: aspose.pydrawing.Drawing2D.FillMode) -> None:
        ...
    
    @overload
    def draw_closed_curve(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def draw_closed_curve(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.Point], tension: float, fillmode: aspose.pydrawing.Drawing2D.FillMode) -> None:
        ...
    
    @overload
    def fill_rectangle(self, brush: aspose.pydrawing.Brush, rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def fill_rectangle(self, brush: aspose.pydrawing.Brush, x: float, y: float, width: float, height: float) -> None:
        ...
    
    @overload
    def fill_rectangle(self, brush: aspose.pydrawing.Brush, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def fill_rectangle(self, brush: aspose.pydrawing.Brush, x: int, y: int, width: int, height: int) -> None:
        ...
    
    @overload
    def fill_rectangles(self, brush: aspose.pydrawing.Brush, rects: list[aspose.pydrawing.RectangleF]) -> None:
        ...
    
    @overload
    def fill_rectangles(self, brush: aspose.pydrawing.Brush, rects: list[aspose.pydrawing.Rectangle]) -> None:
        ...
    
    @overload
    def fill_polygon(self, brush: aspose.pydrawing.Brush, points: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def fill_polygon(self, brush: aspose.pydrawing.Brush, points: list[aspose.pydrawing.PointF], fill_mode: aspose.pydrawing.Drawing2D.FillMode) -> None:
        ...
    
    @overload
    def fill_polygon(self, brush: aspose.pydrawing.Brush, points: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def fill_polygon(self, brush: aspose.pydrawing.Brush, points: list[aspose.pydrawing.Point], fill_mode: aspose.pydrawing.Drawing2D.FillMode) -> None:
        ...
    
    @overload
    def fill_ellipse(self, brush: aspose.pydrawing.Brush, rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def fill_ellipse(self, brush: aspose.pydrawing.Brush, x: float, y: float, width: float, height: float) -> None:
        ...
    
    @overload
    def fill_ellipse(self, brush: aspose.pydrawing.Brush, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def fill_ellipse(self, brush: aspose.pydrawing.Brush, x: int, y: int, width: int, height: int) -> None:
        ...
    
    @overload
    def fill_pie(self, brush: aspose.pydrawing.Brush, rect: aspose.pydrawing.Rectangle, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def fill_pie(self, brush: aspose.pydrawing.Brush, x: float, y: float, width: float, height: float, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def fill_pie(self, brush: aspose.pydrawing.Brush, x: int, y: int, width: int, height: int, start_angle: int, sweep_angle: int) -> None:
        ...
    
    @overload
    def fill_closed_curve(self, brush: aspose.pydrawing.Brush, points: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def fill_closed_curve(self, brush: aspose.pydrawing.Brush, points: list[aspose.pydrawing.PointF], fillmode: aspose.pydrawing.Drawing2D.FillMode) -> None:
        ...
    
    @overload
    def fill_closed_curve(self, brush: aspose.pydrawing.Brush, points: list[aspose.pydrawing.PointF], fillmode: aspose.pydrawing.Drawing2D.FillMode, tension: float) -> None:
        ...
    
    @overload
    def fill_closed_curve(self, brush: aspose.pydrawing.Brush, points: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def fill_closed_curve(self, brush: aspose.pydrawing.Brush, points: list[aspose.pydrawing.Point], fillmode: aspose.pydrawing.Drawing2D.FillMode) -> None:
        ...
    
    @overload
    def fill_closed_curve(self, brush: aspose.pydrawing.Brush, points: list[aspose.pydrawing.Point], fillmode: aspose.pydrawing.Drawing2D.FillMode, tension: float) -> None:
        ...
    
    @overload
    def draw_string(self, s: str, font: aspose.pydrawing.Font, brush: aspose.pydrawing.Brush, x: float, y: float) -> None:
        ...
    
    @overload
    def draw_string(self, s: str, font: aspose.pydrawing.Font, brush: aspose.pydrawing.Brush, point: aspose.pydrawing.PointF) -> None:
        ...
    
    @overload
    def draw_string(self, s: str, font: aspose.pydrawing.Font, brush: aspose.pydrawing.Brush, x: float, y: float, format: aspose.pydrawing.StringFormat) -> None:
        ...
    
    @overload
    def draw_string(self, s: str, font: aspose.pydrawing.Font, brush: aspose.pydrawing.Brush, point: aspose.pydrawing.PointF, format: aspose.pydrawing.StringFormat) -> None:
        ...
    
    @overload
    def draw_string(self, s: str, font: aspose.pydrawing.Font, brush: aspose.pydrawing.Brush, layout_rectangle: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def draw_string(self, s: str, font: aspose.pydrawing.Font, brush: aspose.pydrawing.Brush, layout_rectangle: aspose.pydrawing.RectangleF, format: aspose.pydrawing.StringFormat) -> None:
        ...
    
    @overload
    def measure_string(self, text: str, font: aspose.pydrawing.Font, layout_area: aspose.pydrawing.SizeF, string_format: aspose.pydrawing.StringFormat, characters_fitted: int, lines_filled: int) -> aspose.pydrawing.SizeF:
        ...
    
    @overload
    def measure_string(self, text: str, font: aspose.pydrawing.Font, origin: aspose.pydrawing.PointF, string_format: aspose.pydrawing.StringFormat) -> aspose.pydrawing.SizeF:
        ...
    
    @overload
    def measure_string(self, text: str, font: aspose.pydrawing.Font, layout_area: aspose.pydrawing.SizeF) -> aspose.pydrawing.SizeF:
        ...
    
    @overload
    def measure_string(self, text: str, font: aspose.pydrawing.Font, layout_area: aspose.pydrawing.SizeF, string_format: aspose.pydrawing.StringFormat) -> aspose.pydrawing.SizeF:
        ...
    
    @overload
    def measure_string(self, text: str, font: aspose.pydrawing.Font) -> aspose.pydrawing.SizeF:
        ...
    
    @overload
    def measure_string(self, text: str, font: aspose.pydrawing.Font, width: int) -> aspose.pydrawing.SizeF:
        ...
    
    @overload
    def measure_string(self, text: str, font: aspose.pydrawing.Font, width: int, format: aspose.pydrawing.StringFormat) -> aspose.pydrawing.SizeF:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, point: aspose.pydrawing.PointF) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, x: float, y: float) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, x: float, y: float, width: float, height: float) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, point: aspose.pydrawing.Point) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, x: int, y: int) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, x: int, y: int, width: int, height: int) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, dest_points: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, dest_points: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, x: float, y: float, src_rect: aspose.pydrawing.RectangleF, src_unit: aspose.pydrawing.GraphicsUnit) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, x: int, y: int, src_rect: aspose.pydrawing.Rectangle, src_unit: aspose.pydrawing.GraphicsUnit) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, dest_rect: aspose.pydrawing.RectangleF, src_rect: aspose.pydrawing.RectangleF, src_unit: aspose.pydrawing.GraphicsUnit) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, dest_rect: aspose.pydrawing.Rectangle, src_rect: aspose.pydrawing.Rectangle, src_unit: aspose.pydrawing.GraphicsUnit) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, dest_points: list[aspose.pydrawing.PointF], src_rect: aspose.pydrawing.RectangleF, src_unit: aspose.pydrawing.GraphicsUnit) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, dest_points: list[aspose.pydrawing.PointF], src_rect: aspose.pydrawing.RectangleF, src_unit: aspose.pydrawing.GraphicsUnit, image_attr: aspose.pydrawing.Imaging.ImageAttributes) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, dest_points: list[aspose.pydrawing.Point], src_rect: aspose.pydrawing.Rectangle, src_unit: aspose.pydrawing.GraphicsUnit) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, dest_points: list[aspose.pydrawing.Point], src_rect: aspose.pydrawing.Rectangle, src_unit: aspose.pydrawing.GraphicsUnit, image_attr: aspose.pydrawing.Imaging.ImageAttributes) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, dest_rect: aspose.pydrawing.Rectangle, src_x: float, src_y: float, src_width: float, src_height: float, src_unit: aspose.pydrawing.GraphicsUnit) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, dest_rect: aspose.pydrawing.Rectangle, src_x: float, src_y: float, src_width: float, src_height: float, src_unit: aspose.pydrawing.GraphicsUnit, image_attrs: aspose.pydrawing.Imaging.ImageAttributes) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, dest_rect: aspose.pydrawing.Rectangle, src_x: int, src_y: int, src_width: int, src_height: int, src_unit: aspose.pydrawing.GraphicsUnit) -> None:
        ...
    
    @overload
    def draw_image(self, image: aspose.pydrawing.Image, dest_rect: aspose.pydrawing.Rectangle, src_x: int, src_y: int, src_width: int, src_height: int, src_unit: aspose.pydrawing.GraphicsUnit, image_attr: aspose.pydrawing.Imaging.ImageAttributes) -> None:
        ...
    
    @overload
    def draw_image_unscaled(self, image: aspose.pydrawing.Image, point: aspose.pydrawing.Point) -> None:
        ...
    
    @overload
    def draw_image_unscaled(self, image: aspose.pydrawing.Image, x: int, y: int) -> None:
        ...
    
    @overload
    def draw_image_unscaled(self, image: aspose.pydrawing.Image, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def draw_image_unscaled(self, image: aspose.pydrawing.Image, x: int, y: int, width: int, height: int) -> None:
        ...
    
    @overload
    def draw_line(self, pen: aspose.pydrawing.Pen, pt1: aspose.pydrawing.PointF, pt2: aspose.pydrawing.PointF) -> None:
        ...
    
    @overload
    def draw_line(self, pen: aspose.pydrawing.Pen, x1: int, y1: int, x2: int, y2: int) -> None:
        ...
    
    @overload
    def draw_line(self, pen: aspose.pydrawing.Pen, pt1: aspose.pydrawing.Point, pt2: aspose.pydrawing.Point) -> None:
        ...
    
    @overload
    def draw_line(self, pen: aspose.pydrawing.Pen, x1: float, y1: float, x2: float, y2: float) -> None:
        ...
    
    @overload
    def draw_lines(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def draw_lines(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def copy_from_screen(self, upper_left_source: aspose.pydrawing.Point, upper_left_destination: aspose.pydrawing.Point, block_region_size: aspose.pydrawing.Size) -> None:
        ...
    
    @overload
    def copy_from_screen(self, source_x: int, source_y: int, destination_x: int, destination_y: int, block_region_size: aspose.pydrawing.Size) -> None:
        ...
    
    @overload
    def copy_from_screen(self, upper_left_source: aspose.pydrawing.Point, upper_left_destination: aspose.pydrawing.Point, block_region_size: aspose.pydrawing.Size, copy_pixel_operation: aspose.pydrawing.CopyPixelOperation) -> None:
        ...
    
    @overload
    def copy_from_screen(self, source_x: int, source_y: int, destination_x: int, destination_y: int, block_region_size: aspose.pydrawing.Size, copy_pixel_operation: aspose.pydrawing.CopyPixelOperation) -> None:
        ...
    
    @overload
    def transform_points(self, dest_space: aspose.pydrawing.Drawing2D.CoordinateSpace, src_space: aspose.pydrawing.Drawing2D.CoordinateSpace, pts: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def transform_points(self, dest_space: aspose.pydrawing.Drawing2D.CoordinateSpace, src_space: aspose.pydrawing.Drawing2D.CoordinateSpace, pts: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def draw_beziers(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def draw_beziers(self, pen: aspose.pydrawing.Pen, points: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def draw_icon(self, icon: aspose.pydrawing.Icon, x: int, y: int) -> None:
        ...
    
    @overload
    def draw_icon(self, icon: aspose.pydrawing.Icon, target_rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def begin_container(self, dstrect: aspose.pydrawing.RectangleF, srcrect: aspose.pydrawing.RectangleF, unit: aspose.pydrawing.GraphicsUnit) -> aspose.pydrawing.Drawing2D.GraphicsContainer:
        ...
    
    @overload
    def begin_container(self) -> aspose.pydrawing.Drawing2D.GraphicsContainer:
        ...
    
    @overload
    def begin_container(self, dstrect: aspose.pydrawing.Rectangle, srcrect: aspose.pydrawing.Rectangle, unit: aspose.pydrawing.GraphicsUnit) -> aspose.pydrawing.Drawing2D.GraphicsContainer:
        ...
    
    def release_hdc(self) -> None:
        ...
    
    def reset_clip(self) -> None:
        ...
    
    def reset_transform(self) -> None:
        ...
    
    def draw_path(self, pen: aspose.pydrawing.Pen, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        ...
    
    def clear(self, color: aspose.pydrawing.Color) -> None:
        ...
    
    def measure_character_ranges(self, text: str, font: aspose.pydrawing.Font, layout_rect: aspose.pydrawing.RectangleF, string_format: aspose.pydrawing.StringFormat) -> list[aspose.pydrawing.Region]:
        ...
    
    def draw_image_unscaled_and_clipped(self, image: aspose.pydrawing.Image, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @staticmethod
    def from_image(image: aspose.pydrawing.Image) -> aspose.pydrawing.Graphics:
        ...
    
    def get_nearest_color(self, color: aspose.pydrawing.Color) -> aspose.pydrawing.Color:
        ...
    
    def fill_path(self, brush: aspose.pydrawing.Brush, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        ...
    
    def fill_region(self, brush: aspose.pydrawing.Brush, region: aspose.pydrawing.Region) -> None:
        ...
    
    def draw_icon_unstretched(self, icon: aspose.pydrawing.Icon, target_rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    def get_context_info(self) -> object:
        ...
    
    def save(self) -> aspose.pydrawing.Drawing2D.GraphicsState:
        ...
    
    def restore(self, gstate: aspose.pydrawing.Drawing2D.GraphicsState) -> None:
        ...
    
    def end_container(self, container: aspose.pydrawing.Drawing2D.GraphicsContainer) -> None:
        ...
    
    def add_metafile_comment(self, data: bytes) -> None:
        ...
    
    @property
    def clip(self) -> aspose.pydrawing.Region:
        ...
    
    @clip.setter
    def clip(self, value: aspose.pydrawing.Region):
        ...
    
    @property
    def clip_bounds(self) -> aspose.pydrawing.RectangleF:
        ...
    
    @property
    def compositing_mode(self) -> aspose.pydrawing.Drawing2D.CompositingMode:
        ...
    
    @compositing_mode.setter
    def compositing_mode(self, value: aspose.pydrawing.Drawing2D.CompositingMode):
        ...
    
    @property
    def compositing_quality(self) -> aspose.pydrawing.Drawing2D.CompositingQuality:
        ...
    
    @compositing_quality.setter
    def compositing_quality(self, value: aspose.pydrawing.Drawing2D.CompositingQuality):
        ...
    
    @property
    def dpi_x(self) -> float:
        ...
    
    @property
    def dpi_y(self) -> float:
        ...
    
    @property
    def interpolation_mode(self) -> aspose.pydrawing.Drawing2D.InterpolationMode:
        ...
    
    @interpolation_mode.setter
    def interpolation_mode(self, value: aspose.pydrawing.Drawing2D.InterpolationMode):
        ...
    
    @property
    def is_clip_empty(self) -> bool:
        ...
    
    @property
    def is_visible_clip_empty(self) -> bool:
        ...
    
    @property
    def page_scale(self) -> float:
        ...
    
    @page_scale.setter
    def page_scale(self, value: float):
        ...
    
    @property
    def page_unit(self) -> aspose.pydrawing.GraphicsUnit:
        ...
    
    @page_unit.setter
    def page_unit(self, value: aspose.pydrawing.GraphicsUnit):
        ...
    
    @property
    def pixel_offset_mode(self) -> aspose.pydrawing.Drawing2D.PixelOffsetMode:
        ...
    
    @pixel_offset_mode.setter
    def pixel_offset_mode(self, value: aspose.pydrawing.Drawing2D.PixelOffsetMode):
        ...
    
    @property
    def rendering_origin(self) -> aspose.pydrawing.Point:
        ...
    
    @rendering_origin.setter
    def rendering_origin(self, value: aspose.pydrawing.Point):
        ...
    
    @property
    def smoothing_mode(self) -> aspose.pydrawing.Drawing2D.SmoothingMode:
        ...
    
    @smoothing_mode.setter
    def smoothing_mode(self, value: aspose.pydrawing.Drawing2D.SmoothingMode):
        ...
    
    @property
    def text_contrast(self) -> int:
        ...
    
    @text_contrast.setter
    def text_contrast(self, value: int):
        ...
    
    @property
    def text_rendering_hint(self) -> aspose.pydrawing.Text.TextRenderingHint:
        ...
    
    @text_rendering_hint.setter
    def text_rendering_hint(self, value: aspose.pydrawing.Text.TextRenderingHint):
        ...
    
    @property
    def transform(self) -> aspose.pydrawing.Drawing2D.Matrix:
        ...
    
    @transform.setter
    def transform(self, value: aspose.pydrawing.Drawing2D.Matrix):
        ...
    
    @property
    def visible_clip_bounds(self) -> aspose.pydrawing.RectangleF:
        ...
    
    ...

class IconConverter:
    
    def __init__(self):
        ...
    
    ...

class Image:
    
    @overload
    @staticmethod
    def from_file(filename: str) -> aspose.pydrawing.Image:
        ...
    
    @overload
    @staticmethod
    def from_file(filename: str, use_embedded_color_management: bool) -> aspose.pydrawing.Image:
        ...
    
    @overload
    @staticmethod
    def from_stream(stream: io.BytesIO) -> aspose.pydrawing.Image:
        ...
    
    @overload
    @staticmethod
    def from_stream(stream: io.BytesIO, use_embedded_color_management: bool) -> aspose.pydrawing.Image:
        ...
    
    @overload
    @staticmethod
    def from_stream(stream: io.BytesIO, use_embedded_color_management: bool, validate_image_data: bool) -> aspose.pydrawing.Image:
        ...
    
    @overload
    def save(self, filename: str) -> None:
        ...
    
    @overload
    def save(self, filename: str, format: aspose.pydrawing.Imaging.ImageFormat) -> None:
        ...
    
    @overload
    def save(self, filename: str, encoder: aspose.pydrawing.Imaging.ImageCodecInfo, encoder_params: aspose.pydrawing.Imaging.EncoderParameters) -> None:
        ...
    
    @overload
    def save(self, stream: io.BytesIO, format: aspose.pydrawing.Imaging.ImageFormat) -> None:
        ...
    
    @overload
    def save(self, stream: io.BytesIO, encoder: aspose.pydrawing.Imaging.ImageCodecInfo, encoder_params: aspose.pydrawing.Imaging.EncoderParameters) -> None:
        ...
    
    @overload
    def save_add(self, encoder_params: aspose.pydrawing.Imaging.EncoderParameters) -> None:
        ...
    
    @overload
    def save_add(self, image: aspose.pydrawing.Image, encoder_params: aspose.pydrawing.Imaging.EncoderParameters) -> None:
        ...
    
    def get_frame_count(self, dimension: aspose.pydrawing.Imaging.FrameDimension) -> int:
        ...
    
    def select_active_frame(self, dimension: aspose.pydrawing.Imaging.FrameDimension, frame_index: int) -> int:
        ...
    
    def rotate_flip(self, rotate_flip_type: aspose.pydrawing.RotateFlipType) -> None:
        ...
    
    def remove_property_item(self, propid: int) -> None:
        ...
    
    def get_encoder_parameter_list(self, encoder: uuid.UUID) -> aspose.pydrawing.Imaging.EncoderParameters:
        ...
    
    @staticmethod
    def is_extended_pixel_format(pixfmt: aspose.pydrawing.Imaging.PixelFormat) -> bool:
        ...
    
    @staticmethod
    def is_canonical_pixel_format(pixfmt: aspose.pydrawing.Imaging.PixelFormat) -> bool:
        ...
    
    @staticmethod
    def get_pixel_format_size(pixfmt: aspose.pydrawing.Imaging.PixelFormat) -> int:
        ...
    
    @staticmethod
    def is_alpha_pixel_format(pixfmt: aspose.pydrawing.Imaging.PixelFormat) -> bool:
        ...
    
    def clone(self) -> object:
        ...
    
    def get_bounds(self, page_unit: aspose.pydrawing.GraphicsUnit) -> aspose.pydrawing.RectangleF:
        ...
    
    def get_property_item(self, propid: int) -> aspose.pydrawing.Imaging.PropertyItem:
        ...
    
    def set_property_item(self, propitem: aspose.pydrawing.Imaging.PropertyItem) -> None:
        ...
    
    @property
    def tag(self) -> object:
        ...
    
    @tag.setter
    def tag(self, value: object):
        ...
    
    @property
    def physical_dimension(self) -> aspose.pydrawing.SizeF:
        ...
    
    @property
    def size(self) -> aspose.pydrawing.Size:
        ...
    
    @property
    def width(self) -> int:
        ...
    
    @property
    def height(self) -> int:
        ...
    
    @property
    def horizontal_resolution(self) -> float:
        ...
    
    @property
    def vertical_resolution(self) -> float:
        ...
    
    @property
    def flags(self) -> int:
        ...
    
    @property
    def raw_format(self) -> aspose.pydrawing.Imaging.ImageFormat:
        ...
    
    @property
    def pixel_format(self) -> aspose.pydrawing.Imaging.PixelFormat:
        ...
    
    @property
    def frame_dimensions_list(self) -> list[uuid.UUID]:
        ...
    
    @property
    def palette(self) -> aspose.pydrawing.Imaging.ColorPalette:
        ...
    
    @palette.setter
    def palette(self, value: aspose.pydrawing.Imaging.ColorPalette):
        ...
    
    @property
    def property_id_list(self) -> list[int]:
        ...
    
    @property
    def property_items(self) -> list[aspose.pydrawing.Imaging.PropertyItem]:
        ...
    
    ...

class ImageConverter:
    
    def __init__(self):
        ...
    
    ...

class ImageFormatConverter:
    
    def __init__(self):
        ...
    
    ...

class Pen:
    
    @overload
    def __init__(self, color: aspose.pydrawing.Color):
        ...
    
    @overload
    def __init__(self, color: aspose.pydrawing.Color, width: float):
        ...
    
    @overload
    def __init__(self, brush: aspose.pydrawing.Brush):
        ...
    
    @overload
    def __init__(self, brush: aspose.pydrawing.Brush, width: float):
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.Drawing2D.Matrix) -> None:
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.Drawing2D.Matrix, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float) -> None:
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float) -> None:
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        ...
    
    @overload
    def rotate_transform(self, angle: float) -> None:
        ...
    
    @overload
    def rotate_transform(self, angle: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        ...
    
    def clone(self) -> object:
        ...
    
    def set_line_cap(self, start_cap: aspose.pydrawing.Drawing2D.LineCap, end_cap: aspose.pydrawing.Drawing2D.LineCap, dash_cap: aspose.pydrawing.Drawing2D.DashCap) -> None:
        ...
    
    def reset_transform(self) -> None:
        ...
    
    @property
    def width(self) -> float:
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def start_cap(self) -> aspose.pydrawing.Drawing2D.LineCap:
        ...
    
    @start_cap.setter
    def start_cap(self, value: aspose.pydrawing.Drawing2D.LineCap):
        ...
    
    @property
    def end_cap(self) -> aspose.pydrawing.Drawing2D.LineCap:
        ...
    
    @end_cap.setter
    def end_cap(self, value: aspose.pydrawing.Drawing2D.LineCap):
        ...
    
    @property
    def dash_cap(self) -> aspose.pydrawing.Drawing2D.DashCap:
        ...
    
    @dash_cap.setter
    def dash_cap(self, value: aspose.pydrawing.Drawing2D.DashCap):
        ...
    
    @property
    def line_join(self) -> aspose.pydrawing.Drawing2D.LineJoin:
        ...
    
    @line_join.setter
    def line_join(self, value: aspose.pydrawing.Drawing2D.LineJoin):
        ...
    
    @property
    def miter_limit(self) -> float:
        ...
    
    @miter_limit.setter
    def miter_limit(self, value: float):
        ...
    
    @property
    def alignment(self) -> aspose.pydrawing.Drawing2D.PenAlignment:
        ...
    
    @alignment.setter
    def alignment(self, value: aspose.pydrawing.Drawing2D.PenAlignment):
        ...
    
    @property
    def transform(self) -> aspose.pydrawing.Drawing2D.Matrix:
        ...
    
    @transform.setter
    def transform(self, value: aspose.pydrawing.Drawing2D.Matrix):
        ...
    
    @property
    def pen_type(self) -> aspose.pydrawing.Drawing2D.PenType:
        ...
    
    @property
    def color(self) -> aspose.pydrawing.Color:
        ...
    
    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def brush(self) -> aspose.pydrawing.Brush:
        ...
    
    @brush.setter
    def brush(self, value: aspose.pydrawing.Brush):
        ...
    
    @property
    def dash_style(self) -> aspose.pydrawing.Drawing2D.DashStyle:
        ...
    
    @dash_style.setter
    def dash_style(self, value: aspose.pydrawing.Drawing2D.DashStyle):
        ...
    
    @property
    def dash_offset(self) -> float:
        ...
    
    @dash_offset.setter
    def dash_offset(self, value: float):
        ...
    
    @property
    def dash_pattern(self) -> list[float]:
        ...
    
    @dash_pattern.setter
    def dash_pattern(self, value: list[float]):
        ...
    
    @property
    def compound_array(self) -> list[float]:
        ...
    
    @compound_array.setter
    def compound_array(self, value: list[float]):
        ...
    
    @property
    def custom_start_cap(self) -> aspose.pydrawing.Drawing2D.CustomLineCap:
        ...
    
    @custom_start_cap.setter
    def custom_start_cap(self, value: aspose.pydrawing.Drawing2D.CustomLineCap):
        ...
    
    @property
    def custom_end_cap(self) -> aspose.pydrawing.Drawing2D.CustomLineCap:
        ...
    
    @custom_end_cap.setter
    def custom_end_cap(self, value: aspose.pydrawing.Drawing2D.CustomLineCap):
        ...
    
    ...

class Pens:
    
    transparent: aspose.pydrawing.Pen
    
    alice_blue: aspose.pydrawing.Pen
    
    antique_white: aspose.pydrawing.Pen
    
    aqua: aspose.pydrawing.Pen
    
    aquamarine: aspose.pydrawing.Pen
    
    azure: aspose.pydrawing.Pen
    
    beige: aspose.pydrawing.Pen
    
    bisque: aspose.pydrawing.Pen
    
    black: aspose.pydrawing.Pen
    
    blanched_almond: aspose.pydrawing.Pen
    
    blue: aspose.pydrawing.Pen
    
    blue_violet: aspose.pydrawing.Pen
    
    brown: aspose.pydrawing.Pen
    
    burly_wood: aspose.pydrawing.Pen
    
    cadet_blue: aspose.pydrawing.Pen
    
    chartreuse: aspose.pydrawing.Pen
    
    chocolate: aspose.pydrawing.Pen
    
    coral: aspose.pydrawing.Pen
    
    cornflower_blue: aspose.pydrawing.Pen
    
    cornsilk: aspose.pydrawing.Pen
    
    crimson: aspose.pydrawing.Pen
    
    cyan: aspose.pydrawing.Pen
    
    dark_blue: aspose.pydrawing.Pen
    
    dark_cyan: aspose.pydrawing.Pen
    
    dark_goldenrod: aspose.pydrawing.Pen
    
    dark_gray: aspose.pydrawing.Pen
    
    dark_green: aspose.pydrawing.Pen
    
    dark_khaki: aspose.pydrawing.Pen
    
    dark_magenta: aspose.pydrawing.Pen
    
    dark_olive_green: aspose.pydrawing.Pen
    
    dark_orange: aspose.pydrawing.Pen
    
    dark_orchid: aspose.pydrawing.Pen
    
    dark_red: aspose.pydrawing.Pen
    
    dark_salmon: aspose.pydrawing.Pen
    
    dark_sea_green: aspose.pydrawing.Pen
    
    dark_slate_blue: aspose.pydrawing.Pen
    
    dark_slate_gray: aspose.pydrawing.Pen
    
    dark_turquoise: aspose.pydrawing.Pen
    
    dark_violet: aspose.pydrawing.Pen
    
    deep_pink: aspose.pydrawing.Pen
    
    deep_sky_blue: aspose.pydrawing.Pen
    
    dim_gray: aspose.pydrawing.Pen
    
    dodger_blue: aspose.pydrawing.Pen
    
    firebrick: aspose.pydrawing.Pen
    
    floral_white: aspose.pydrawing.Pen
    
    forest_green: aspose.pydrawing.Pen
    
    fuchsia: aspose.pydrawing.Pen
    
    gainsboro: aspose.pydrawing.Pen
    
    ghost_white: aspose.pydrawing.Pen
    
    gold: aspose.pydrawing.Pen
    
    goldenrod: aspose.pydrawing.Pen
    
    gray: aspose.pydrawing.Pen
    
    green: aspose.pydrawing.Pen
    
    green_yellow: aspose.pydrawing.Pen
    
    honeydew: aspose.pydrawing.Pen
    
    hot_pink: aspose.pydrawing.Pen
    
    indian_red: aspose.pydrawing.Pen
    
    indigo: aspose.pydrawing.Pen
    
    ivory: aspose.pydrawing.Pen
    
    khaki: aspose.pydrawing.Pen
    
    lavender: aspose.pydrawing.Pen
    
    lavender_blush: aspose.pydrawing.Pen
    
    lawn_green: aspose.pydrawing.Pen
    
    lemon_chiffon: aspose.pydrawing.Pen
    
    light_blue: aspose.pydrawing.Pen
    
    light_coral: aspose.pydrawing.Pen
    
    light_cyan: aspose.pydrawing.Pen
    
    light_goldenrod_yellow: aspose.pydrawing.Pen
    
    light_green: aspose.pydrawing.Pen
    
    light_gray: aspose.pydrawing.Pen
    
    light_pink: aspose.pydrawing.Pen
    
    light_salmon: aspose.pydrawing.Pen
    
    light_sea_green: aspose.pydrawing.Pen
    
    light_sky_blue: aspose.pydrawing.Pen
    
    light_slate_gray: aspose.pydrawing.Pen
    
    light_steel_blue: aspose.pydrawing.Pen
    
    light_yellow: aspose.pydrawing.Pen
    
    lime: aspose.pydrawing.Pen
    
    lime_green: aspose.pydrawing.Pen
    
    linen: aspose.pydrawing.Pen
    
    magenta: aspose.pydrawing.Pen
    
    maroon: aspose.pydrawing.Pen
    
    medium_aquamarine: aspose.pydrawing.Pen
    
    medium_blue: aspose.pydrawing.Pen
    
    medium_orchid: aspose.pydrawing.Pen
    
    medium_purple: aspose.pydrawing.Pen
    
    medium_sea_green: aspose.pydrawing.Pen
    
    medium_slate_blue: aspose.pydrawing.Pen
    
    medium_spring_green: aspose.pydrawing.Pen
    
    medium_turquoise: aspose.pydrawing.Pen
    
    medium_violet_red: aspose.pydrawing.Pen
    
    midnight_blue: aspose.pydrawing.Pen
    
    mint_cream: aspose.pydrawing.Pen
    
    misty_rose: aspose.pydrawing.Pen
    
    moccasin: aspose.pydrawing.Pen
    
    navajo_white: aspose.pydrawing.Pen
    
    navy: aspose.pydrawing.Pen
    
    old_lace: aspose.pydrawing.Pen
    
    olive: aspose.pydrawing.Pen
    
    olive_drab: aspose.pydrawing.Pen
    
    orange: aspose.pydrawing.Pen
    
    orange_red: aspose.pydrawing.Pen
    
    orchid: aspose.pydrawing.Pen
    
    pale_goldenrod: aspose.pydrawing.Pen
    
    pale_green: aspose.pydrawing.Pen
    
    pale_turquoise: aspose.pydrawing.Pen
    
    pale_violet_red: aspose.pydrawing.Pen
    
    papaya_whip: aspose.pydrawing.Pen
    
    peach_puff: aspose.pydrawing.Pen
    
    peru: aspose.pydrawing.Pen
    
    pink: aspose.pydrawing.Pen
    
    plum: aspose.pydrawing.Pen
    
    powder_blue: aspose.pydrawing.Pen
    
    purple: aspose.pydrawing.Pen
    
    red: aspose.pydrawing.Pen
    
    rosy_brown: aspose.pydrawing.Pen
    
    royal_blue: aspose.pydrawing.Pen
    
    saddle_brown: aspose.pydrawing.Pen
    
    salmon: aspose.pydrawing.Pen
    
    sandy_brown: aspose.pydrawing.Pen
    
    sea_green: aspose.pydrawing.Pen
    
    sea_shell: aspose.pydrawing.Pen
    
    sienna: aspose.pydrawing.Pen
    
    silver: aspose.pydrawing.Pen
    
    sky_blue: aspose.pydrawing.Pen
    
    slate_blue: aspose.pydrawing.Pen
    
    slate_gray: aspose.pydrawing.Pen
    
    snow: aspose.pydrawing.Pen
    
    spring_green: aspose.pydrawing.Pen
    
    steel_blue: aspose.pydrawing.Pen
    
    tan: aspose.pydrawing.Pen
    
    teal: aspose.pydrawing.Pen
    
    thistle: aspose.pydrawing.Pen
    
    tomato: aspose.pydrawing.Pen
    
    turquoise: aspose.pydrawing.Pen
    
    violet: aspose.pydrawing.Pen
    
    wheat: aspose.pydrawing.Pen
    
    white: aspose.pydrawing.Pen
    
    white_smoke: aspose.pydrawing.Pen
    
    yellow: aspose.pydrawing.Pen
    
    yellow_green: aspose.pydrawing.Pen
    
    ...

class StringFormat:
    
    @overload
    def __init__(self):
        ...
    
    @overload
    def __init__(self, options: aspose.pydrawing.StringFormatFlags):
        ...
    
    @overload
    def __init__(self, options: aspose.pydrawing.StringFormatFlags, language: int):
        ...
    
    @overload
    def __init__(self, format: aspose.pydrawing.StringFormat):
        ...
    
    def clone(self) -> object:
        ...
    
    def set_measurable_character_ranges(self, ranges: list[aspose.pydrawing.CharacterRange]) -> None:
        ...
    
    def set_tab_stops(self, first_tab_offset: float, tab_stops: list[float]) -> None:
        ...
    
    def get_tab_stops(self, first_tab_offset: float) -> list[float]:
        ...
    
    def set_digit_substitution(self, language: int, substitute: aspose.pydrawing.StringDigitSubstitute) -> None:
        ...
    
    @property
    def format_flags(self) -> aspose.pydrawing.StringFormatFlags:
        ...
    
    @format_flags.setter
    def format_flags(self, value: aspose.pydrawing.StringFormatFlags):
        ...
    
    @property
    def alignment(self) -> aspose.pydrawing.StringAlignment:
        ...
    
    @alignment.setter
    def alignment(self, value: aspose.pydrawing.StringAlignment):
        ...
    
    @property
    def line_alignment(self) -> aspose.pydrawing.StringAlignment:
        ...
    
    @line_alignment.setter
    def line_alignment(self, value: aspose.pydrawing.StringAlignment):
        ...
    
    @property
    def hotkey_prefix(self) -> aspose.pydrawing.Text.HotkeyPrefix:
        ...
    
    @hotkey_prefix.setter
    def hotkey_prefix(self, value: aspose.pydrawing.Text.HotkeyPrefix):
        ...
    
    @property
    def trimming(self) -> aspose.pydrawing.StringTrimming:
        ...
    
    @trimming.setter
    def trimming(self, value: aspose.pydrawing.StringTrimming):
        ...
    
    generic_default: aspose.pydrawing.StringFormat
    
    generic_typographic: aspose.pydrawing.StringFormat
    
    @property
    def digit_substitution_method(self) -> aspose.pydrawing.StringDigitSubstitute:
        ...
    
    @property
    def digit_substitution_language(self) -> int:
        ...
    
    ...

class SystemFonts:
    
    @staticmethod
    def get_font_by_name(system_font_name: str) -> aspose.pydrawing.Font:
        ...
    
    caption_font: aspose.pydrawing.Font
    
    small_caption_font: aspose.pydrawing.Font
    
    menu_font: aspose.pydrawing.Font
    
    status_font: aspose.pydrawing.Font
    
    message_box_font: aspose.pydrawing.Font
    
    icon_title_font: aspose.pydrawing.Font
    
    default_font: aspose.pydrawing.Font
    
    dialog_font: aspose.pydrawing.Font
    
    ...

class SystemPens:
    
    @staticmethod
    def from_system_color(c: aspose.pydrawing.Color) -> aspose.pydrawing.Pen:
        ...
    
    active_border: aspose.pydrawing.Pen
    
    active_caption: aspose.pydrawing.Pen
    
    active_caption_text: aspose.pydrawing.Pen
    
    app_workspace: aspose.pydrawing.Pen
    
    button_face: aspose.pydrawing.Pen
    
    button_highlight: aspose.pydrawing.Pen
    
    button_shadow: aspose.pydrawing.Pen
    
    control: aspose.pydrawing.Pen
    
    control_text: aspose.pydrawing.Pen
    
    control_dark: aspose.pydrawing.Pen
    
    control_dark_dark: aspose.pydrawing.Pen
    
    control_light: aspose.pydrawing.Pen
    
    control_light_light: aspose.pydrawing.Pen
    
    desktop: aspose.pydrawing.Pen
    
    gradient_active_caption: aspose.pydrawing.Pen
    
    gradient_inactive_caption: aspose.pydrawing.Pen
    
    gray_text: aspose.pydrawing.Pen
    
    highlight: aspose.pydrawing.Pen
    
    highlight_text: aspose.pydrawing.Pen
    
    hot_track: aspose.pydrawing.Pen
    
    inactive_border: aspose.pydrawing.Pen
    
    inactive_caption: aspose.pydrawing.Pen
    
    inactive_caption_text: aspose.pydrawing.Pen
    
    info: aspose.pydrawing.Pen
    
    info_text: aspose.pydrawing.Pen
    
    menu: aspose.pydrawing.Pen
    
    menu_bar: aspose.pydrawing.Pen
    
    menu_highlight: aspose.pydrawing.Pen
    
    menu_text: aspose.pydrawing.Pen
    
    scroll_bar: aspose.pydrawing.Pen
    
    window: aspose.pydrawing.Pen
    
    window_frame: aspose.pydrawing.Pen
    
    window_text: aspose.pydrawing.Pen
    
    ...

class Region:
    
    @overload
    def __init__(self):
        ...
    
    @overload
    def __init__(self, rect: aspose.pydrawing.RectangleF):
        ...
    
    @overload
    def __init__(self, rect: aspose.pydrawing.Rectangle):
        ...
    
    @overload
    def __init__(self, path: aspose.pydrawing.Drawing2D.GraphicsPath):
        ...
    
    @overload
    def __init__(self, rgn_data: aspose.pydrawing.Drawing2D.RegionData):
        ...
    
    @overload
    def intersect(self, rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def intersect(self, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def intersect(self, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        ...
    
    @overload
    def intersect(self, region: aspose.pydrawing.Region) -> None:
        ...
    
    @overload
    def union(self, rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def union(self, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def union(self, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        ...
    
    @overload
    def union(self, region: aspose.pydrawing.Region) -> None:
        ...
    
    @overload
    def xor(self, rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def xor(self, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def xor(self, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        ...
    
    @overload
    def xor(self, region: aspose.pydrawing.Region) -> None:
        ...
    
    @overload
    def exclude(self, rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def exclude(self, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def exclude(self, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        ...
    
    @overload
    def exclude(self, region: aspose.pydrawing.Region) -> None:
        ...
    
    @overload
    def complement(self, rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def complement(self, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def complement(self, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        ...
    
    @overload
    def complement(self, region: aspose.pydrawing.Region) -> None:
        ...
    
    @overload
    def translate(self, dx: float, dy: float) -> None:
        ...
    
    @overload
    def translate(self, dx: int, dy: int) -> None:
        ...
    
    @overload
    def is_visible(self, x: float, y: float) -> bool:
        ...
    
    @overload
    def is_visible(self, point: aspose.pydrawing.PointF) -> bool:
        ...
    
    @overload
    def is_visible(self, x: float, y: float, g: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_visible(self, point: aspose.pydrawing.PointF, g: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_visible(self, x: float, y: float, width: float, height: float) -> bool:
        ...
    
    @overload
    def is_visible(self, rect: aspose.pydrawing.RectangleF) -> bool:
        ...
    
    @overload
    def is_visible(self, x: float, y: float, width: float, height: float, g: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_visible(self, rect: aspose.pydrawing.RectangleF, g: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_visible(self, x: int, y: int, g: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_visible(self, point: aspose.pydrawing.Point) -> bool:
        ...
    
    @overload
    def is_visible(self, point: aspose.pydrawing.Point, g: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_visible(self, x: int, y: int, width: int, height: int) -> bool:
        ...
    
    @overload
    def is_visible(self, rect: aspose.pydrawing.Rectangle) -> bool:
        ...
    
    @overload
    def is_visible(self, x: int, y: int, width: int, height: int, g: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_visible(self, rect: aspose.pydrawing.Rectangle, g: aspose.pydrawing.Graphics) -> bool:
        ...
    
    def clone(self) -> aspose.pydrawing.Region:
        ...
    
    def make_infinite(self) -> None:
        ...
    
    def make_empty(self) -> None:
        ...
    
    def transform(self, matrix: aspose.pydrawing.Drawing2D.Matrix) -> None:
        ...
    
    def get_bounds(self, g: aspose.pydrawing.Graphics) -> aspose.pydrawing.RectangleF:
        ...
    
    def is_empty(self, g: aspose.pydrawing.Graphics) -> bool:
        ...
    
    def is_infinite(self, g: aspose.pydrawing.Graphics) -> bool:
        ...
    
    def equals(self, region: aspose.pydrawing.Region, g: aspose.pydrawing.Graphics) -> bool:
        ...
    
    def get_region_data(self) -> aspose.pydrawing.Drawing2D.RegionData:
        ...
    
    def get_region_scans(self, matrix: aspose.pydrawing.Drawing2D.Matrix) -> list[aspose.pydrawing.RectangleF]:
        ...
    
    ...

class Brush:
    
    def clone(self) -> object:
        ...
    
    ...

class Font:
    
    @overload
    def __init__(self, prototype: aspose.pydrawing.Font, new_style: aspose.pydrawing.FontStyle):
        ...
    
    @overload
    def __init__(self, family: aspose.pydrawing.FontFamily, em_size: float, style: aspose.pydrawing.FontStyle, unit: aspose.pydrawing.GraphicsUnit):
        ...
    
    @overload
    def __init__(self, family: aspose.pydrawing.FontFamily, em_size: float, style: aspose.pydrawing.FontStyle, unit: aspose.pydrawing.GraphicsUnit, gdi_char_set: int):
        ...
    
    @overload
    def __init__(self, family: aspose.pydrawing.FontFamily, em_size: float, style: aspose.pydrawing.FontStyle, unit: aspose.pydrawing.GraphicsUnit, gdi_char_set: int, gdi_vertical_font: bool):
        ...
    
    @overload
    def __init__(self, family_name: str, em_size: float, style: aspose.pydrawing.FontStyle, unit: aspose.pydrawing.GraphicsUnit, gdi_char_set: int):
        ...
    
    @overload
    def __init__(self, family_name: str, em_size: float, style: aspose.pydrawing.FontStyle, unit: aspose.pydrawing.GraphicsUnit, gdi_char_set: int, gdi_vertical_font: bool):
        ...
    
    @overload
    def __init__(self, family: aspose.pydrawing.FontFamily, em_size: float, style: aspose.pydrawing.FontStyle):
        ...
    
    @overload
    def __init__(self, family: aspose.pydrawing.FontFamily, em_size: float, unit: aspose.pydrawing.GraphicsUnit):
        ...
    
    @overload
    def __init__(self, family: aspose.pydrawing.FontFamily, em_size: float):
        ...
    
    @overload
    def __init__(self, family_name: str, em_size: float, style: aspose.pydrawing.FontStyle, unit: aspose.pydrawing.GraphicsUnit):
        ...
    
    @overload
    def __init__(self, family_name: str, em_size: float, style: aspose.pydrawing.FontStyle):
        ...
    
    @overload
    def __init__(self, family_name: str, em_size: float, unit: aspose.pydrawing.GraphicsUnit):
        ...
    
    @overload
    def __init__(self, family_name: str, em_size: float):
        ...
    
    @overload
    def get_height(self, graphics: aspose.pydrawing.Graphics) -> float:
        ...
    
    @overload
    def get_height(self, dpi: float) -> float:
        ...
    
    @overload
    def get_height(self) -> float:
        ...
    
    @overload
    def to_log_font(self, log_font: object, graphics: aspose.pydrawing.Graphics) -> None:
        ...
    
    @overload
    def to_log_font(self, log_font: object) -> None:
        ...
    
    @staticmethod
    def from_log_font(lf: object) -> aspose.pydrawing.Font:
        ...
    
    def clone(self) -> object:
        ...
    
    @property
    def size(self) -> float:
        ...
    
    @property
    def style(self) -> aspose.pydrawing.FontStyle:
        ...
    
    @property
    def bold(self) -> bool:
        ...
    
    @property
    def italic(self) -> bool:
        ...
    
    @property
    def strikeout(self) -> bool:
        ...
    
    @property
    def underline(self) -> bool:
        ...
    
    @property
    def font_family(self) -> aspose.pydrawing.FontFamily:
        ...
    
    @property
    def name(self) -> str:
        ...
    
    @property
    def unit(self) -> aspose.pydrawing.GraphicsUnit:
        ...
    
    @property
    def gdi_char_set(self) -> int:
        ...
    
    @property
    def gdi_vertical_font(self) -> bool:
        ...
    
    @property
    def original_font_name(self) -> str:
        ...
    
    @property
    def system_font_name(self) -> str:
        ...
    
    @property
    def is_system_font(self) -> bool:
        ...
    
    @property
    def height(self) -> int:
        ...
    
    @property
    def size_in_points(self) -> float:
        ...
    
    ...

class FontConverter:
    
    def __init__(self):
        ...
    
    ...

class FontFamily:
    
    @overload
    def __init__(self, name: str):
        ...
    
    @overload
    def __init__(self, name: str, font_collection: aspose.pydrawing.Text.FontCollection):
        ...
    
    @overload
    def __init__(self, generic_family: aspose.pydrawing.Text.GenericFontFamilies):
        ...
    
    def get_name(self, language: int) -> str:
        ...
    
    @staticmethod
    def get_families(graphics: aspose.pydrawing.Graphics) -> list[aspose.pydrawing.FontFamily]:
        ...
    
    def is_style_available(self, style: aspose.pydrawing.FontStyle) -> bool:
        ...
    
    def get_em_height(self, style: aspose.pydrawing.FontStyle) -> int:
        ...
    
    def get_cell_ascent(self, style: aspose.pydrawing.FontStyle) -> int:
        ...
    
    def get_cell_descent(self, style: aspose.pydrawing.FontStyle) -> int:
        ...
    
    def get_line_spacing(self, style: aspose.pydrawing.FontStyle) -> int:
        ...
    
    @property
    def name(self) -> str:
        ...
    
    families: list[aspose.pydrawing.FontFamily]
    
    generic_sans_serif: aspose.pydrawing.FontFamily
    
    generic_serif: aspose.pydrawing.FontFamily
    
    generic_monospace: aspose.pydrawing.FontFamily
    
    ...

class SolidBrush:
    
    def __init__(self, color: aspose.pydrawing.Color):
        ...
    
    def clone(self) -> object:
        ...
    
    @property
    def color(self) -> aspose.pydrawing.Color:
        ...
    
    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...
    
    ...

class SystemBrushes:
    
    @staticmethod
    def from_system_color(c: aspose.pydrawing.Color) -> aspose.pydrawing.Brush:
        ...
    
    active_border: aspose.pydrawing.Brush
    
    active_caption: aspose.pydrawing.Brush
    
    active_caption_text: aspose.pydrawing.Brush
    
    app_workspace: aspose.pydrawing.Brush
    
    button_face: aspose.pydrawing.Brush
    
    button_highlight: aspose.pydrawing.Brush
    
    button_shadow: aspose.pydrawing.Brush
    
    control: aspose.pydrawing.Brush
    
    control_light_light: aspose.pydrawing.Brush
    
    control_light: aspose.pydrawing.Brush
    
    control_dark: aspose.pydrawing.Brush
    
    control_dark_dark: aspose.pydrawing.Brush
    
    control_text: aspose.pydrawing.Brush
    
    desktop: aspose.pydrawing.Brush
    
    gradient_active_caption: aspose.pydrawing.Brush
    
    gradient_inactive_caption: aspose.pydrawing.Brush
    
    gray_text: aspose.pydrawing.Brush
    
    highlight: aspose.pydrawing.Brush
    
    highlight_text: aspose.pydrawing.Brush
    
    hot_track: aspose.pydrawing.Brush
    
    inactive_caption: aspose.pydrawing.Brush
    
    inactive_border: aspose.pydrawing.Brush
    
    inactive_caption_text: aspose.pydrawing.Brush
    
    info: aspose.pydrawing.Brush
    
    info_text: aspose.pydrawing.Brush
    
    menu: aspose.pydrawing.Brush
    
    menu_bar: aspose.pydrawing.Brush
    
    menu_highlight: aspose.pydrawing.Brush
    
    menu_text: aspose.pydrawing.Brush
    
    scroll_bar: aspose.pydrawing.Brush
    
    window: aspose.pydrawing.Brush
    
    window_frame: aspose.pydrawing.Brush
    
    window_text: aspose.pydrawing.Brush
    
    ...

class TextureBrush:
    
    @overload
    def __init__(self, bitmap: aspose.pydrawing.Image):
        ...
    
    @overload
    def __init__(self, image: aspose.pydrawing.Image, wrap_mode: aspose.pydrawing.Drawing2D.WrapMode):
        ...
    
    @overload
    def __init__(self, image: aspose.pydrawing.Image, wrap_mode: aspose.pydrawing.Drawing2D.WrapMode, dst_rect: aspose.pydrawing.RectangleF):
        ...
    
    @overload
    def __init__(self, image: aspose.pydrawing.Image, wrap_mode: aspose.pydrawing.Drawing2D.WrapMode, dst_rect: aspose.pydrawing.Rectangle):
        ...
    
    @overload
    def __init__(self, image: aspose.pydrawing.Image, dst_rect: aspose.pydrawing.RectangleF):
        ...
    
    @overload
    def __init__(self, image: aspose.pydrawing.Image, dst_rect: aspose.pydrawing.RectangleF, image_attr: aspose.pydrawing.Imaging.ImageAttributes):
        ...
    
    @overload
    def __init__(self, image: aspose.pydrawing.Image, dst_rect: aspose.pydrawing.Rectangle):
        ...
    
    @overload
    def __init__(self, image: aspose.pydrawing.Image, dst_rect: aspose.pydrawing.Rectangle, image_attr: aspose.pydrawing.Imaging.ImageAttributes):
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.Drawing2D.Matrix) -> None:
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.Drawing2D.Matrix, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float) -> None:
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float) -> None:
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        ...
    
    @overload
    def rotate_transform(self, angle: float) -> None:
        ...
    
    @overload
    def rotate_transform(self, angle: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        ...
    
    def clone(self) -> object:
        ...
    
    def reset_transform(self) -> None:
        ...
    
    @property
    def transform(self) -> aspose.pydrawing.Drawing2D.Matrix:
        ...
    
    @transform.setter
    def transform(self, value: aspose.pydrawing.Drawing2D.Matrix):
        ...
    
    @property
    def wrap_mode(self) -> aspose.pydrawing.Drawing2D.WrapMode:
        ...
    
    @wrap_mode.setter
    def wrap_mode(self, value: aspose.pydrawing.Drawing2D.WrapMode):
        ...
    
    @property
    def image(self) -> aspose.pydrawing.Image:
        ...
    
    ...

class BufferedGraphicsManager:
    
    current: aspose.pydrawing.BufferedGraphicsContext
    
    ...

class Icon:
    
    @overload
    def __init__(self, file_name: str):
        ...
    
    @overload
    def __init__(self, file_name: str, size: aspose.pydrawing.Size):
        ...
    
    @overload
    def __init__(self, file_name: str, width: int, height: int):
        ...
    
    @overload
    def __init__(self, original: aspose.pydrawing.Icon, size: aspose.pydrawing.Size):
        ...
    
    @overload
    def __init__(self, original: aspose.pydrawing.Icon, width: int, height: int):
        ...
    
    @overload
    def __init__(self, type: object, resource: str):
        ...
    
    @overload
    def __init__(self, stream: io.BytesIO):
        ...
    
    @overload
    def __init__(self, stream: io.BytesIO, size: aspose.pydrawing.Size):
        ...
    
    @overload
    def __init__(self, stream: io.BytesIO, width: int, height: int):
        ...
    
    @staticmethod
    def extract_associated_icon(file_path: str) -> aspose.pydrawing.Icon:
        ...
    
    def clone(self) -> object:
        ...
    
    def save(self, output_stream: io.BytesIO) -> None:
        ...
    
    def to_bitmap(self) -> aspose.pydrawing.Bitmap:
        ...
    
    @property
    def height(self) -> int:
        ...
    
    @property
    def size(self) -> aspose.pydrawing.Size:
        ...
    
    @property
    def width(self) -> int:
        ...
    
    ...

class ImageAnimator:
    
    @overload
    @staticmethod
    def update_frames(image: aspose.pydrawing.Image) -> None:
        ...
    
    @overload
    @staticmethod
    def update_frames() -> None:
        ...
    
    @staticmethod
    def can_animate(image: aspose.pydrawing.Image) -> bool:
        ...
    
    ...

class SystemIcons:
    
    application: aspose.pydrawing.Icon
    
    asterisk: aspose.pydrawing.Icon
    
    error: aspose.pydrawing.Icon
    
    exclamation: aspose.pydrawing.Icon
    
    hand: aspose.pydrawing.Icon
    
    information: aspose.pydrawing.Icon
    
    question: aspose.pydrawing.Icon
    
    warning: aspose.pydrawing.Icon
    
    win_logo: aspose.pydrawing.Icon
    
    shield: aspose.pydrawing.Icon
    
    ...

class ToolboxBitmapAttribute:
    
    @overload
    def __init__(self, image_file: str):
        ...
    
    @overload
    def __init__(self, t: object):
        ...
    
    @overload
    def __init__(self, t: object, name: str):
        ...
    
    @overload
    def get_image(self, component: object) -> aspose.pydrawing.Image:
        ...
    
    @overload
    def get_image(self, component: object, large: bool) -> aspose.pydrawing.Image:
        ...
    
    @overload
    def get_image(self, type: object) -> aspose.pydrawing.Image:
        ...
    
    @overload
    def get_image(self, type: object, large: bool) -> aspose.pydrawing.Image:
        ...
    
    @overload
    def get_image(self, type: object, img_name: str, large: bool) -> aspose.pydrawing.Image:
        ...
    
    @staticmethod
    def get_image_from_resource(t: object, image_name: str, large: bool) -> aspose.pydrawing.Image:
        ...
    
    DEFAULT: aspose.pydrawing.ToolboxBitmapAttribute
    
    ...

class ColorTranslator:
    
    @staticmethod
    def to_win32(c: aspose.pydrawing.Color) -> int:
        ...
    
    @staticmethod
    def to_ole(c: aspose.pydrawing.Color) -> int:
        ...
    
    @staticmethod
    def from_ole(ole_color: int) -> aspose.pydrawing.Color:
        ...
    
    @staticmethod
    def from_win32(win_32_color: int) -> aspose.pydrawing.Color:
        ...
    
    @staticmethod
    def from_html(html_color: str) -> aspose.pydrawing.Color:
        ...
    
    @staticmethod
    def to_html(c: aspose.pydrawing.Color) -> str:
        ...
    
    ...

class SystemColors:
    
    active_border: aspose.pydrawing.Color
    
    active_caption: aspose.pydrawing.Color
    
    active_caption_text: aspose.pydrawing.Color
    
    app_workspace: aspose.pydrawing.Color
    
    button_face: aspose.pydrawing.Color
    
    button_highlight: aspose.pydrawing.Color
    
    button_shadow: aspose.pydrawing.Color
    
    control: aspose.pydrawing.Color
    
    control_dark: aspose.pydrawing.Color
    
    control_dark_dark: aspose.pydrawing.Color
    
    control_light: aspose.pydrawing.Color
    
    control_light_light: aspose.pydrawing.Color
    
    control_text: aspose.pydrawing.Color
    
    desktop: aspose.pydrawing.Color
    
    gradient_active_caption: aspose.pydrawing.Color
    
    gradient_inactive_caption: aspose.pydrawing.Color
    
    gray_text: aspose.pydrawing.Color
    
    highlight: aspose.pydrawing.Color
    
    highlight_text: aspose.pydrawing.Color
    
    hot_track: aspose.pydrawing.Color
    
    inactive_border: aspose.pydrawing.Color
    
    inactive_caption: aspose.pydrawing.Color
    
    inactive_caption_text: aspose.pydrawing.Color
    
    info: aspose.pydrawing.Color
    
    info_text: aspose.pydrawing.Color
    
    menu: aspose.pydrawing.Color
    
    menu_bar: aspose.pydrawing.Color
    
    menu_highlight: aspose.pydrawing.Color
    
    menu_text: aspose.pydrawing.Color
    
    scroll_bar: aspose.pydrawing.Color
    
    window: aspose.pydrawing.Color
    
    window_frame: aspose.pydrawing.Color
    
    window_text: aspose.pydrawing.Color
    
    ...

class ContentAlignment(Enum):
    
    TOP_LEFT: int
    
    TOP_CENTER: int
    
    TOP_RIGHT: int
    
    MIDDLE_LEFT: int
    
    MIDDLE_CENTER: int
    
    MIDDLE_RIGHT: int
    
    BOTTOM_LEFT: int
    
    BOTTOM_CENTER: int
    
    BOTTOM_RIGHT: int
    

class GraphicsUnit(Enum):
    
    WORLD: int
    
    DISPLAY: int
    
    PIXEL: int
    
    POINT: int
    
    INCH: int
    
    DOCUMENT: int
    
    MILLIMETER: int
    

class RotateFlipType(Enum):
    
    ROTATE_NONE_FLIP_NONE: int
    
    ROTATE_90_FLIP_NONE: int
    
    ROTATE_180_FLIP_NONE: int
    
    ROTATE_270_FLIP_NONE: int
    
    ROTATE_NONE_FLIP_X: int
    
    ROTATE_90_FLIP_X: int
    
    ROTATE_180_FLIP_X: int
    
    ROTATE_270_FLIP_X: int
    
    ROTATE_NONE_FLIP_Y: int
    
    ROTATE_90_FLIP_Y: int
    
    ROTATE_180_FLIP_Y: int
    
    ROTATE_270_FLIP_Y: int
    
    ROTATE_NONE_FLIP_XY: int
    
    ROTATE_90_FLIP_XY: int
    
    ROTATE_180_FLIP_XY: int
    
    ROTATE_270_FLIP_XY: int
    

class CopyPixelOperation(Enum):
    
    BLACKNESS: int
    
    CAPTURE_BLT: int
    
    DESTINATION_INVERT: int
    
    MERGE_COPY: int
    
    MERGE_PAINT: int
    
    NO_MIRROR_BITMAP: int
    
    NOT_SOURCE_COPY: int
    
    NOT_SOURCE_ERASE: int
    
    PAT_COPY: int
    
    PAT_INVERT: int
    
    PAT_PAINT: int
    
    SOURCE_AND: int
    
    SOURCE_COPY: int
    
    SOURCE_ERASE: int
    
    SOURCE_INVERT: int
    
    SOURCE_PAINT: int
    
    WHITENESS: int
    

class FontStyle(Enum):
    
    REGULAR: int
    
    BOLD: int
    
    ITALIC: int
    
    UNDERLINE: int
    
    STRIKEOUT: int
    

class StringAlignment(Enum):
    
    NEAR: int
    
    CENTER: int
    
    FAR: int
    

class StringDigitSubstitute(Enum):
    
    USER: int
    
    NONE: int
    
    NATIONAL: int
    
    TRADITIONAL: int
    

class StringFormatFlags(Enum):
    
    DIRECTION_RIGHT_TO_LEFT: int
    
    DIRECTION_VERTICAL: int
    
    FIT_BLACK_BOX: int
    
    DISPLAY_FORMAT_CONTROL: int
    
    NO_FONT_FALLBACK: int
    
    MEASURE_TRAILING_SPACES: int
    
    NO_WRAP: int
    
    LINE_LIMIT: int
    
    NO_CLIP: int
    

class StringTrimming(Enum):
    
    NONE: int
    
    CHARACTER: int
    
    WORD: int
    
    ELLIPSIS_CHARACTER: int
    
    ELLIPSIS_WORD: int
    
    ELLIPSIS_PATH: int
    

class StringUnit(Enum):
    
    WORLD: int
    
    DISPLAY: int
    
    PIXEL: int
    
    POINT: int
    
    INCH: int
    
    DOCUMENT: int
    
    MILLIMETER: int
    
    EM: int
    

class KnownColor(Enum):
    
    ACTIVE_BORDER: int
    
    ACTIVE_CAPTION: int
    
    ACTIVE_CAPTION_TEXT: int
    
    APP_WORKSPACE: int
    
    CONTROL: int
    
    CONTROL_DARK: int
    
    CONTROL_DARK_DARK: int
    
    CONTROL_LIGHT: int
    
    CONTROL_LIGHT_LIGHT: int
    
    CONTROL_TEXT: int
    
    DESKTOP: int
    
    GRAY_TEXT: int
    
    HIGHLIGHT: int
    
    HIGHLIGHT_TEXT: int
    
    HOT_TRACK: int
    
    INACTIVE_BORDER: int
    
    INACTIVE_CAPTION: int
    
    INACTIVE_CAPTION_TEXT: int
    
    INFO: int
    
    INFO_TEXT: int
    
    MENU: int
    
    MENU_TEXT: int
    
    SCROLL_BAR: int
    
    WINDOW: int
    
    WINDOW_FRAME: int
    
    WINDOW_TEXT: int
    
    TRANSPARENT: int
    
    ALICE_BLUE: int
    
    ANTIQUE_WHITE: int
    
    AQUA: int
    
    AQUAMARINE: int
    
    AZURE: int
    
    BEIGE: int
    
    BISQUE: int
    
    BLACK: int
    
    BLANCHED_ALMOND: int
    
    BLUE: int
    
    BLUE_VIOLET: int
    
    BROWN: int
    
    BURLY_WOOD: int
    
    CADET_BLUE: int
    
    CHARTREUSE: int
    
    CHOCOLATE: int
    
    CORAL: int
    
    CORNFLOWER_BLUE: int
    
    CORNSILK: int
    
    CRIMSON: int
    
    CYAN: int
    
    DARK_BLUE: int
    
    DARK_CYAN: int
    
    DARK_GOLDENROD: int
    
    DARK_GRAY: int
    
    DARK_GREEN: int
    
    DARK_KHAKI: int
    
    DARK_MAGENTA: int
    
    DARK_OLIVE_GREEN: int
    
    DARK_ORANGE: int
    
    DARK_ORCHID: int
    
    DARK_RED: int
    
    DARK_SALMON: int
    
    DARK_SEA_GREEN: int
    
    DARK_SLATE_BLUE: int
    
    DARK_SLATE_GRAY: int
    
    DARK_TURQUOISE: int
    
    DARK_VIOLET: int
    
    DEEP_PINK: int
    
    DEEP_SKY_BLUE: int
    
    DIM_GRAY: int
    
    DODGER_BLUE: int
    
    FIREBRICK: int
    
    FLORAL_WHITE: int
    
    FOREST_GREEN: int
    
    FUCHSIA: int
    
    GAINSBORO: int
    
    GHOST_WHITE: int
    
    GOLD: int
    
    GOLDENROD: int
    
    GRAY: int
    
    GREEN: int
    
    GREEN_YELLOW: int
    
    HONEYDEW: int
    
    HOT_PINK: int
    
    INDIAN_RED: int
    
    INDIGO: int
    
    IVORY: int
    
    KHAKI: int
    
    LAVENDER: int
    
    LAVENDER_BLUSH: int
    
    LAWN_GREEN: int
    
    LEMON_CHIFFON: int
    
    LIGHT_BLUE: int
    
    LIGHT_CORAL: int
    
    LIGHT_CYAN: int
    
    LIGHT_GOLDENROD_YELLOW: int
    
    LIGHT_GRAY: int
    
    LIGHT_GREEN: int
    
    LIGHT_PINK: int
    
    LIGHT_SALMON: int
    
    LIGHT_SEA_GREEN: int
    
    LIGHT_SKY_BLUE: int
    
    LIGHT_SLATE_GRAY: int
    
    LIGHT_STEEL_BLUE: int
    
    LIGHT_YELLOW: int
    
    LIME: int
    
    LIME_GREEN: int
    
    LINEN: int
    
    MAGENTA: int
    
    MAROON: int
    
    MEDIUM_AQUAMARINE: int
    
    MEDIUM_BLUE: int
    
    MEDIUM_ORCHID: int
    
    MEDIUM_PURPLE: int
    
    MEDIUM_SEA_GREEN: int
    
    MEDIUM_SLATE_BLUE: int
    
    MEDIUM_SPRING_GREEN: int
    
    MEDIUM_TURQUOISE: int
    
    MEDIUM_VIOLET_RED: int
    
    MIDNIGHT_BLUE: int
    
    MINT_CREAM: int
    
    MISTY_ROSE: int
    
    MOCCASIN: int
    
    NAVAJO_WHITE: int
    
    NAVY: int
    
    OLD_LACE: int
    
    OLIVE: int
    
    OLIVE_DRAB: int
    
    ORANGE: int
    
    ORANGE_RED: int
    
    ORCHID: int
    
    PALE_GOLDENROD: int
    
    PALE_GREEN: int
    
    PALE_TURQUOISE: int
    
    PALE_VIOLET_RED: int
    
    PAPAYA_WHIP: int
    
    PEACH_PUFF: int
    
    PERU: int
    
    PINK: int
    
    PLUM: int
    
    POWDER_BLUE: int
    
    PURPLE: int
    
    RED: int
    
    ROSY_BROWN: int
    
    ROYAL_BLUE: int
    
    SADDLE_BROWN: int
    
    SALMON: int
    
    SANDY_BROWN: int
    
    SEA_GREEN: int
    
    SEA_SHELL: int
    
    SIENNA: int
    
    SILVER: int
    
    SKY_BLUE: int
    
    SLATE_BLUE: int
    
    SLATE_GRAY: int
    
    SNOW: int
    
    SPRING_GREEN: int
    
    STEEL_BLUE: int
    
    TAN: int
    
    TEAL: int
    
    THISTLE: int
    
    TOMATO: int
    
    TURQUOISE: int
    
    VIOLET: int
    
    WHEAT: int
    
    WHITE: int
    
    WHITE_SMOKE: int
    
    YELLOW: int
    
    YELLOW_GREEN: int
    
    BUTTON_FACE: int
    
    BUTTON_HIGHLIGHT: int
    
    BUTTON_SHADOW: int
    
    GRADIENT_ACTIVE_CAPTION: int
    
    GRADIENT_INACTIVE_CAPTION: int
    
    MENU_BAR: int
    
    MENU_HIGHLIGHT: int
