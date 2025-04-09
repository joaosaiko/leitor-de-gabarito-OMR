import aspose.pydrawing
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable
from enum import Enum

class PreviewPageInfo:
    
    def __init__(self, image: aspose.pydrawing.Image, physical_size: aspose.pydrawing.Size):
        ...
    
    @property
    def image(self) -> aspose.pydrawing.Image:
        ...
    
    @property
    def physical_size(self) -> aspose.pydrawing.Size:
        ...
    
    ...

class PreviewPrintController:
    
    def __init__(self):
        ...
    
    def on_start_page(self, document: aspose.pydrawing.printing.PrintDocument, e: aspose.pydrawing.printing.PrintPageEventArgs) -> aspose.pydrawing.Graphics:
        ...
    
    def on_end_page(self, document: aspose.pydrawing.printing.PrintDocument, e: aspose.pydrawing.printing.PrintPageEventArgs) -> None:
        ...
    
    def on_start_print(self, document: aspose.pydrawing.printing.PrintDocument, e: aspose.pydrawing.printing.PrintEventArgs) -> None:
        ...
    
    def on_end_print(self, document: aspose.pydrawing.printing.PrintDocument, e: aspose.pydrawing.printing.PrintEventArgs) -> None:
        ...
    
    def get_preview_page_info(self) -> list[aspose.pydrawing.printing.PreviewPageInfo]:
        ...
    
    @property
    def is_preview(self) -> bool:
        ...
    
    @property
    def use_anti_alias(self) -> bool:
        ...
    
    @use_anti_alias.setter
    def use_anti_alias(self, value: bool):
        ...
    
    ...

class PrintController:
    
    def on_start_page(self, document: aspose.pydrawing.printing.PrintDocument, e: aspose.pydrawing.printing.PrintPageEventArgs) -> aspose.pydrawing.Graphics:
        ...
    
    def on_end_page(self, document: aspose.pydrawing.printing.PrintDocument, e: aspose.pydrawing.printing.PrintPageEventArgs) -> None:
        ...
    
    def on_start_print(self, document: aspose.pydrawing.printing.PrintDocument, e: aspose.pydrawing.printing.PrintEventArgs) -> None:
        ...
    
    def on_end_print(self, document: aspose.pydrawing.printing.PrintDocument, e: aspose.pydrawing.printing.PrintEventArgs) -> None:
        ...
    
    @property
    def is_preview(self) -> bool:
        ...
    
    ...

class QueryPageSettingsEventArgs:
    
    def __init__(self, page_settings: aspose.pydrawing.printing.PageSettings):
        ...
    
    @property
    def print_action(self) -> aspose.pydrawing.printing.PrintAction:
        ...
    
    @property
    def page_settings(self) -> aspose.pydrawing.printing.PageSettings:
        ...
    
    @page_settings.setter
    def page_settings(self, value: aspose.pydrawing.printing.PageSettings):
        ...
    
    ...

class InvalidPrinterException(RuntimeError):
    
    def __init__(self, settings: aspose.pydrawing.printing.PrinterSettings):
        ...
    
    ...

class Margins:
    
    @overload
    def __init__(self):
        ...
    
    @overload
    def __init__(self, left: int, right: int, top: int, bottom: int):
        ...
    
    def clone(self) -> object:
        ...
    
    @property
    def left(self) -> int:
        ...
    
    @left.setter
    def left(self, value: int):
        ...
    
    @property
    def right(self) -> int:
        ...
    
    @right.setter
    def right(self, value: int):
        ...
    
    @property
    def top(self) -> int:
        ...
    
    @top.setter
    def top(self, value: int):
        ...
    
    @property
    def bottom(self) -> int:
        ...
    
    @bottom.setter
    def bottom(self, value: int):
        ...
    
    ...

class MarginsConverter:
    
    def __init__(self):
        ...
    
    ...

class PaperSize:
    
    @overload
    def __init__(self):
        ...
    
    @overload
    def __init__(self, name: str, width: int, height: int):
        ...
    
    @property
    def height(self) -> int:
        ...
    
    @height.setter
    def height(self, value: int):
        ...
    
    @property
    def kind(self) -> aspose.pydrawing.printing.PaperKind:
        ...
    
    @property
    def paper_name(self) -> str:
        ...
    
    @paper_name.setter
    def paper_name(self, value: str):
        ...
    
    @property
    def raw_kind(self) -> int:
        ...
    
    @raw_kind.setter
    def raw_kind(self, value: int):
        ...
    
    @property
    def width(self) -> int:
        ...
    
    @width.setter
    def width(self, value: int):
        ...
    
    ...

class PaperSource:
    
    def __init__(self):
        ...
    
    @property
    def kind(self) -> aspose.pydrawing.printing.PaperSourceKind:
        ...
    
    @property
    def raw_kind(self) -> int:
        ...
    
    @raw_kind.setter
    def raw_kind(self, value: int):
        ...
    
    @property
    def source_name(self) -> str:
        ...
    
    @source_name.setter
    def source_name(self, value: str):
        ...
    
    ...

class PrinterResolution:
    
    def __init__(self):
        ...
    
    @property
    def kind(self) -> aspose.pydrawing.printing.PrinterResolutionKind:
        ...
    
    @kind.setter
    def kind(self, value: aspose.pydrawing.printing.PrinterResolutionKind):
        ...
    
    @property
    def x(self) -> int:
        ...
    
    @x.setter
    def x(self, value: int):
        ...
    
    @property
    def y(self) -> int:
        ...
    
    @y.setter
    def y(self, value: int):
        ...
    
    ...

class PrinterUnitConvert:
    
    @overload
    @staticmethod
    def convert(value: float, from_unit: aspose.pydrawing.printing.PrinterUnit, to_unit: aspose.pydrawing.printing.PrinterUnit) -> float:
        ...
    
    @overload
    @staticmethod
    def convert(value: int, from_unit: aspose.pydrawing.printing.PrinterUnit, to_unit: aspose.pydrawing.printing.PrinterUnit) -> int:
        ...
    
    @overload
    @staticmethod
    def convert(value: aspose.pydrawing.Point, from_unit: aspose.pydrawing.printing.PrinterUnit, to_unit: aspose.pydrawing.printing.PrinterUnit) -> aspose.pydrawing.Point:
        ...
    
    @overload
    @staticmethod
    def convert(value: aspose.pydrawing.Size, from_unit: aspose.pydrawing.printing.PrinterUnit, to_unit: aspose.pydrawing.printing.PrinterUnit) -> aspose.pydrawing.Size:
        ...
    
    @overload
    @staticmethod
    def convert(value: aspose.pydrawing.Rectangle, from_unit: aspose.pydrawing.printing.PrinterUnit, to_unit: aspose.pydrawing.printing.PrinterUnit) -> aspose.pydrawing.Rectangle:
        ...
    
    @overload
    @staticmethod
    def convert(value: aspose.pydrawing.printing.Margins, from_unit: aspose.pydrawing.printing.PrinterUnit, to_unit: aspose.pydrawing.printing.PrinterUnit) -> aspose.pydrawing.printing.Margins:
        ...
    
    ...

class StandardPrintController:
    
    def __init__(self):
        ...
    
    def on_start_page(self, document: aspose.pydrawing.printing.PrintDocument, e: aspose.pydrawing.printing.PrintPageEventArgs) -> aspose.pydrawing.Graphics:
        ...
    
    def on_end_page(self, document: aspose.pydrawing.printing.PrintDocument, e: aspose.pydrawing.printing.PrintPageEventArgs) -> None:
        ...
    
    def on_start_print(self, document: aspose.pydrawing.printing.PrintDocument, e: aspose.pydrawing.printing.PrintEventArgs) -> None:
        ...
    
    def on_end_print(self, document: aspose.pydrawing.printing.PrintDocument, e: aspose.pydrawing.printing.PrintEventArgs) -> None:
        ...
    
    @property
    def is_preview(self) -> bool:
        ...
    
    ...

class PageSettings:
    
    @overload
    def __init__(self):
        ...
    
    @overload
    def __init__(self, printer_settings: aspose.pydrawing.printing.PrinterSettings):
        ...
    
    def clone(self) -> object:
        ...
    
    @property
    def bounds(self) -> aspose.pydrawing.Rectangle:
        ...
    
    @property
    def color(self) -> bool:
        ...
    
    @color.setter
    def color(self, value: bool):
        ...
    
    @property
    def hard_margin_x(self) -> float:
        ...
    
    @property
    def hard_margin_y(self) -> float:
        ...
    
    @property
    def landscape(self) -> bool:
        ...
    
    @landscape.setter
    def landscape(self, value: bool):
        ...
    
    @property
    def margins(self) -> aspose.pydrawing.printing.Margins:
        ...
    
    @margins.setter
    def margins(self, value: aspose.pydrawing.printing.Margins):
        ...
    
    @property
    def paper_size(self) -> aspose.pydrawing.printing.PaperSize:
        ...
    
    @paper_size.setter
    def paper_size(self, value: aspose.pydrawing.printing.PaperSize):
        ...
    
    @property
    def paper_source(self) -> aspose.pydrawing.printing.PaperSource:
        ...
    
    @paper_source.setter
    def paper_source(self, value: aspose.pydrawing.printing.PaperSource):
        ...
    
    @property
    def printable_area(self) -> aspose.pydrawing.RectangleF:
        ...
    
    @property
    def printer_resolution(self) -> aspose.pydrawing.printing.PrinterResolution:
        ...
    
    @printer_resolution.setter
    def printer_resolution(self, value: aspose.pydrawing.printing.PrinterResolution):
        ...
    
    @property
    def printer_settings(self) -> aspose.pydrawing.printing.PrinterSettings:
        ...
    
    @printer_settings.setter
    def printer_settings(self, value: aspose.pydrawing.printing.PrinterSettings):
        ...
    
    ...

class PrintDocument:
    
    def __init__(self):
        ...
    
    def print(self) -> None:
        ...
    
    @property
    def default_page_settings(self) -> aspose.pydrawing.printing.PageSettings:
        ...
    
    @default_page_settings.setter
    def default_page_settings(self, value: aspose.pydrawing.printing.PageSettings):
        ...
    
    @property
    def document_name(self) -> str:
        ...
    
    @document_name.setter
    def document_name(self, value: str):
        ...
    
    @property
    def origin_at_margins(self) -> bool:
        ...
    
    @origin_at_margins.setter
    def origin_at_margins(self, value: bool):
        ...
    
    @property
    def print_controller(self) -> aspose.pydrawing.printing.PrintController:
        ...
    
    @print_controller.setter
    def print_controller(self, value: aspose.pydrawing.printing.PrintController):
        ...
    
    @property
    def printer_settings(self) -> aspose.pydrawing.printing.PrinterSettings:
        ...
    
    @printer_settings.setter
    def printer_settings(self, value: aspose.pydrawing.printing.PrinterSettings):
        ...
    
    ...

class PrinterSettings:
    
    def __init__(self):
        ...
    
    @overload
    def is_direct_printing_supported(self, image_format: aspose.pydrawing.Imaging.ImageFormat) -> bool:
        ...
    
    @overload
    def is_direct_printing_supported(self, image: aspose.pydrawing.Image) -> bool:
        ...
    
    @overload
    def create_measurement_graphics(self) -> aspose.pydrawing.Graphics:
        ...
    
    @overload
    def create_measurement_graphics(self, honor_origin_at_margins: bool) -> aspose.pydrawing.Graphics:
        ...
    
    @overload
    def create_measurement_graphics(self, page_settings: aspose.pydrawing.printing.PageSettings) -> aspose.pydrawing.Graphics:
        ...
    
    @overload
    def create_measurement_graphics(self, page_settings: aspose.pydrawing.printing.PageSettings, honor_origin_at_margins: bool) -> aspose.pydrawing.Graphics:
        ...
    
    def clone(self) -> object:
        ...
    
    @property
    def can_duplex(self) -> bool:
        ...
    
    @property
    def copies(self) -> int:
        ...
    
    @copies.setter
    def copies(self, value: int):
        ...
    
    @property
    def collate(self) -> bool:
        ...
    
    @collate.setter
    def collate(self, value: bool):
        ...
    
    @property
    def default_page_settings(self) -> aspose.pydrawing.printing.PageSettings:
        ...
    
    @property
    def duplex(self) -> aspose.pydrawing.printing.Duplex:
        ...
    
    @duplex.setter
    def duplex(self, value: aspose.pydrawing.printing.Duplex):
        ...
    
    @property
    def from_page(self) -> int:
        ...
    
    @from_page.setter
    def from_page(self, value: int):
        ...
    
    installed_printers: None
    
    @property
    def is_default_printer(self) -> bool:
        ...
    
    @property
    def is_plotter(self) -> bool:
        ...
    
    @property
    def is_valid(self) -> bool:
        ...
    
    @property
    def landscape_angle(self) -> int:
        ...
    
    @property
    def maximum_copies(self) -> int:
        ...
    
    @property
    def maximum_page(self) -> int:
        ...
    
    @maximum_page.setter
    def maximum_page(self, value: int):
        ...
    
    @property
    def minimum_page(self) -> int:
        ...
    
    @minimum_page.setter
    def minimum_page(self, value: int):
        ...
    
    @property
    def print_file_name(self) -> str:
        ...
    
    @print_file_name.setter
    def print_file_name(self, value: str):
        ...
    
    @property
    def paper_sizes(self) -> None:
        ...
    
    @property
    def paper_sources(self) -> None:
        ...
    
    @property
    def print_range(self) -> aspose.pydrawing.printing.PrintRange:
        ...
    
    @print_range.setter
    def print_range(self, value: aspose.pydrawing.printing.PrintRange):
        ...
    
    @property
    def print_to_file(self) -> bool:
        ...
    
    @print_to_file.setter
    def print_to_file(self, value: bool):
        ...
    
    @property
    def printer_name(self) -> str:
        ...
    
    @printer_name.setter
    def printer_name(self, value: str):
        ...
    
    @property
    def printer_resolutions(self) -> None:
        ...
    
    @property
    def supports_color(self) -> bool:
        ...
    
    @property
    def to_page(self) -> int:
        ...
    
    @to_page.setter
    def to_page(self, value: int):
        ...
    
    ...

class PrintEventArgs:
    
    def __init__(self):
        ...
    
    @property
    def print_action(self) -> aspose.pydrawing.printing.PrintAction:
        ...
    
    ...

class PrintPageEventArgs:
    
    def __init__(self, graphics: aspose.pydrawing.Graphics, margin_bounds: aspose.pydrawing.Rectangle, page_bounds: aspose.pydrawing.Rectangle, page_settings: aspose.pydrawing.printing.PageSettings):
        ...
    
    @property
    def cancel(self) -> bool:
        ...
    
    @cancel.setter
    def cancel(self, value: bool):
        ...
    
    @property
    def graphics(self) -> aspose.pydrawing.Graphics:
        ...
    
    @property
    def has_more_pages(self) -> bool:
        ...
    
    @has_more_pages.setter
    def has_more_pages(self, value: bool):
        ...
    
    @property
    def margin_bounds(self) -> aspose.pydrawing.Rectangle:
        ...
    
    @property
    def page_bounds(self) -> aspose.pydrawing.Rectangle:
        ...
    
    @property
    def page_settings(self) -> aspose.pydrawing.printing.PageSettings:
        ...
    
    ...

class PrinterUnit(Enum):
    
    DISPLAY: int
    
    THOUSANDTHS_OF_AN_INCH: int
    
    HUNDREDTHS_OF_A_MILLIMETER: int
    
    TENTHS_OF_A_MILLIMETER: int
    

class PrintAction(Enum):
    
    PRINT_TO_FILE: int
    
    PRINT_TO_PREVIEW: int
    
    PRINT_TO_PRINTER: int
    

class Duplex(Enum):
    
    DEFAULT: int
    
    SIMPLEX: int
    
    HORIZONTAL: int
    
    VERTICAL: int
    

class PaperKind(Enum):
    
    CUSTOM: int
    
    LETTER: int
    
    LEGAL: int
    
    A4: int
    
    C_SHEET: int
    
    D_SHEET: int
    
    E_SHEET: int
    
    LETTER_SMALL: int
    
    TABLOID: int
    
    LEDGER: int
    
    STATEMENT: int
    
    EXECUTIVE: int
    
    A3: int
    
    A4_SMALL: int
    
    A5: int
    
    B4: int
    
    B5: int
    
    FOLIO: int
    
    QUARTO: int
    
    STANDARD_10X14: int
    
    STANDARD_11X17: int
    
    NOTE: int
    
    NUMBER_9_ENVELOPE: int
    
    NUMBER_10_ENVELOPE: int
    
    NUMBER_11_ENVELOPE: int
    
    NUMBER_12_ENVELOPE: int
    
    NUMBER_14_ENVELOPE: int
    
    DL_ENVELOPE: int
    
    C5_ENVELOPE: int
    
    C3_ENVELOPE: int
    
    C4_ENVELOPE: int
    
    C6_ENVELOPE: int
    
    C65_ENVELOPE: int
    
    B4_ENVELOPE: int
    
    B5_ENVELOPE: int
    
    B6_ENVELOPE: int
    
    ITALY_ENVELOPE: int
    
    MONARCH_ENVELOPE: int
    
    PERSONAL_ENVELOPE: int
    
    US_STANDARD_FANFOLD: int
    
    GERMAN_STANDARD_FANFOLD: int
    
    GERMAN_LEGAL_FANFOLD: int
    
    ISO_B4: int
    
    JAPANESE_POSTCARD: int
    
    STANDARD_9X11: int
    
    STANDARD_10X11: int
    
    STANDARD_15X11: int
    
    INVITE_ENVELOPE: int
    
    LETTER_EXTRA: int
    
    LEGAL_EXTRA: int
    
    TABLOID_EXTRA: int
    
    A4_EXTRA: int
    
    LETTER_TRANSVERSE: int
    
    A4_TRANSVERSE: int
    
    LETTER_EXTRA_TRANSVERSE: int
    
    A_PLUS: int
    
    B_PLUS: int
    
    LETTER_PLUS: int
    
    A4_PLUS: int
    
    A5_TRANSVERSE: int
    
    B5_TRANSVERSE: int
    
    A3_EXTRA: int
    
    A5_EXTRA: int
    
    B5_EXTRA: int
    
    A2: int
    
    A3_TRANSVERSE: int
    
    A3_EXTRA_TRANSVERSE: int
    
    JAPANESE_DOUBLE_POSTCARD: int
    
    A6: int
    
    JAPANESE_ENVELOPE_KAKU_NUMBER2: int
    
    JAPANESE_ENVELOPE_KAKU_NUMBER3: int
    
    JAPANESE_ENVELOPE_CHOU_NUMBER3: int
    
    JAPANESE_ENVELOPE_CHOU_NUMBER4: int
    
    LETTER_ROTATED: int
    
    A3_ROTATED: int
    
    A4_ROTATED: int
    
    A5_ROTATED: int
    
    B4_JIS_ROTATED: int
    
    B5_JIS_ROTATED: int
    
    JAPANESE_POSTCARD_ROTATED: int
    
    JAPANESE_DOUBLE_POSTCARD_ROTATED: int
    
    A6_ROTATED: int
    
    JAPANESE_ENVELOPE_KAKU_NUMBER_2_ROTATED: int
    
    JAPANESE_ENVELOPE_KAKU_NUMBER_3_ROTATED: int
    
    JAPANESE_ENVELOPE_CHOU_NUMBER_3_ROTATED: int
    
    JAPANESE_ENVELOPE_CHOU_NUMBER_4_ROTATED: int
    
    B6_JIS: int
    
    B6_JIS_ROTATED: int
    
    STANDARD_12X11: int
    
    JAPANESE_ENVELOPE_YOU_NUMBER4: int
    
    JAPANESE_ENVELOPE_YOU_NUMBER_4_ROTATED: int
    
    PRC_16K: int
    
    PRC_32K: int
    
    PRC_32K_BIG: int
    
    PRC_ENVELOPE_NUMBER1: int
    
    PRC_ENVELOPE_NUMBER2: int
    
    PRC_ENVELOPE_NUMBER3: int
    
    PRC_ENVELOPE_NUMBER4: int
    
    PRC_ENVELOPE_NUMBER5: int
    
    PRC_ENVELOPE_NUMBER6: int
    
    PRC_ENVELOPE_NUMBER7: int
    
    PRC_ENVELOPE_NUMBER8: int
    
    PRC_ENVELOPE_NUMBER9: int
    
    PRC_ENVELOPE_NUMBER10: int
    
    PRC_16K_ROTATED: int
    
    PRC_32K_ROTATED: int
    
    PRC_32K_BIG_ROTATED: int
    
    PRC_ENVELOPE_NUMBER_1_ROTATED: int
    
    PRC_ENVELOPE_NUMBER_2_ROTATED: int
    
    PRC_ENVELOPE_NUMBER_3_ROTATED: int
    
    PRC_ENVELOPE_NUMBER_4_ROTATED: int
    
    PRC_ENVELOPE_NUMBER_5_ROTATED: int
    
    PRC_ENVELOPE_NUMBER_6_ROTATED: int
    
    PRC_ENVELOPE_NUMBER_7_ROTATED: int
    
    PRC_ENVELOPE_NUMBER_8_ROTATED: int
    
    PRC_ENVELOPE_NUMBER_9_ROTATED: int
    
    PRC_ENVELOPE_NUMBER_10_ROTATED: int
    

class PaperSourceKind(Enum):
    
    UPPER: int
    
    LOWER: int
    
    MIDDLE: int
    
    MANUAL: int
    
    ENVELOPE: int
    
    MANUAL_FEED: int
    
    AUTOMATIC_FEED: int
    
    TRACTOR_FEED: int
    
    SMALL_FORMAT: int
    
    LARGE_FORMAT: int
    
    LARGE_CAPACITY: int
    
    CASSETTE: int
    
    FORM_SOURCE: int
    
    CUSTOM: int
    

class PrinterResolutionKind(Enum):
    
    HIGH: int
    
    MEDIUM: int
    
    LOW: int
    
    DRAFT: int
    
    CUSTOM: int
    

class PrintRange(Enum):
    
    ALL_PAGES: int
    
    SOME_PAGES: int
    
    SELECTION: int
    
    CURRENT_PAGE: int
    

