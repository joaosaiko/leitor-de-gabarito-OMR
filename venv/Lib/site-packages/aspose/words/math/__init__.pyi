import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List
from enum import Enum

class OfficeMath(aspose.words.CompositeNode):
    """Represents an Office Math object such as function, equation, matrix or alike. Can contain child elements
    including runs of mathematical text, bookmarks, comments, other :class:`OfficeMath` instances and some other nodes.
    To learn more, visit the `Working with OfficeMath <https://docs.aspose.com/words/python-net/working-with-officemath/>` documentation article.
    
    In this version of Aspose.Words, :class:`OfficeMath` nodes do not provide public methods
    and properties to create or modify a :class:`OfficeMath` object. In this version you are not able to instantiate
    :mod:`aspose.words.math` nodes or modify existing except deleting them.
    
    :class:`OfficeMath` can only be a child of :class:`aspose.words.Paragraph`."""
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`aspose.words.DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`aspose.words.DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`aspose.words.DocumentVisitor.visit_office_math_start`, then calls :meth:`aspose.words.Node.accept` for all
        child nodes of the Office Math and calls :meth:`aspose.words.DocumentVisitor.visit_office_math_end` at the end."""
        ...
    
    def accept_start(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """Accepts a visitor for visiting the start of the office math.
        
        :param visitor: The document visitor.
        :returns: The action to be taken by the visitor."""
        ...
    
    def accept_end(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """Accepts a visitor for visiting the end of the office math.
        
        :param visitor: The document visitor.
        :returns: The action to be taken by the visitor."""
        ...
    
    def get_math_renderer(self) -> aspose.words.rendering.OfficeMathRenderer:
        """Creates and returns an object that can be used to render this equation into an image.
        
        This method just invokes the :class:`aspose.words.rendering.OfficeMathRenderer` constructor and passes
        this object as a parameter.
        
        :returns: The renderer object for this equation."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`aspose.words.NodeType.OFFICE_MATH`."""
        ...
    
    @property
    def parent_paragraph(self) -> aspose.words.Paragraph:
        """Retrieves the parent :class:`aspose.words.Paragraph` of this node."""
        ...
    
    @property
    def math_object_type(self) -> aspose.words.math.MathObjectType:
        """Gets type :attr:`OfficeMath.math_object_type` of this Office Math object."""
        ...
    
    @property
    def justification(self) -> aspose.words.math.OfficeMathJustification:
        """Gets/sets Office Math justification.
        
        Justification cannot be set to the Office Math with display format type :attr:`OfficeMathDisplayType.INLINE`.
        
        Inline justification cannot be set to the Office Math with display format type :attr:`OfficeMathDisplayType.DISPLAY`.
        
        Corresponding :attr:`OfficeMath.display_type` has to be set before setting Office Math justification."""
        ...
    
    @justification.setter
    def justification(self, value: aspose.words.math.OfficeMathJustification):
        ...
    
    @property
    def display_type(self) -> aspose.words.math.OfficeMathDisplayType:
        """Gets/sets Office Math display format type which represents whether an equation is displayed inline with the text
        or displayed on its own line.
        
        Display format type has effect for top level Office Math only.
        
        Returned display format type is always :attr:`OfficeMathDisplayType.INLINE` for nested Office Math."""
        ...
    
    @display_type.setter
    def display_type(self, value: aspose.words.math.OfficeMathDisplayType):
        ...
    
    ...

class MathObjectType(Enum):
    """Specifies type of an Office Math object."""
    
    """Instance of mathematical text."""
    O_MATH: int
    
    """Math paragraph, or display math zone, that contains one or more :attr:`MathObjectType.O_MATH` elements that are in display mode."""
    O_MATH_PARA: int
    
    """Accent function, consisting of a base and a combining diacritical mark."""
    ACCENT: int
    
    """Bar function, consisting of a base argument and an overbar or underbar."""
    BAR: int
    
    """Border Box object, consisting of a border drawn around an instance of mathematical text (such as a formula or equation)"""
    BORDER_BOX: int
    
    """Box object, which is used to group components of an equation or other instance of mathematical text."""
    BOX: int
    
    """Delimiter object, consisting of opening and closing delimiters (such as parentheses,
    braces, brackets, and vertical bars), and an element contained inside."""
    DELIMITER: int
    
    """Degree in the mathematical radical."""
    DEGREE: int
    
    """Argument object. Encloses Office Math entities when they are used as arguments to other Office Math entities."""
    ARGUMENT: int
    
    """Array object, consisting of one or more equations, expressions, or other mathematical text runs
    that can be vertically justified as a unit with respect to surrounding text on the line."""
    ARRAY: int
    
    """Fraction object, consisting of a numerator and denominator separated by a fraction bar."""
    FRACTION: int
    
    """Denominator of a fraction object."""
    DENOMINATOR: int
    
    """Numerator of the Fraction object."""
    NUMERATOR: int
    
    """Function-Apply object, which consists of a function name and an argument element acted upon."""
    FUNCTION: int
    
    """Name of the function. For example, function names are sin and cos."""
    FUNCTION_NAME: int
    
    """Group-Character object, consisting of a character drawn above or below text, often
    with the purpose of visually grouping items"""
    GROUP_CHARACTER: int
    
    """Lower limit of the :attr:`MathObjectType.LOWER_LIMIT` object and
    the upper limit of the :attr:`MathObjectType.UPPER_LIMIT` function."""
    LIMIT: int
    
    """Lower-Limit object, consisting of text on the baseline and reduced-size text immediately below it."""
    LOWER_LIMIT: int
    
    """Upper-Limit object, consisting of text on the baseline and reduced-size text immediately above it."""
    UPPER_LIMIT: int
    
    """Matrix object, consisting of one or more elements laid out in one or more rows and one or more columns."""
    MATRIX: int
    
    """Single row of the matrix."""
    MATRIX_ROW: int
    
    """N-ary object, consisting of an n-ary object, a base (or operand), and optional upper and lower limits."""
    N_ARY: int
    
    """Phantom object."""
    PHANTOM: int
    
    """Radical object, consisting of a radical, a base element, and an optional degree ."""
    RADICAL: int
    
    """Subscript of the object that can have subscript part."""
    SUBSCRIPT_PART: int
    
    """Superscript of the superscript object."""
    SUPERSCRIPT_PART: int
    
    """Pre-Sub-Superscript object, which consists of a base element and a subscript and superscript placed to the left of the base."""
    PRE_SUB_SUPERSCRIPT: int
    
    """Subscript object, which consists of a base element and a reduced-size script placed below and to the right."""
    SUBSCRIPT: int
    
    """Sub-superscript object, which consists of a base element, a reduced-size script placed below and to the right, and a reduced-size script placed above and to the right."""
    SUB_SUPERSCRIPT: int
    
    """Superscript object, which consists of a base element and a reduced-size script placed above and to the right."""
    SUPERCRIPT: int
    

class OfficeMathDisplayType(Enum):
    """Specifies the display format type of the equation."""
    
    """The Office Math is displayed on its own line."""
    DISPLAY: int
    
    """The Office Math is displayed inline with the text."""
    INLINE: int
    

class OfficeMathJustification(Enum):
    """Specifies the justification of the equation."""
    
    """Justifies instances of mathematical text to the left with respect to each other, and centers the group of mathematical
    text (the Math Paragraph) with respect to the page."""
    CENTER_GROUP: int
    
    """Centers each instance of mathematical text individually with respect to margins."""
    CENTER: int
    
    """Left justification of Math Paragraph."""
    LEFT: int
    
    """Right Justification of Math Paragraph."""
    RIGHT: int
    
    """Inline position of Math."""
    INLINE: int
    
    """Default value :attr:`OfficeMathJustification.CENTER_GROUP`."""
    DEFAULT: int
    

