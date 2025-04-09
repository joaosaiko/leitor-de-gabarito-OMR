import aspose.pydrawing
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable
from enum import Enum

class Metafile:
    
    @overload
    def __init__(self, filename: str):
        ...
    
    @overload
    def __init__(self, stream: io.BytesIO):
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
    def save(self, filename: str, format: aspose.pydrawing.imaging.ImageFormat) -> None:
        ...
    
    @overload
    def save(self, filename: str, encoder: aspose.pydrawing.imaging.ImageCodecInfo, encoder_params: aspose.pydrawing.imaging.EncoderParameters) -> None:
        ...
    
    @overload
    def save(self, stream: io.BytesIO, format: aspose.pydrawing.imaging.ImageFormat) -> None:
        ...
    
    @overload
    def save(self, stream: io.BytesIO, encoder: aspose.pydrawing.imaging.ImageCodecInfo, encoder_params: aspose.pydrawing.imaging.EncoderParameters) -> None:
        ...
    
    @overload
    def save_add(self, encoder_params: aspose.pydrawing.imaging.EncoderParameters) -> None:
        ...
    
    @overload
    def save_add(self, image: aspose.pydrawing.Image, encoder_params: aspose.pydrawing.imaging.EncoderParameters) -> None:
        ...
    
    @overload
    @staticmethod
    def get_metafile_header(file_name: str) -> aspose.pydrawing.imaging.MetafileHeader:
        ...
    
    @overload
    @staticmethod
    def get_metafile_header(stream: io.BytesIO) -> aspose.pydrawing.imaging.MetafileHeader:
        ...
    
    @overload
    def get_metafile_header(self) -> aspose.pydrawing.imaging.MetafileHeader:
        ...
    
    def get_frame_count(self, dimension: aspose.pydrawing.imaging.FrameDimension) -> int:
        ...
    
    def select_active_frame(self, dimension: aspose.pydrawing.imaging.FrameDimension, frame_index: int) -> int:
        ...
    
    def rotate_flip(self, rotate_flip_type: aspose.pydrawing.RotateFlipType) -> None:
        ...
    
    def remove_property_item(self, propid: int) -> None:
        ...
    
    def get_encoder_parameter_list(self, encoder: uuid.UUID) -> aspose.pydrawing.imaging.EncoderParameters:
        ...
    
    @staticmethod
    def is_extended_pixel_format(pixfmt: aspose.pydrawing.imaging.PixelFormat) -> bool:
        ...
    
    @staticmethod
    def is_canonical_pixel_format(pixfmt: aspose.pydrawing.imaging.PixelFormat) -> bool:
        ...
    
    @staticmethod
    def get_pixel_format_size(pixfmt: aspose.pydrawing.imaging.PixelFormat) -> int:
        ...
    
    @staticmethod
    def is_alpha_pixel_format(pixfmt: aspose.pydrawing.imaging.PixelFormat) -> bool:
        ...
    
    def clone(self) -> object:
        ...
    
    def get_bounds(self, page_unit: aspose.pydrawing.GraphicsUnit) -> aspose.pydrawing.RectangleF:
        ...
    
    def get_property_item(self, propid: int) -> aspose.pydrawing.imaging.PropertyItem:
        ...
    
    def set_property_item(self, propitem: aspose.pydrawing.imaging.PropertyItem) -> None:
        ...
    
    def play_record(self, record_type: aspose.pydrawing.imaging.EmfPlusRecordType, flags: int, data_size: int, data: bytes) -> None:
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
    def raw_format(self) -> aspose.pydrawing.imaging.ImageFormat:
        ...
    
    @property
    def pixel_format(self) -> aspose.pydrawing.imaging.PixelFormat:
        ...
    
    @property
    def frame_dimensions_list(self) -> list[uuid.UUID]:
        ...
    
    @property
    def palette(self) -> aspose.pydrawing.imaging.ColorPalette:
        ...
    
    @palette.setter
    def palette(self, value: aspose.pydrawing.imaging.ColorPalette):
        ...
    
    @property
    def property_id_list(self) -> list[int]:
        ...
    
    @property
    def property_items(self) -> list[aspose.pydrawing.imaging.PropertyItem]:
        ...
    
    ...

class ColorMap:
    
    def __init__(self):
        ...
    
    @property
    def old_color(self) -> aspose.pydrawing.Color:
        ...
    
    @old_color.setter
    def old_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def new_color(self) -> aspose.pydrawing.Color:
        ...
    
    @new_color.setter
    def new_color(self, value: aspose.pydrawing.Color):
        ...
    
    ...

class Encoder:
    
    def __init__(self, guid: uuid.UUID):
        ...
    
    @property
    def guid(self) -> uuid.UUID:
        ...
    
    COMPRESSION: aspose.pydrawing.imaging.Encoder
    
    COLOR_DEPTH: aspose.pydrawing.imaging.Encoder
    
    SCAN_METHOD: aspose.pydrawing.imaging.Encoder
    
    VERSION: aspose.pydrawing.imaging.Encoder
    
    RENDER_METHOD: aspose.pydrawing.imaging.Encoder
    
    QUALITY: aspose.pydrawing.imaging.Encoder
    
    TRANSFORMATION: aspose.pydrawing.imaging.Encoder
    
    LUMINANCE_TABLE: aspose.pydrawing.imaging.Encoder
    
    CHROMINANCE_TABLE: aspose.pydrawing.imaging.Encoder
    
    SAVE_FLAG: aspose.pydrawing.imaging.Encoder
    
    COLOR_SPACE: aspose.pydrawing.imaging.Encoder
    
    IMAGE_ITEMS: aspose.pydrawing.imaging.Encoder
    
    SAVE_AS_CMYK: aspose.pydrawing.imaging.Encoder
    
    ...

class FrameDimension:
    
    def __init__(self, guid: uuid.UUID):
        ...
    
    @property
    def guid(self) -> uuid.UUID:
        ...
    
    time: aspose.pydrawing.imaging.FrameDimension
    
    resolution: aspose.pydrawing.imaging.FrameDimension
    
    page: aspose.pydrawing.imaging.FrameDimension
    
    ...

class ImageFormat:
    
    def __init__(self, guid: uuid.UUID):
        ...
    
    @property
    def guid(self) -> uuid.UUID:
        ...
    
    memory_bmp: aspose.pydrawing.imaging.ImageFormat
    
    bmp: aspose.pydrawing.imaging.ImageFormat
    
    emf: aspose.pydrawing.imaging.ImageFormat
    
    wmf: aspose.pydrawing.imaging.ImageFormat
    
    gif: aspose.pydrawing.imaging.ImageFormat
    
    jpeg: aspose.pydrawing.imaging.ImageFormat
    
    png: aspose.pydrawing.imaging.ImageFormat
    
    tiff: aspose.pydrawing.imaging.ImageFormat
    
    exif: aspose.pydrawing.imaging.ImageFormat
    
    icon: aspose.pydrawing.imaging.ImageFormat
    
    ...

class PropertyItem:
    
    @property
    def id(self) -> int:
        ...
    
    @id.setter
    def id(self, value: int):
        ...
    
    @property
    def len(self) -> int:
        ...
    
    @len.setter
    def len(self, value: int):
        ...
    
    @property
    def type(self) -> int:
        ...
    
    @type.setter
    def type(self, value: int):
        ...
    
    @property
    def value(self) -> bytes:
        ...
    
    @value.setter
    def value(self, value: bytes):
        ...
    
    ...

class WmfPlaceableFileHeader:
    
    def __init__(self):
        ...
    
    @property
    def key(self) -> int:
        ...
    
    @key.setter
    def key(self, value: int):
        ...
    
    @property
    def hmf(self) -> int:
        ...
    
    @hmf.setter
    def hmf(self, value: int):
        ...
    
    @property
    def bbox_left(self) -> int:
        ...
    
    @bbox_left.setter
    def bbox_left(self, value: int):
        ...
    
    @property
    def bbox_top(self) -> int:
        ...
    
    @bbox_top.setter
    def bbox_top(self, value: int):
        ...
    
    @property
    def bbox_right(self) -> int:
        ...
    
    @bbox_right.setter
    def bbox_right(self, value: int):
        ...
    
    @property
    def bbox_bottom(self) -> int:
        ...
    
    @bbox_bottom.setter
    def bbox_bottom(self, value: int):
        ...
    
    @property
    def inch(self) -> int:
        ...
    
    @inch.setter
    def inch(self, value: int):
        ...
    
    @property
    def reserved(self) -> int:
        ...
    
    @reserved.setter
    def reserved(self, value: int):
        ...
    
    @property
    def checksum(self) -> int:
        ...
    
    @checksum.setter
    def checksum(self, value: int):
        ...
    
    ...

class BitmapData:
    
    def __init__(self):
        ...
    
    @property
    def width(self) -> int:
        ...
    
    @width.setter
    def width(self, value: int):
        ...
    
    @property
    def height(self) -> int:
        ...
    
    @height.setter
    def height(self, value: int):
        ...
    
    @property
    def stride(self) -> int:
        ...
    
    @stride.setter
    def stride(self, value: int):
        ...
    
    @property
    def pixel_format(self) -> aspose.pydrawing.imaging.PixelFormat:
        ...
    
    @pixel_format.setter
    def pixel_format(self, value: aspose.pydrawing.imaging.PixelFormat):
        ...
    
    @property
    def reserved(self) -> int:
        ...
    
    @reserved.setter
    def reserved(self, value: int):
        ...
    
    ...

class ColorMatrix:
    
    @overload
    def __init__(self):
        ...
    
    @overload
    def __init__(self, new_color_matrix: list[list[float]]):
        ...
    
    @property
    def matrix00(self) -> float:
        ...
    
    @matrix00.setter
    def matrix00(self, value: float):
        ...
    
    @property
    def matrix01(self) -> float:
        ...
    
    @matrix01.setter
    def matrix01(self, value: float):
        ...
    
    @property
    def matrix02(self) -> float:
        ...
    
    @matrix02.setter
    def matrix02(self, value: float):
        ...
    
    @property
    def matrix03(self) -> float:
        ...
    
    @matrix03.setter
    def matrix03(self, value: float):
        ...
    
    @property
    def matrix04(self) -> float:
        ...
    
    @matrix04.setter
    def matrix04(self, value: float):
        ...
    
    @property
    def matrix10(self) -> float:
        ...
    
    @matrix10.setter
    def matrix10(self, value: float):
        ...
    
    @property
    def matrix11(self) -> float:
        ...
    
    @matrix11.setter
    def matrix11(self, value: float):
        ...
    
    @property
    def matrix12(self) -> float:
        ...
    
    @matrix12.setter
    def matrix12(self, value: float):
        ...
    
    @property
    def matrix13(self) -> float:
        ...
    
    @matrix13.setter
    def matrix13(self, value: float):
        ...
    
    @property
    def matrix14(self) -> float:
        ...
    
    @matrix14.setter
    def matrix14(self, value: float):
        ...
    
    @property
    def matrix20(self) -> float:
        ...
    
    @matrix20.setter
    def matrix20(self, value: float):
        ...
    
    @property
    def matrix21(self) -> float:
        ...
    
    @matrix21.setter
    def matrix21(self, value: float):
        ...
    
    @property
    def matrix22(self) -> float:
        ...
    
    @matrix22.setter
    def matrix22(self, value: float):
        ...
    
    @property
    def matrix23(self) -> float:
        ...
    
    @matrix23.setter
    def matrix23(self, value: float):
        ...
    
    @property
    def matrix24(self) -> float:
        ...
    
    @matrix24.setter
    def matrix24(self, value: float):
        ...
    
    @property
    def matrix30(self) -> float:
        ...
    
    @matrix30.setter
    def matrix30(self, value: float):
        ...
    
    @property
    def matrix31(self) -> float:
        ...
    
    @matrix31.setter
    def matrix31(self, value: float):
        ...
    
    @property
    def matrix32(self) -> float:
        ...
    
    @matrix32.setter
    def matrix32(self, value: float):
        ...
    
    @property
    def matrix33(self) -> float:
        ...
    
    @matrix33.setter
    def matrix33(self, value: float):
        ...
    
    @property
    def matrix34(self) -> float:
        ...
    
    @matrix34.setter
    def matrix34(self, value: float):
        ...
    
    @property
    def matrix40(self) -> float:
        ...
    
    @matrix40.setter
    def matrix40(self, value: float):
        ...
    
    @property
    def matrix41(self) -> float:
        ...
    
    @matrix41.setter
    def matrix41(self, value: float):
        ...
    
    @property
    def matrix42(self) -> float:
        ...
    
    @matrix42.setter
    def matrix42(self, value: float):
        ...
    
    @property
    def matrix43(self) -> float:
        ...
    
    @matrix43.setter
    def matrix43(self, value: float):
        ...
    
    @property
    def matrix44(self) -> float:
        ...
    
    @matrix44.setter
    def matrix44(self, value: float):
        ...
    
    ...

class ColorPalette:
    
    @property
    def flags(self) -> int:
        ...
    
    @property
    def entries(self) -> list[aspose.pydrawing.Color]:
        ...
    
    ...

class EncoderParameter:
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, value: int):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, value: int, undefined: bool):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, value: int):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, value: int):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, numerator: int, denominator: int):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, rangebegin: int, rangeend: int):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, numerator1: int, demoninator1: int, numerator2: int, demoninator2: int):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, value: str):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, value: bytes):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, value: bytes, undefined: bool):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, value: list[int]):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, value: list[int]):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, numerator: list[int], denominator: list[int]):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, rangebegin: list[int], rangeend: list[int]):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, numerator1: list[int], denominator1: list[int], numerator2: list[int], denominator2: list[int]):
        ...
    
    @overload
    def __init__(self, encoder: aspose.pydrawing.imaging.Encoder, number_of_values: int, type: int, value: int):
        ...
    
    @property
    def encoder(self) -> aspose.pydrawing.imaging.Encoder:
        ...
    
    @encoder.setter
    def encoder(self, value: aspose.pydrawing.imaging.Encoder):
        ...
    
    @property
    def type(self) -> aspose.pydrawing.imaging.EncoderParameterValueType:
        ...
    
    @property
    def value_type(self) -> aspose.pydrawing.imaging.EncoderParameterValueType:
        ...
    
    @property
    def number_of_values(self) -> int:
        ...
    
    ...

class EncoderParameters:
    
    @overload
    def __init__(self, count: int):
        ...
    
    @overload
    def __init__(self):
        ...
    
    @property
    def param(self) -> list[aspose.pydrawing.imaging.EncoderParameter]:
        ...
    
    @param.setter
    def param(self, value: list[aspose.pydrawing.imaging.EncoderParameter]):
        ...
    
    ...

class ImageAttributes:
    
    def __init__(self):
        ...
    
    @overload
    def set_color_matrix(self, new_color_matrix: aspose.pydrawing.imaging.ColorMatrix) -> None:
        ...
    
    @overload
    def set_color_matrix(self, new_color_matrix: aspose.pydrawing.imaging.ColorMatrix, flags: aspose.pydrawing.imaging.ColorMatrixFlag) -> None:
        ...
    
    @overload
    def set_color_matrix(self, new_color_matrix: aspose.pydrawing.imaging.ColorMatrix, mode: aspose.pydrawing.imaging.ColorMatrixFlag, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def clear_color_matrix(self) -> None:
        ...
    
    @overload
    def clear_color_matrix(self, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def set_color_matrices(self, new_color_matrix: aspose.pydrawing.imaging.ColorMatrix, gray_matrix: aspose.pydrawing.imaging.ColorMatrix) -> None:
        ...
    
    @overload
    def set_color_matrices(self, new_color_matrix: aspose.pydrawing.imaging.ColorMatrix, gray_matrix: aspose.pydrawing.imaging.ColorMatrix, flags: aspose.pydrawing.imaging.ColorMatrixFlag) -> None:
        ...
    
    @overload
    def set_color_matrices(self, new_color_matrix: aspose.pydrawing.imaging.ColorMatrix, gray_matrix: aspose.pydrawing.imaging.ColorMatrix, mode: aspose.pydrawing.imaging.ColorMatrixFlag, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def set_threshold(self, threshold: float) -> None:
        ...
    
    @overload
    def set_threshold(self, threshold: float, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def clear_threshold(self) -> None:
        ...
    
    @overload
    def clear_threshold(self, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def set_gamma(self, gamma: float) -> None:
        ...
    
    @overload
    def set_gamma(self, gamma: float, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def clear_gamma(self) -> None:
        ...
    
    @overload
    def clear_gamma(self, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def set_no_op(self) -> None:
        ...
    
    @overload
    def set_no_op(self, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def clear_no_op(self) -> None:
        ...
    
    @overload
    def clear_no_op(self, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def set_color_key(self, color_low: aspose.pydrawing.Color, color_high: aspose.pydrawing.Color) -> None:
        ...
    
    @overload
    def set_color_key(self, color_low: aspose.pydrawing.Color, color_high: aspose.pydrawing.Color, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def clear_color_key(self) -> None:
        ...
    
    @overload
    def clear_color_key(self, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def set_output_channel(self, flags: aspose.pydrawing.imaging.ColorChannelFlag) -> None:
        ...
    
    @overload
    def set_output_channel(self, flags: aspose.pydrawing.imaging.ColorChannelFlag, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def clear_output_channel(self) -> None:
        ...
    
    @overload
    def clear_output_channel(self, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def set_output_channel_color_profile(self, color_profile_filename: str) -> None:
        ...
    
    @overload
    def set_output_channel_color_profile(self, color_profile_filename: str, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def clear_output_channel_color_profile(self) -> None:
        ...
    
    @overload
    def clear_output_channel_color_profile(self, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def set_remap_table(self, map: list[aspose.pydrawing.imaging.ColorMap]) -> None:
        ...
    
    @overload
    def set_remap_table(self, map: list[aspose.pydrawing.imaging.ColorMap], type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def clear_remap_table(self) -> None:
        ...
    
    @overload
    def clear_remap_table(self, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    @overload
    def set_wrap_mode(self, mode: aspose.pydrawing.Drawing2D.WrapMode) -> None:
        ...
    
    @overload
    def set_wrap_mode(self, mode: aspose.pydrawing.Drawing2D.WrapMode, color: aspose.pydrawing.Color) -> None:
        ...
    
    @overload
    def set_wrap_mode(self, mode: aspose.pydrawing.Drawing2D.WrapMode, color: aspose.pydrawing.Color, clamp: bool) -> None:
        ...
    
    def clone(self) -> object:
        ...
    
    def set_brush_remap_table(self, map: list[aspose.pydrawing.imaging.ColorMap]) -> None:
        ...
    
    def clear_brush_remap_table(self) -> None:
        ...
    
    def get_adjusted_palette(self, palette: aspose.pydrawing.imaging.ColorPalette, type: aspose.pydrawing.imaging.ColorAdjustType) -> None:
        ...
    
    ...

class ImageCodecInfo:
    
    @staticmethod
    def get_image_decoders() -> list[aspose.pydrawing.imaging.ImageCodecInfo]:
        ...
    
    @staticmethod
    def get_image_encoders() -> list[aspose.pydrawing.imaging.ImageCodecInfo]:
        ...
    
    @property
    def clsid(self) -> uuid.UUID:
        ...
    
    @clsid.setter
    def clsid(self, value: uuid.UUID):
        ...
    
    @property
    def format_id(self) -> uuid.UUID:
        ...
    
    @format_id.setter
    def format_id(self, value: uuid.UUID):
        ...
    
    @property
    def codec_name(self) -> str:
        ...
    
    @codec_name.setter
    def codec_name(self, value: str):
        ...
    
    @property
    def dll_name(self) -> str:
        ...
    
    @dll_name.setter
    def dll_name(self, value: str):
        ...
    
    @property
    def format_description(self) -> str:
        ...
    
    @format_description.setter
    def format_description(self, value: str):
        ...
    
    @property
    def filename_extension(self) -> str:
        ...
    
    @filename_extension.setter
    def filename_extension(self, value: str):
        ...
    
    @property
    def mime_type(self) -> str:
        ...
    
    @mime_type.setter
    def mime_type(self, value: str):
        ...
    
    @property
    def flags(self) -> aspose.pydrawing.imaging.ImageCodecFlags:
        ...
    
    @flags.setter
    def flags(self, value: aspose.pydrawing.imaging.ImageCodecFlags):
        ...
    
    @property
    def version(self) -> int:
        ...
    
    @version.setter
    def version(self, value: int):
        ...
    
    @property
    def signature_patterns(self) -> list[bytes]:
        ...
    
    @signature_patterns.setter
    def signature_patterns(self, value: list[bytes]):
        ...
    
    @property
    def signature_masks(self) -> list[bytes]:
        ...
    
    @signature_masks.setter
    def signature_masks(self, value: list[bytes]):
        ...
    
    ...

class MetafileHeader:
    
    def is_wmf(self) -> bool:
        ...
    
    def is_wmf_placeable(self) -> bool:
        ...
    
    def is_emf(self) -> bool:
        ...
    
    def is_emf_or_emf_plus(self) -> bool:
        ...
    
    def is_emf_plus(self) -> bool:
        ...
    
    def is_emf_plus_dual(self) -> bool:
        ...
    
    def is_emf_plus_only(self) -> bool:
        ...
    
    def is_display(self) -> bool:
        ...
    
    @property
    def type(self) -> aspose.pydrawing.imaging.MetafileType:
        ...
    
    @property
    def metafile_size(self) -> int:
        ...
    
    @property
    def version(self) -> int:
        ...
    
    @property
    def dpi_x(self) -> float:
        ...
    
    @property
    def dpi_y(self) -> float:
        ...
    
    @property
    def bounds(self) -> aspose.pydrawing.Rectangle:
        ...
    
    @property
    def wmf_header(self) -> aspose.pydrawing.imaging.MetaHeader:
        ...
    
    @property
    def emf_plus_header_size(self) -> int:
        ...
    
    @property
    def logical_dpi_x(self) -> int:
        ...
    
    @property
    def logical_dpi_y(self) -> int:
        ...
    
    ...

class MetaHeader:
    
    def __init__(self):
        ...
    
    @property
    def type(self) -> int:
        ...
    
    @type.setter
    def type(self, value: int):
        ...
    
    @property
    def header_size(self) -> int:
        ...
    
    @header_size.setter
    def header_size(self, value: int):
        ...
    
    @property
    def version(self) -> int:
        ...
    
    @version.setter
    def version(self, value: int):
        ...
    
    @property
    def size(self) -> int:
        ...
    
    @size.setter
    def size(self, value: int):
        ...
    
    @property
    def no_objects(self) -> int:
        ...
    
    @no_objects.setter
    def no_objects(self, value: int):
        ...
    
    @property
    def max_record(self) -> int:
        ...
    
    @max_record.setter
    def max_record(self, value: int):
        ...
    
    @property
    def no_parameters(self) -> int:
        ...
    
    @no_parameters.setter
    def no_parameters(self, value: int):
        ...
    
    ...

class ColorAdjustType(Enum):
    
    DEFAULT: int
    
    BITMAP: int
    
    BRUSH: int
    
    PEN: int
    
    TEXT: int
    
    COUNT: int
    
    ANY: int
    

class ColorChannelFlag(Enum):
    
    COLOR_CHANNEL_C: int
    
    COLOR_CHANNEL_M: int
    
    COLOR_CHANNEL_Y: int
    
    COLOR_CHANNEL_K: int
    
    COLOR_CHANNEL_LAST: int
    

class ColorMapType(Enum):
    
    DEFAULT: int
    
    BRUSH: int
    

class ColorMatrixFlag(Enum):
    
    DEFAULT: int
    
    SKIP_GRAYS: int
    
    ALT_GRAYS: int
    

class ColorMode(Enum):
    
    ARGB_32_MODE: int
    
    ARGB_64_MODE: int
    

class EmfPlusRecordType(Enum):
    
    WMF_RECORD_BASE: int
    
    WMF_SET_BK_COLOR: int
    
    WMF_SET_BK_MODE: int
    
    WMF_SET_MAP_MODE: int
    
    WMF_SET_ROP2: int
    
    WMF_SET_REL_ABS: int
    
    WMF_SET_POLY_FILL_MODE: int
    
    WMF_SET_STRETCH_BLT_MODE: int
    
    WMF_SET_TEXT_CHAR_EXTRA: int
    
    WMF_SET_TEXT_COLOR: int
    
    WMF_SET_TEXT_JUSTIFICATION: int
    
    WMF_SET_WINDOW_ORG: int
    
    WMF_SET_WINDOW_EXT: int
    
    WMF_SET_VIEWPORT_ORG: int
    
    WMF_SET_VIEWPORT_EXT: int
    
    WMF_OFFSET_WINDOW_ORG: int
    
    WMF_SCALE_WINDOW_EXT: int
    
    WMF_OFFSET_VIEWPORT_ORG: int
    
    WMF_SCALE_VIEWPORT_EXT: int
    
    WMF_LINE_TO: int
    
    WMF_MOVE_TO: int
    
    WMF_EXCLUDE_CLIP_RECT: int
    
    WMF_INTERSECT_CLIP_RECT: int
    
    WMF_ARC: int
    
    WMF_ELLIPSE: int
    
    WMF_FLOOD_FILL: int
    
    WMF_PIE: int
    
    WMF_RECTANGLE: int
    
    WMF_ROUND_RECT: int
    
    WMF_PAT_BLT: int
    
    WMF_SAVE_DC: int
    
    WMF_SET_PIXEL: int
    
    WMF_OFFSET_CILP_RGN: int
    
    WMF_TEXT_OUT: int
    
    WMF_BIT_BLT: int
    
    WMF_STRETCH_BLT: int
    
    WMF_POLYGON: int
    
    WMF_POLYLINE: int
    
    WMF_ESCAPE: int
    
    WMF_RESTORE_DC: int
    
    WMF_FILL_REGION: int
    
    WMF_FRAME_REGION: int
    
    WMF_INVERT_REGION: int
    
    WMF_PAINT_REGION: int
    
    WMF_SELECT_CLIP_REGION: int
    
    WMF_SELECT_OBJECT: int
    
    WMF_SET_TEXT_ALIGN: int
    
    WMF_CHORD: int
    
    WMF_SET_MAPPER_FLAGS: int
    
    WMF_EXT_TEXT_OUT: int
    
    WMF_SET_DIB_TO_DEV: int
    
    WMF_SELECT_PALETTE: int
    
    WMF_REALIZE_PALETTE: int
    
    WMF_ANIMATE_PALETTE: int
    
    WMF_SET_PAL_ENTRIES: int
    
    WMF_POLY_POLYGON: int
    
    WMF_RESIZE_PALETTE: int
    
    WMF_DIB_BIT_BLT: int
    
    WMF_DIB_STRETCH_BLT: int
    
    WMF_DIB_CREATE_PATTERN_BRUSH: int
    
    WMF_STRETCH_DIB: int
    
    WMF_EXT_FLOOD_FILL: int
    
    WMF_SET_LAYOUT: int
    
    WMF_DELETE_OBJECT: int
    
    WMF_CREATE_PALETTE: int
    
    WMF_CREATE_PATTERN_BRUSH: int
    
    WMF_CREATE_PEN_INDIRECT: int
    
    WMF_CREATE_FONT_INDIRECT: int
    
    WMF_CREATE_BRUSH_INDIRECT: int
    
    WMF_CREATE_REGION: int
    
    EMF_HEADER: int
    
    EMF_POLY_BEZIER: int
    
    EMF_POLYGON: int
    
    EMF_POLYLINE: int
    
    EMF_POLY_BEZIER_TO: int
    
    EMF_POLY_LINE_TO: int
    
    EMF_POLY_POLYLINE: int
    
    EMF_POLY_POLYGON: int
    
    EMF_SET_WINDOW_EXT_EX: int
    
    EMF_SET_WINDOW_ORG_EX: int
    
    EMF_SET_VIEWPORT_EXT_EX: int
    
    EMF_SET_VIEWPORT_ORG_EX: int
    
    EMF_SET_BRUSH_ORG_EX: int
    
    EMF_EOF: int
    
    EMF_SET_PIXEL_V: int
    
    EMF_SET_MAPPER_FLAGS: int
    
    EMF_SET_MAP_MODE: int
    
    EMF_SET_BK_MODE: int
    
    EMF_SET_POLY_FILL_MODE: int
    
    EMF_SET_ROP2: int
    
    EMF_SET_STRETCH_BLT_MODE: int
    
    EMF_SET_TEXT_ALIGN: int
    
    EMF_SET_COLOR_ADJUSTMENT: int
    
    EMF_SET_TEXT_COLOR: int
    
    EMF_SET_BK_COLOR: int
    
    EMF_OFFSET_CLIP_RGN: int
    
    EMF_MOVE_TO_EX: int
    
    EMF_SET_META_RGN: int
    
    EMF_EXCLUDE_CLIP_RECT: int
    
    EMF_INTERSECT_CLIP_RECT: int
    
    EMF_SCALE_VIEWPORT_EXT_EX: int
    
    EMF_SCALE_WINDOW_EXT_EX: int
    
    EMF_SAVE_DC: int
    
    EMF_RESTORE_DC: int
    
    EMF_SET_WORLD_TRANSFORM: int
    
    EMF_MODIFY_WORLD_TRANSFORM: int
    
    EMF_SELECT_OBJECT: int
    
    EMF_CREATE_PEN: int
    
    EMF_CREATE_BRUSH_INDIRECT: int
    
    EMF_DELETE_OBJECT: int
    
    EMF_ANGLE_ARC: int
    
    EMF_ELLIPSE: int
    
    EMF_RECTANGLE: int
    
    EMF_ROUND_RECT: int
    
    EMF_ROUND_ARC: int
    
    EMF_CHORD: int
    
    EMF_PIE: int
    
    EMF_SELECT_PALETTE: int
    
    EMF_CREATE_PALETTE: int
    
    EMF_SET_PALETTE_ENTRIES: int
    
    EMF_RESIZE_PALETTE: int
    
    EMF_REALIZE_PALETTE: int
    
    EMF_EXT_FLOOD_FILL: int
    
    EMF_LINE_TO: int
    
    EMF_ARC_TO: int
    
    EMF_POLY_DRAW: int
    
    EMF_SET_ARC_DIRECTION: int
    
    EMF_SET_MITER_LIMIT: int
    
    EMF_BEGIN_PATH: int
    
    EMF_END_PATH: int
    
    EMF_CLOSE_FIGURE: int
    
    EMF_FILL_PATH: int
    
    EMF_STROKE_AND_FILL_PATH: int
    
    EMF_STROKE_PATH: int
    
    EMF_FLATTEN_PATH: int
    
    EMF_WIDEN_PATH: int
    
    EMF_SELECT_CLIP_PATH: int
    
    EMF_ABORT_PATH: int
    
    EMF_RESERVED069: int
    
    EMF_GDI_COMMENT: int
    
    EMF_FILL_RGN: int
    
    EMF_FRAME_RGN: int
    
    EMF_INVERT_RGN: int
    
    EMF_PAINT_RGN: int
    
    EMF_EXT_SELECT_CLIP_RGN: int
    
    EMF_BIT_BLT: int
    
    EMF_STRETCH_BLT: int
    
    EMF_MASK_BLT: int
    
    EMF_PLG_BLT: int
    
    EMF_SET_DI_BITS_TO_DEVICE: int
    
    EMF_STRETCH_DI_BITS: int
    
    EMF_EXT_CREATE_FONT_INDIRECT: int
    
    EMF_EXT_TEXT_OUT_A: int
    
    EMF_EXT_TEXT_OUT_W: int
    
    EMF_POLY_BEZIER16: int
    
    EMF_POLYGON16: int
    
    EMF_POLYLINE16: int
    
    EMF_POLY_BEZIER_TO16: int
    
    EMF_POLYLINE_TO16: int
    
    EMF_POLY_POLYLINE16: int
    
    EMF_POLY_POLYGON16: int
    
    EMF_POLY_DRAW16: int
    
    EMF_CREATE_MONO_BRUSH: int
    
    EMF_CREATE_DIB_PATTERN_BRUSH_PT: int
    
    EMF_EXT_CREATE_PEN: int
    
    EMF_POLY_TEXT_OUT_A: int
    
    EMF_POLY_TEXT_OUT_W: int
    
    EMF_SET_ICM_MODE: int
    
    EMF_CREATE_COLOR_SPACE: int
    
    EMF_SET_COLOR_SPACE: int
    
    EMF_DELETE_COLOR_SPACE: int
    
    EMF_GLS_RECORD: int
    
    EMF_GLS_BOUNDED_RECORD: int
    
    EMF_PIXEL_FORMAT: int
    
    EMF_DRAW_ESCAPE: int
    
    EMF_EXT_ESCAPE: int
    
    EMF_START_DOC: int
    
    EMF_SMALL_TEXT_OUT: int
    
    EMF_FORCE_UFI_MAPPING: int
    
    EMF_NAMED_ESCPAE: int
    
    EMF_COLOR_CORRECT_PALETTE: int
    
    EMF_SET_ICM_PROFILE_A: int
    
    EMF_SET_ICM_PROFILE_W: int
    
    EMF_ALPHA_BLEND: int
    
    EMF_SET_LAYOUT: int
    
    EMF_TRANSPARENT_BLT: int
    
    EMF_RESERVED117: int
    
    EMF_GRADIENT_FILL: int
    
    EMF_SET_LINKED_UFIS: int
    
    EMF_SET_TEXT_JUSTIFICATION: int
    
    EMF_COLOR_MATCH_TO_TARGET_W: int
    
    EMF_CREATE_COLOR_SPACE_W: int
    
    EMF_MAX: int
    
    EMF_MIN: int
    
    EMF_PLUS_RECORD_BASE: int
    
    INVALID: int
    
    HEADER: int
    
    END_OF_FILE: int
    
    COMMENT: int
    
    GET_DC: int
    
    MULTI_FORMAT_START: int
    
    MULTI_FORMAT_SECTION: int
    
    MULTI_FORMAT_END: int
    
    OBJECT: int
    
    CLEAR: int
    
    FILL_RECTS: int
    
    DRAW_RECTS: int
    
    FILL_POLYGON: int
    
    DRAW_LINES: int
    
    FILL_ELLIPSE: int
    
    DRAW_ELLIPSE: int
    
    FILL_PIE: int
    
    DRAW_PIE: int
    
    DRAW_ARC: int
    
    FILL_REGION: int
    
    FILL_PATH: int
    
    DRAW_PATH: int
    
    FILL_CLOSED_CURVE: int
    
    DRAW_CLOSED_CURVE: int
    
    DRAW_CURVE: int
    
    DRAW_BEZIERS: int
    
    DRAW_IMAGE: int
    
    DRAW_IMAGE_POINTS: int
    
    DRAW_STRING: int
    
    SET_RENDERING_ORIGIN: int
    
    SET_ANTI_ALIAS_MODE: int
    
    SET_TEXT_RENDERING_HINT: int
    
    SET_TEXT_CONTRAST: int
    
    SET_INTERPOLATION_MODE: int
    
    SET_PIXEL_OFFSET_MODE: int
    
    SET_COMPOSITING_MODE: int
    
    SET_COMPOSITING_QUALITY: int
    
    SAVE: int
    
    RESTORE: int
    
    BEGIN_CONTAINER: int
    
    BEGIN_CONTAINER_NO_PARAMS: int
    
    END_CONTAINER: int
    
    SET_WORLD_TRANSFORM: int
    
    RESET_WORLD_TRANSFORM: int
    
    MULTIPLY_WORLD_TRANSFORM: int
    
    TRANSLATE_WORLD_TRANSFORM: int
    
    SCALE_WORLD_TRANSFORM: int
    
    ROTATE_WORLD_TRANSFORM: int
    
    SET_PAGE_TRANSFORM: int
    
    RESET_CLIP: int
    
    SET_CLIP_RECT: int
    
    SET_CLIP_PATH: int
    
    SET_CLIP_REGION: int
    
    OFFSET_CLIP: int
    
    DRAW_DRIVER_STRING: int
    
    TOTAL: int
    
    MAX: int
    
    MIN: int
    

class EmfType(Enum):
    
    EMF_ONLY: int
    
    EMF_PLUS_ONLY: int
    
    EMF_PLUS_DUAL: int
    

class EncoderParameterValueType(Enum):
    
    VALUE_TYPE_BYTE: int
    
    VALUE_TYPE_ASCII: int
    
    VALUE_TYPE_SHORT: int
    
    VALUE_TYPE_LONG: int
    
    VALUE_TYPE_RATIONAL: int
    
    VALUE_TYPE_LONG_RANGE: int
    
    VALUE_TYPE_UNDEFINED: int
    
    VALUE_TYPE_RATIONAL_RANGE: int
    
    VALUE_TYPE_POINTER: int
    

class EncoderValue(Enum):
    
    COLOR_TYPE_CMYK: int
    
    COLOR_TYPE_YCCK: int
    
    COMPRESSION_LZW: int
    
    COMPRESSION_CCITT3: int
    
    COMPRESSION_CCITT4: int
    
    COMPRESSION_RLE: int
    
    COMPRESSION_NONE: int
    
    SCAN_METHOD_INTERLACED: int
    
    SCAN_METHOD_NON_INTERLACED: int
    
    VERSION_GIF87: int
    
    VERSION_GIF89: int
    
    RENDER_PROGRESSIVE: int
    
    RENDER_NON_PROGRESSIVE: int
    
    TRANSFORM_ROTATE90: int
    
    TRANSFORM_ROTATE180: int
    
    TRANSFORM_ROTATE270: int
    
    TRANSFORM_FLIP_HORIZONTAL: int
    
    TRANSFORM_FLIP_VERTICAL: int
    
    MULTI_FRAME: int
    
    LAST_FRAME: int
    
    FLUSH: int
    
    FRAME_DIMENSION_TIME: int
    
    FRAME_DIMENSION_RESOLUTION: int
    
    FRAME_DIMENSION_PAGE: int
    

class ImageCodecFlags(Enum):
    
    ENCODER: int
    
    DECODER: int
    
    SUPPORT_BITMAP: int
    
    SUPPORT_VECTOR: int
    
    SEEKABLE_ENCODE: int
    
    BLOCKING_DECODE: int
    
    BUILTIN: int
    
    SYSTEM: int
    
    USER: int
    

class ImageFlags(Enum):
    
    NONE: int
    
    SCALABLE: int
    
    HAS_ALPHA: int
    
    HAS_TRANSLUCENT: int
    
    PARTIALLY_SCALABLE: int
    
    COLOR_SPACE_RGB: int
    
    COLOR_SPACE_CMYK: int
    
    COLOR_SPACE_GRAY: int
    
    COLOR_SPACE_YCBCR: int
    
    COLOR_SPACE_YCCK: int
    
    HAS_REAL_DPI: int
    
    HAS_REAL_PIXEL_SIZE: int
    
    READ_ONLY: int
    
    CACHING: int
    

class ImageLockMode(Enum):
    
    READ_ONLY: int
    
    WRITE_ONLY: int
    
    READ_WRITE: int
    
    USER_INPUT_BUFFER: int
    

class MetafileType(Enum):
    
    INVALID: int
    
    WMF: int
    
    WMF_PLACEABLE: int
    
    EMF: int
    
    EMF_PLUS_ONLY: int
    
    EMF_PLUS_DUAL: int
    

class PaletteFlags(Enum):
    
    HAS_ALPHA: int
    
    GRAY_SCALE: int
    
    HALFTONE: int
    

class PixelFormat(Enum):
    
    INDEXED: int
    
    GDI: int
    
    ALPHA: int
    
    P_ALPHA: int
    
    EXTENDED: int
    
    CANONICAL: int
    
    UNDEFINED: int
    
    DONT_CARE: int
    
    FORMAT_1BPP_INDEXED: int
    
    FORMAT_4BPP_INDEXED: int
    
    FORMAT_8BPP_INDEXED: int
    
    FORMAT_16BPP_GRAY_SCALE: int
    
    FORMAT_16BPP_RGB_555: int
    
    FORMAT_16BPP_RGB_565: int
    
    FORMAT_16BPP_ARGB_1555: int
    
    FORMAT_24BPP_RGB: int
    
    FORMAT_32BPP_RGB: int
    
    FORMAT_32BPP_ARGB: int
    
    FORMAT_32BPP_P_ARGB: int
    
    FORMAT_48BPP_RGB: int
    
    FORMAT_64BPP_ARGB: int
    
    FORMAT_64BPP_P_ARGB: int
    
    MAX: int
    

class MetafileFrameUnit(Enum):
    
    PIXEL: int
    
    POINT: int
    
    INCH: int
    
    DOCUMENT: int
    
    MILLIMETER: int
    
    GDI_COMPATIBLE: int
    

