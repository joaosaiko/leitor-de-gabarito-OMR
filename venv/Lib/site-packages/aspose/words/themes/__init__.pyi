import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List
from enum import Enum

class Theme:
    """Represents document Theme, and provides access to main theme parts including :attr:`Theme.major_fonts`, :attr:`Theme.minor_fonts` and :attr:`Theme.colors`
    To learn more, visit the `Working with Styles and Themes <https://docs.aspose.com/words/python-net/working-with-styles-and-themes/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def major_fonts(self) -> aspose.words.themes.ThemeFonts:
        """Allows to specify the set of major fonts for different languages."""
        ...
    
    @property
    def minor_fonts(self) -> aspose.words.themes.ThemeFonts:
        """Allows to specify the set of minor fonts for different languages."""
        ...
    
    @property
    def colors(self) -> aspose.words.themes.ThemeColors:
        """Allows to specify the set of theme colors for the document."""
        ...
    
    ...

class ThemeColors:
    """Represents the color scheme of the document theme which contains twelve colors.
    
    :class:`ThemeColors` object contains six accent colors, two dark colors, two light colors
    and a color for each of a hyperlink and followed hyperlink."""
    
    @property
    def accent1(self) -> aspose.pydrawing.Color:
        """Specifies color Accent 1."""
        ...
    
    @accent1.setter
    def accent1(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def accent2(self) -> aspose.pydrawing.Color:
        """Specifies color Accent 2."""
        ...
    
    @accent2.setter
    def accent2(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def accent3(self) -> aspose.pydrawing.Color:
        """Specifies color Accent 3."""
        ...
    
    @accent3.setter
    def accent3(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def accent4(self) -> aspose.pydrawing.Color:
        """Specifies color Accent 4."""
        ...
    
    @accent4.setter
    def accent4(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def accent5(self) -> aspose.pydrawing.Color:
        """Specifies color Accent 5."""
        ...
    
    @accent5.setter
    def accent5(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def accent6(self) -> aspose.pydrawing.Color:
        """Specifies color Accent 6."""
        ...
    
    @accent6.setter
    def accent6(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def dark1(self) -> aspose.pydrawing.Color:
        """Specifies color Dark 1."""
        ...
    
    @dark1.setter
    def dark1(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def dark2(self) -> aspose.pydrawing.Color:
        """Specifies color Dark 2."""
        ...
    
    @dark2.setter
    def dark2(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def followed_hyperlink(self) -> aspose.pydrawing.Color:
        """Specifies color for a clicked hyperlink."""
        ...
    
    @followed_hyperlink.setter
    def followed_hyperlink(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def hyperlink(self) -> aspose.pydrawing.Color:
        """Specifies color for a hyperlink."""
        ...
    
    @hyperlink.setter
    def hyperlink(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def light1(self) -> aspose.pydrawing.Color:
        """Specifies color Light 1."""
        ...
    
    @light1.setter
    def light1(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def light2(self) -> aspose.pydrawing.Color:
        """Specifies color Light 2."""
        ...
    
    @light2.setter
    def light2(self, value: aspose.pydrawing.Color):
        ...
    
    ...

class ThemeFonts:
    """Represents a collection of fonts in the font scheme, allowing to specify different fonts for different languages :attr:`ThemeFonts.latin`, :attr:`ThemeFonts.east_asian` and :attr:`ThemeFonts.complex_script`.
    To learn more, visit the `Working with Styles and Themes <https://docs.aspose.com/words/python-net/working-with-styles-and-themes/>` documentation article."""
    
    @property
    def latin(self) -> str:
        """Specifies font name for Latin characters."""
        ...
    
    @latin.setter
    def latin(self, value: str):
        ...
    
    @property
    def east_asian(self) -> str:
        """Specifies font name for EastAsian characters."""
        ...
    
    @east_asian.setter
    def east_asian(self, value: str):
        ...
    
    @property
    def complex_script(self) -> str:
        """Specifies font name for ComplexScript characters."""
        ...
    
    @complex_script.setter
    def complex_script(self, value: str):
        ...
    
    ...

class ThemeColor(Enum):
    """Specifies the theme colors for document themes.
    To learn more, visit the `Working with Styles and Themes <https://docs.aspose.com/words/python-net/working-with-styles-and-themes/>` documentation article.
    
    The specified theme color is a reference to one of the predefined theme colors, located in the
    document's Theme part, which allows color information to be set centrally in the document."""
    
    """No color."""
    NONE: int
    
    """Dark main color 1."""
    DARK1: int
    
    """Light main color 1."""
    LIGHT1: int
    
    """Dark main color 2."""
    DARK2: int
    
    """Light main color 2."""
    LIGHT2: int
    
    """Accent color 1."""
    ACCENT1: int
    
    """Accent color 2."""
    ACCENT2: int
    
    """Accent color 3."""
    ACCENT3: int
    
    """Accent color 4."""
    ACCENT4: int
    
    """Accent color 5."""
    ACCENT5: int
    
    """Accent color 6."""
    ACCENT6: int
    
    """Hyperlink color."""
    HYPERLINK: int
    
    """Followed hyperlink color."""
    FOLLOWED_HYPERLINK: int
    
    """Text color 1."""
    TEXT1: int
    
    """Text color 2."""
    TEXT2: int
    
    """Background color 1."""
    BACKGROUND1: int
    
    """Background color 2."""
    BACKGROUND2: int
    

class ThemeFont(Enum):
    """Specifies the types of theme font names for document themes.
    
    Specifies a theme font type which can be referenced as a theme font within the parent object properties.
    This theme font is a reference to one of the predefined theme fonts, located in the document's
    Theme part, which allows for font information to be set centrally in the document."""
    
    """No theme font."""
    NONE: int
    
    """Major theme font."""
    MAJOR: int
    
    """Minor theme font."""
    MINOR: int
    

