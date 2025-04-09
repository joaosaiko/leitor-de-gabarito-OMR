import aspose.pydrawing
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable
from enum import Enum

class Blend:
    
    @overload
    def __init__(self):
        ...
    
    @overload
    def __init__(self, count: int):
        ...
    
    @property
    def factors(self) -> list[float]:
        ...
    
    @factors.setter
    def factors(self, value: list[float]):
        ...
    
    @property
    def positions(self) -> list[float]:
        ...
    
    @positions.setter
    def positions(self, value: list[float]):
        ...
    
    ...

class ColorBlend:
    
    @overload
    def __init__(self):
        ...
    
    @overload
    def __init__(self, count: int):
        ...
    
    @property
    def colors(self) -> list[aspose.pydrawing.Color]:
        ...
    
    @colors.setter
    def colors(self, value: list[aspose.pydrawing.Color]):
        ...
    
    @property
    def positions(self) -> list[float]:
        ...
    
    @positions.setter
    def positions(self, value: list[float]):
        ...
    
    ...

class GraphicsContainer:
    
    ...

class HatchBrush:
    
    @overload
    def __init__(self, hatchstyle: aspose.pydrawing.drawing2d.HatchStyle, fore_color: aspose.pydrawing.Color):
        ...
    
    @overload
    def __init__(self, hatchstyle: aspose.pydrawing.drawing2d.HatchStyle, fore_color: aspose.pydrawing.Color, back_color: aspose.pydrawing.Color):
        ...
    
    def clone(self) -> object:
        ...
    
    @property
    def hatch_style(self) -> aspose.pydrawing.drawing2d.HatchStyle:
        ...
    
    @property
    def foreground_color(self) -> aspose.pydrawing.Color:
        ...
    
    @property
    def background_color(self) -> aspose.pydrawing.Color:
        ...
    
    ...

class LinearGradientBrush:
    
    @overload
    def __init__(self, point1: aspose.pydrawing.PointF, point2: aspose.pydrawing.PointF, color1: aspose.pydrawing.Color, color2: aspose.pydrawing.Color):
        ...
    
    @overload
    def __init__(self, point1: aspose.pydrawing.Point, point2: aspose.pydrawing.Point, color1: aspose.pydrawing.Color, color2: aspose.pydrawing.Color):
        ...
    
    @overload
    def __init__(self, rect: aspose.pydrawing.RectangleF, color1: aspose.pydrawing.Color, color2: aspose.pydrawing.Color, linear_gradient_mode: aspose.pydrawing.drawing2d.LinearGradientMode):
        ...
    
    @overload
    def __init__(self, rect: aspose.pydrawing.Rectangle, color1: aspose.pydrawing.Color, color2: aspose.pydrawing.Color, linear_gradient_mode: aspose.pydrawing.drawing2d.LinearGradientMode):
        ...
    
    @overload
    def __init__(self, rect: aspose.pydrawing.RectangleF, color1: aspose.pydrawing.Color, color2: aspose.pydrawing.Color, angle: float):
        ...
    
    @overload
    def __init__(self, rect: aspose.pydrawing.RectangleF, color1: aspose.pydrawing.Color, color2: aspose.pydrawing.Color, angle: float, is_angle_scaleable: bool):
        ...
    
    @overload
    def __init__(self, rect: aspose.pydrawing.Rectangle, color1: aspose.pydrawing.Color, color2: aspose.pydrawing.Color, angle: float):
        ...
    
    @overload
    def __init__(self, rect: aspose.pydrawing.Rectangle, color1: aspose.pydrawing.Color, color2: aspose.pydrawing.Color, angle: float, is_angle_scaleable: bool):
        ...
    
    @overload
    def set_sigma_bell_shape(self, focus: float) -> None:
        ...
    
    @overload
    def set_sigma_bell_shape(self, focus: float, scale: float) -> None:
        ...
    
    @overload
    def set_blend_triangular_shape(self, focus: float) -> None:
        ...
    
    @overload
    def set_blend_triangular_shape(self, focus: float, scale: float) -> None:
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.drawing2d.Matrix, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float) -> None:
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float) -> None:
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    @overload
    def rotate_transform(self, angle: float) -> None:
        ...
    
    @overload
    def rotate_transform(self, angle: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    def clone(self) -> object:
        ...
    
    def reset_transform(self) -> None:
        ...
    
    @property
    def linear_colors(self) -> list[aspose.pydrawing.Color]:
        ...
    
    @linear_colors.setter
    def linear_colors(self, value: list[aspose.pydrawing.Color]):
        ...
    
    @property
    def rectangle(self) -> aspose.pydrawing.RectangleF:
        ...
    
    @property
    def gamma_correction(self) -> bool:
        ...
    
    @gamma_correction.setter
    def gamma_correction(self, value: bool):
        ...
    
    @property
    def blend(self) -> aspose.pydrawing.drawing2d.Blend:
        ...
    
    @blend.setter
    def blend(self, value: aspose.pydrawing.drawing2d.Blend):
        ...
    
    @property
    def interpolation_colors(self) -> aspose.pydrawing.drawing2d.ColorBlend:
        ...
    
    @interpolation_colors.setter
    def interpolation_colors(self, value: aspose.pydrawing.drawing2d.ColorBlend):
        ...
    
    @property
    def wrap_mode(self) -> aspose.pydrawing.drawing2d.WrapMode:
        ...
    
    @wrap_mode.setter
    def wrap_mode(self, value: aspose.pydrawing.drawing2d.WrapMode):
        ...
    
    @property
    def transform(self) -> aspose.pydrawing.drawing2d.Matrix:
        ...
    
    @transform.setter
    def transform(self, value: aspose.pydrawing.drawing2d.Matrix):
        ...
    
    ...

class Matrix:
    
    @overload
    def __init__(self):
        ...
    
    @overload
    def __init__(self, m11: float, m12: float, m21: float, m22: float, dx: float, dy: float):
        ...
    
    @overload
    def __init__(self, rect: aspose.pydrawing.RectangleF, plgpts: list[aspose.pydrawing.PointF]):
        ...
    
    @overload
    def __init__(self, rect: aspose.pydrawing.Rectangle, plgpts: list[aspose.pydrawing.Point]):
        ...
    
    @overload
    def multiply(self, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        ...
    
    @overload
    def multiply(self, matrix: aspose.pydrawing.drawing2d.Matrix, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    @overload
    def translate(self, offset_x: float, offset_y: float) -> None:
        ...
    
    @overload
    def translate(self, offset_x: float, offset_y: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    @overload
    def scale(self, scale_x: float, scale_y: float) -> None:
        ...
    
    @overload
    def scale(self, scale_x: float, scale_y: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    @overload
    def rotate(self, angle: float) -> None:
        ...
    
    @overload
    def rotate(self, angle: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    @overload
    def rotate_at(self, angle: float, point: aspose.pydrawing.PointF) -> None:
        ...
    
    @overload
    def rotate_at(self, angle: float, point: aspose.pydrawing.PointF, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    @overload
    def shear(self, shear_x: float, shear_y: float) -> None:
        ...
    
    @overload
    def shear(self, shear_x: float, shear_y: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    @overload
    def transform_points(self, pts: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def transform_points(self, pts: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def transform_vectors(self, pts: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def transform_vectors(self, pts: list[aspose.pydrawing.Point]) -> None:
        ...
    
    def clone(self) -> aspose.pydrawing.drawing2d.Matrix:
        ...
    
    def reset(self) -> None:
        ...
    
    def invert(self) -> None:
        ...
    
    def vector_transform_points(self, pts: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @property
    def elements(self) -> list[float]:
        ...
    
    @property
    def offset_x(self) -> float:
        ...
    
    @property
    def offset_y(self) -> float:
        ...
    
    @property
    def is_invertible(self) -> bool:
        ...
    
    @property
    def is_identity(self) -> bool:
        ...
    
    ...

class PathData:
    
    def __init__(self):
        ...
    
    @property
    def points(self) -> list[aspose.pydrawing.PointF]:
        ...
    
    @points.setter
    def points(self, value: list[aspose.pydrawing.PointF]):
        ...
    
    @property
    def types(self) -> bytes:
        ...
    
    @types.setter
    def types(self, value: bytes):
        ...
    
    ...

class PathGradientBrush:
    
    @overload
    def __init__(self, points: list[aspose.pydrawing.PointF]):
        ...
    
    @overload
    def __init__(self, points: list[aspose.pydrawing.PointF], wrap_mode: aspose.pydrawing.drawing2d.WrapMode):
        ...
    
    @overload
    def __init__(self, points: list[aspose.pydrawing.Point]):
        ...
    
    @overload
    def __init__(self, points: list[aspose.pydrawing.Point], wrap_mode: aspose.pydrawing.drawing2d.WrapMode):
        ...
    
    @overload
    def __init__(self, path: aspose.pydrawing.drawing2d.GraphicsPath):
        ...
    
    @overload
    def set_sigma_bell_shape(self, focus: float) -> None:
        ...
    
    @overload
    def set_sigma_bell_shape(self, focus: float, scale: float) -> None:
        ...
    
    @overload
    def set_blend_triangular_shape(self, focus: float) -> None:
        ...
    
    @overload
    def set_blend_triangular_shape(self, focus: float, scale: float) -> None:
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.drawing2d.Matrix, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float) -> None:
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float) -> None:
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    @overload
    def rotate_transform(self, angle: float) -> None:
        ...
    
    @overload
    def rotate_transform(self, angle: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        ...
    
    def clone(self) -> object:
        ...
    
    def reset_transform(self) -> None:
        ...
    
    @property
    def center_color(self) -> aspose.pydrawing.Color:
        ...
    
    @center_color.setter
    def center_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def surround_colors(self) -> list[aspose.pydrawing.Color]:
        ...
    
    @surround_colors.setter
    def surround_colors(self, value: list[aspose.pydrawing.Color]):
        ...
    
    @property
    def center_point(self) -> aspose.pydrawing.PointF:
        ...
    
    @center_point.setter
    def center_point(self, value: aspose.pydrawing.PointF):
        ...
    
    @property
    def rectangle(self) -> aspose.pydrawing.RectangleF:
        ...
    
    @property
    def blend(self) -> aspose.pydrawing.drawing2d.Blend:
        ...
    
    @blend.setter
    def blend(self, value: aspose.pydrawing.drawing2d.Blend):
        ...
    
    @property
    def interpolation_colors(self) -> aspose.pydrawing.drawing2d.ColorBlend:
        ...
    
    @interpolation_colors.setter
    def interpolation_colors(self, value: aspose.pydrawing.drawing2d.ColorBlend):
        ...
    
    @property
    def transform(self) -> aspose.pydrawing.drawing2d.Matrix:
        ...
    
    @transform.setter
    def transform(self, value: aspose.pydrawing.drawing2d.Matrix):
        ...
    
    @property
    def focus_scales(self) -> aspose.pydrawing.PointF:
        ...
    
    @focus_scales.setter
    def focus_scales(self, value: aspose.pydrawing.PointF):
        ...
    
    @property
    def wrap_mode(self) -> aspose.pydrawing.drawing2d.WrapMode:
        ...
    
    @wrap_mode.setter
    def wrap_mode(self, value: aspose.pydrawing.drawing2d.WrapMode):
        ...
    
    ...

class RegionData:
    
    @property
    def data(self) -> bytes:
        ...
    
    @data.setter
    def data(self, value: bytes):
        ...
    
    ...

class AdjustableArrowCap:
    
    @overload
    def __init__(self, width: float, height: float):
        ...
    
    @overload
    def __init__(self, width: float, height: float, is_filled: bool):
        ...
    
    def clone(self) -> object:
        ...
    
    def set_stroke_caps(self, start_cap: aspose.pydrawing.drawing2d.LineCap, end_cap: aspose.pydrawing.drawing2d.LineCap) -> None:
        ...
    
    def get_stroke_caps(self, start_cap: aspose.pydrawing.drawing2d.LineCap, end_cap: aspose.pydrawing.drawing2d.LineCap) -> None:
        ...
    
    @property
    def stroke_join(self) -> aspose.pydrawing.drawing2d.LineJoin:
        ...
    
    @stroke_join.setter
    def stroke_join(self, value: aspose.pydrawing.drawing2d.LineJoin):
        ...
    
    @property
    def base_cap(self) -> aspose.pydrawing.drawing2d.LineCap:
        ...
    
    @base_cap.setter
    def base_cap(self, value: aspose.pydrawing.drawing2d.LineCap):
        ...
    
    @property
    def base_inset(self) -> float:
        ...
    
    @base_inset.setter
    def base_inset(self, value: float):
        ...
    
    @property
    def width_scale(self) -> float:
        ...
    
    @width_scale.setter
    def width_scale(self, value: float):
        ...
    
    @property
    def height(self) -> float:
        ...
    
    @height.setter
    def height(self, value: float):
        ...
    
    @property
    def width(self) -> float:
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def middle_inset(self) -> float:
        ...
    
    @middle_inset.setter
    def middle_inset(self, value: float):
        ...
    
    @property
    def filled(self) -> bool:
        ...
    
    @filled.setter
    def filled(self, value: bool):
        ...
    
    ...

class CustomLineCap:
    
    @overload
    def __init__(self, fill_path: aspose.pydrawing.drawing2d.GraphicsPath, stroke_path: aspose.pydrawing.drawing2d.GraphicsPath):
        ...
    
    @overload
    def __init__(self, fill_path: aspose.pydrawing.drawing2d.GraphicsPath, stroke_path: aspose.pydrawing.drawing2d.GraphicsPath, base_cap: aspose.pydrawing.drawing2d.LineCap):
        ...
    
    @overload
    def __init__(self, fill_path: aspose.pydrawing.drawing2d.GraphicsPath, stroke_path: aspose.pydrawing.drawing2d.GraphicsPath, base_cap: aspose.pydrawing.drawing2d.LineCap, base_inset: float):
        ...
    
    def clone(self) -> object:
        ...
    
    def set_stroke_caps(self, start_cap: aspose.pydrawing.drawing2d.LineCap, end_cap: aspose.pydrawing.drawing2d.LineCap) -> None:
        ...
    
    def get_stroke_caps(self, start_cap: aspose.pydrawing.drawing2d.LineCap, end_cap: aspose.pydrawing.drawing2d.LineCap) -> None:
        ...
    
    @property
    def stroke_join(self) -> aspose.pydrawing.drawing2d.LineJoin:
        ...
    
    @stroke_join.setter
    def stroke_join(self, value: aspose.pydrawing.drawing2d.LineJoin):
        ...
    
    @property
    def base_cap(self) -> aspose.pydrawing.drawing2d.LineCap:
        ...
    
    @base_cap.setter
    def base_cap(self, value: aspose.pydrawing.drawing2d.LineCap):
        ...
    
    @property
    def base_inset(self) -> float:
        ...
    
    @base_inset.setter
    def base_inset(self, value: float):
        ...
    
    @property
    def width_scale(self) -> float:
        ...
    
    @width_scale.setter
    def width_scale(self, value: float):
        ...
    
    ...

class GraphicsPathIterator:
    
    def __init__(self, path: aspose.pydrawing.drawing2d.GraphicsPath):
        ...
    
    @overload
    def next_subpath(self, start_index: int, end_index: int, is_closed: bool) -> int:
        ...
    
    @overload
    def next_subpath(self, path: aspose.pydrawing.drawing2d.GraphicsPath, is_closed: bool) -> int:
        ...
    
    @overload
    def next_marker(self, start_index: int, end_index: int) -> int:
        ...
    
    @overload
    def next_marker(self, path: aspose.pydrawing.drawing2d.GraphicsPath) -> int:
        ...
    
    def next_path_type(self, path_type: int, start_index: int, end_index: int) -> int:
        ...
    
    def has_curve(self) -> bool:
        ...
    
    def rewind(self) -> None:
        ...
    
    def enumerate(self, points: list[aspose.pydrawing.PointF], types: bytes) -> int:
        ...
    
    def copy_data(self, points: list[aspose.pydrawing.PointF], types: bytes, start_index: int, end_index: int) -> int:
        ...
    
    @property
    def count(self) -> int:
        ...
    
    @property
    def subpath_count(self) -> int:
        ...
    
    ...

class GraphicsState:
    
    ...

class GraphicsPath:
    
    @overload
    def __init__(self):
        ...
    
    @overload
    def __init__(self, fill_mode: aspose.pydrawing.drawing2d.FillMode):
        ...
    
    @overload
    def __init__(self, pts: list[aspose.pydrawing.PointF], types: bytes):
        ...
    
    @overload
    def __init__(self, pts: list[aspose.pydrawing.PointF], types: bytes, fill_mode: aspose.pydrawing.drawing2d.FillMode):
        ...
    
    @overload
    def __init__(self, pts: list[aspose.pydrawing.Point], types: bytes):
        ...
    
    @overload
    def __init__(self, pts: list[aspose.pydrawing.Point], types: bytes, fill_mode: aspose.pydrawing.drawing2d.FillMode):
        ...
    
    @overload
    def is_visible(self, x: float, y: float) -> bool:
        ...
    
    @overload
    def is_visible(self, point: aspose.pydrawing.PointF) -> bool:
        ...
    
    @overload
    def is_visible(self, x: float, y: float, graphics: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_visible(self, pt: aspose.pydrawing.PointF, graphics: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_visible(self, x: int, y: int) -> bool:
        ...
    
    @overload
    def is_visible(self, point: aspose.pydrawing.Point) -> bool:
        ...
    
    @overload
    def is_visible(self, x: int, y: int, graphics: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_visible(self, pt: aspose.pydrawing.Point, graphics: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_outline_visible(self, x: float, y: float, pen: aspose.pydrawing.Pen) -> bool:
        ...
    
    @overload
    def is_outline_visible(self, point: aspose.pydrawing.PointF, pen: aspose.pydrawing.Pen) -> bool:
        ...
    
    @overload
    def is_outline_visible(self, x: float, y: float, pen: aspose.pydrawing.Pen, graphics: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_outline_visible(self, pt: aspose.pydrawing.PointF, pen: aspose.pydrawing.Pen, graphics: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_outline_visible(self, x: int, y: int, pen: aspose.pydrawing.Pen) -> bool:
        ...
    
    @overload
    def is_outline_visible(self, point: aspose.pydrawing.Point, pen: aspose.pydrawing.Pen) -> bool:
        ...
    
    @overload
    def is_outline_visible(self, x: int, y: int, pen: aspose.pydrawing.Pen, graphics: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def is_outline_visible(self, pt: aspose.pydrawing.Point, pen: aspose.pydrawing.Pen, graphics: aspose.pydrawing.Graphics) -> bool:
        ...
    
    @overload
    def add_line(self, pt1: aspose.pydrawing.PointF, pt2: aspose.pydrawing.PointF) -> None:
        ...
    
    @overload
    def add_line(self, x1: float, y1: float, x2: float, y2: float) -> None:
        ...
    
    @overload
    def add_line(self, pt1: aspose.pydrawing.Point, pt2: aspose.pydrawing.Point) -> None:
        ...
    
    @overload
    def add_line(self, x1: int, y1: int, x2: int, y2: int) -> None:
        ...
    
    @overload
    def add_lines(self, points: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def add_lines(self, points: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def add_arc(self, rect: aspose.pydrawing.RectangleF, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def add_arc(self, x: float, y: float, width: float, height: float, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def add_arc(self, rect: aspose.pydrawing.Rectangle, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def add_arc(self, x: int, y: int, width: int, height: int, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def add_bezier(self, pt1: aspose.pydrawing.PointF, pt2: aspose.pydrawing.PointF, pt3: aspose.pydrawing.PointF, pt4: aspose.pydrawing.PointF) -> None:
        ...
    
    @overload
    def add_bezier(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> None:
        ...
    
    @overload
    def add_bezier(self, pt1: aspose.pydrawing.Point, pt2: aspose.pydrawing.Point, pt3: aspose.pydrawing.Point, pt4: aspose.pydrawing.Point) -> None:
        ...
    
    @overload
    def add_bezier(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int) -> None:
        ...
    
    @overload
    def add_beziers(self, points: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def add_beziers(self, points: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def add_curve(self, points: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def add_curve(self, points: list[aspose.pydrawing.PointF], tension: float) -> None:
        ...
    
    @overload
    def add_curve(self, points: list[aspose.pydrawing.PointF], offset: int, number_of_segments: int, tension: float) -> None:
        ...
    
    @overload
    def add_curve(self, points: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def add_curve(self, points: list[aspose.pydrawing.Point], tension: float) -> None:
        ...
    
    @overload
    def add_curve(self, points: list[aspose.pydrawing.Point], offset: int, number_of_segments: int, tension: float) -> None:
        ...
    
    @overload
    def add_closed_curve(self, points: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def add_closed_curve(self, points: list[aspose.pydrawing.PointF], tension: float) -> None:
        ...
    
    @overload
    def add_closed_curve(self, points: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def add_closed_curve(self, points: list[aspose.pydrawing.Point], tension: float) -> None:
        ...
    
    @overload
    def add_rectangle(self, rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def add_rectangle(self, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def add_rectangles(self, rects: list[aspose.pydrawing.RectangleF]) -> None:
        ...
    
    @overload
    def add_rectangles(self, rects: list[aspose.pydrawing.Rectangle]) -> None:
        ...
    
    @overload
    def add_ellipse(self, rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def add_ellipse(self, x: float, y: float, width: float, height: float) -> None:
        ...
    
    @overload
    def add_ellipse(self, rect: aspose.pydrawing.Rectangle) -> None:
        ...
    
    @overload
    def add_ellipse(self, x: int, y: int, width: int, height: int) -> None:
        ...
    
    @overload
    def add_pie(self, rect: aspose.pydrawing.Rectangle, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def add_pie(self, x: float, y: float, width: float, height: float, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def add_pie(self, x: int, y: int, width: int, height: int, start_angle: float, sweep_angle: float) -> None:
        ...
    
    @overload
    def add_polygon(self, points: list[aspose.pydrawing.PointF]) -> None:
        ...
    
    @overload
    def add_polygon(self, points: list[aspose.pydrawing.Point]) -> None:
        ...
    
    @overload
    def add_string(self, s: str, family: aspose.pydrawing.FontFamily, style: int, em_size: float, origin: aspose.pydrawing.PointF, format: aspose.pydrawing.StringFormat) -> None:
        ...
    
    @overload
    def add_string(self, s: str, family: aspose.pydrawing.FontFamily, style: int, em_size: float, origin: aspose.pydrawing.Point, format: aspose.pydrawing.StringFormat) -> None:
        ...
    
    @overload
    def add_string(self, s: str, family: aspose.pydrawing.FontFamily, style: int, em_size: float, layout_rect: aspose.pydrawing.RectangleF, format: aspose.pydrawing.StringFormat) -> None:
        ...
    
    @overload
    def add_string(self, s: str, family: aspose.pydrawing.FontFamily, style: int, em_size: float, layout_rect: aspose.pydrawing.Rectangle, format: aspose.pydrawing.StringFormat) -> None:
        ...
    
    @overload
    def get_bounds(self) -> aspose.pydrawing.RectangleF:
        ...
    
    @overload
    def get_bounds(self, matrix: aspose.pydrawing.drawing2d.Matrix) -> aspose.pydrawing.RectangleF:
        ...
    
    @overload
    def get_bounds(self, matrix: aspose.pydrawing.drawing2d.Matrix, pen: aspose.pydrawing.Pen) -> aspose.pydrawing.RectangleF:
        ...
    
    @overload
    def flatten(self) -> None:
        ...
    
    @overload
    def flatten(self, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        ...
    
    @overload
    def flatten(self, matrix: aspose.pydrawing.drawing2d.Matrix, flatness: float) -> None:
        ...
    
    @overload
    def widen(self, pen: aspose.pydrawing.Pen) -> None:
        ...
    
    @overload
    def widen(self, pen: aspose.pydrawing.Pen, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        ...
    
    @overload
    def widen(self, pen: aspose.pydrawing.Pen, matrix: aspose.pydrawing.drawing2d.Matrix, flatness: float) -> None:
        ...
    
    @overload
    def warp(self, dest_points: list[aspose.pydrawing.PointF], src_rect: aspose.pydrawing.RectangleF) -> None:
        ...
    
    @overload
    def warp(self, dest_points: list[aspose.pydrawing.PointF], src_rect: aspose.pydrawing.RectangleF, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        ...
    
    @overload
    def warp(self, dest_points: list[aspose.pydrawing.PointF], src_rect: aspose.pydrawing.RectangleF, matrix: aspose.pydrawing.drawing2d.Matrix, warp_mode: aspose.pydrawing.drawing2d.WarpMode) -> None:
        ...
    
    @overload
    def warp(self, dest_points: list[aspose.pydrawing.PointF], src_rect: aspose.pydrawing.RectangleF, matrix: aspose.pydrawing.drawing2d.Matrix, warp_mode: aspose.pydrawing.drawing2d.WarpMode, flatness: float) -> None:
        ...
    
    def clone(self) -> object:
        ...
    
    def reset(self) -> None:
        ...
    
    def start_figure(self) -> None:
        ...
    
    def close_figure(self) -> None:
        ...
    
    def close_all_figures(self) -> None:
        ...
    
    def set_markers(self) -> None:
        ...
    
    def clear_markers(self) -> None:
        ...
    
    def reverse(self) -> None:
        ...
    
    def get_last_point(self) -> aspose.pydrawing.PointF:
        ...
    
    def add_path(self, adding_path: aspose.pydrawing.drawing2d.GraphicsPath, connect: bool) -> None:
        ...
    
    def transform(self, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        ...
    
    @property
    def fill_mode(self) -> aspose.pydrawing.drawing2d.FillMode:
        ...
    
    @fill_mode.setter
    def fill_mode(self, value: aspose.pydrawing.drawing2d.FillMode):
        ...
    
    @property
    def path_data(self) -> aspose.pydrawing.drawing2d.PathData:
        ...
    
    @property
    def point_count(self) -> int:
        ...
    
    @property
    def path_types(self) -> bytes:
        ...
    
    @property
    def path_points(self) -> list[aspose.pydrawing.PointF]:
        ...
    
    ...

class CombineMode(Enum):
    
    REPLACE: int
    
    INTERSECT: int
    
    UNION: int
    
    XOR: int
    
    EXCLUDE: int
    
    COMPLEMENT: int
    

class CompositingMode(Enum):
    
    SOURCE_OVER: int
    
    SOURCE_COPY: int
    

class CompositingQuality(Enum):
    
    INVALID: int
    
    DEFAULT: int
    
    HIGH_SPEED: int
    
    HIGH_QUALITY: int
    
    GAMMA_CORRECTED: int
    
    ASSUME_LINEAR: int
    

class CoordinateSpace(Enum):
    
    WORLD: int
    
    PAGE: int
    
    DEVICE: int
    

class DashStyle(Enum):
    
    SOLID: int
    
    DASH: int
    
    DOT: int
    
    DASH_DOT: int
    
    DASH_DOT_DOT: int
    
    CUSTOM: int
    

class FillMode(Enum):
    
    ALTERNATE: int
    
    WINDING: int
    

class FlushIntention(Enum):
    
    FLUSH: int
    
    SYNC: int
    

class HatchStyle(Enum):
    
    HORIZONTAL: int
    
    VERTICAL: int
    
    FORWARD_DIAGONAL: int
    
    BACKWARD_DIAGONAL: int
    
    CROSS: int
    
    DIAGONAL_CROSS: int
    
    PERCENT05: int
    
    PERCENT10: int
    
    PERCENT20: int
    
    PERCENT25: int
    
    PERCENT30: int
    
    PERCENT40: int
    
    PERCENT50: int
    
    PERCENT60: int
    
    PERCENT70: int
    
    PERCENT75: int
    
    PERCENT80: int
    
    PERCENT90: int
    
    LIGHT_DOWNWARD_DIAGONAL: int
    
    LIGHT_UPWARD_DIAGONAL: int
    
    DARK_DOWNWARD_DIAGONAL: int
    
    DARK_UPWARD_DIAGONAL: int
    
    WIDE_DOWNWARD_DIAGONAL: int
    
    WIDE_UPWARD_DIAGONAL: int
    
    LIGHT_VERTICAL: int
    
    LIGHT_HORIZONTAL: int
    
    NARROW_VERTICAL: int
    
    NARROW_HORIZONTAL: int
    
    DARK_VERTICAL: int
    
    DARK_HORIZONTAL: int
    
    DASHED_DOWNWARD_DIAGONAL: int
    
    DASHED_UPWARD_DIAGONAL: int
    
    DASHED_HORIZONTAL: int
    
    DASHED_VERTICAL: int
    
    SMALL_CONFETTI: int
    
    LARGE_CONFETTI: int
    
    ZIG_ZAG: int
    
    WAVE: int
    
    DIAGONAL_BRICK: int
    
    HORIZONTAL_BRICK: int
    
    WEAVE: int
    
    PLAID: int
    
    DIVOT: int
    
    DOTTED_GRID: int
    
    DOTTED_DIAMOND: int
    
    SHINGLE: int
    
    TRELLIS: int
    
    SPHERE: int
    
    SMALL_GRID: int
    
    SMALL_CHECKER_BOARD: int
    
    LARGE_CHECKER_BOARD: int
    
    OUTLINED_DIAMOND: int
    
    SOLID_DIAMOND: int
    
    LARGE_GRID: int
    
    MIN: int
    
    MAX: int
    

class InterpolationMode(Enum):
    
    INVALID: int
    
    DEFAULT: int
    
    LOW: int
    
    HIGH: int
    
    BILINEAR: int
    
    BICUBIC: int
    
    NEAREST_NEIGHBOR: int
    
    HIGH_QUALITY_BILINEAR: int
    
    HIGH_QUALITY_BICUBIC: int
    

class LinearGradientMode(Enum):
    
    HORIZONTAL: int
    
    VERTICAL: int
    
    FORWARD_DIAGONAL: int
    
    BACKWARD_DIAGONAL: int
    

class LineCap(Enum):
    
    FLAT: int
    
    SQUARE: int
    
    ROUND: int
    
    TRIANGLE: int
    
    NO_ANCHOR: int
    
    SQUARE_ANCHOR: int
    
    ROUND_ANCHOR: int
    
    DIAMOND_ANCHOR: int
    
    ARROW_ANCHOR: int
    
    CUSTOM: int
    
    ANCHOR_MASK: int
    

class LineJoin(Enum):
    
    MITER: int
    
    BEVEL: int
    
    ROUND: int
    
    MITER_CLIPPED: int
    

class MatrixOrder(Enum):
    
    PREPEND: int
    
    APPEND: int
    

class PathPointType(Enum):
    
    START: int
    
    LINE: int
    
    BEZIER: int
    
    PATH_TYPE_MASK: int
    
    DASH_MODE: int
    
    PATH_MARKER: int
    
    CLOSE_SUBPATH: int
    
    BEZIER3: int
    

class PenAlignment(Enum):
    
    CENTER: int
    
    INSET: int
    
    OUTSET: int
    
    LEFT: int
    
    RIGHT: int
    

class PenType(Enum):
    
    SOLID_COLOR: int
    
    HATCH_FILL: int
    
    TEXTURE_FILL: int
    
    PATH_GRADIENT: int
    
    LINEAR_GRADIENT: int
    

class PixelOffsetMode(Enum):
    
    INVALID: int
    
    DEFAULT: int
    
    HIGH_SPEED: int
    
    HIGH_QUALITY: int
    
    NONE: int
    
    HALF: int
    

class QualityMode(Enum):
    
    INVALID: int
    
    DEFAULT: int
    
    LOW: int
    
    HIGH: int
    

class SmoothingMode(Enum):
    
    INVALID: int
    
    DEFAULT: int
    
    HIGH_SPEED: int
    
    HIGH_QUALITY: int
    
    NONE: int
    
    ANTI_ALIAS: int
    

class WrapMode(Enum):
    
    TILE: int
    
    TILE_FLIP_X: int
    
    TILE_FLIP_Y: int
    
    TILE_FLIP_XY: int
    
    CLAMP: int
    

class WarpMode(Enum):
    
    PERSPECTIVE: int
    
    BILINEAR: int
    

class DashCap(Enum):
    
    FLAT: int
    
    ROUND: int
    
    TRIANGLE: int
    

