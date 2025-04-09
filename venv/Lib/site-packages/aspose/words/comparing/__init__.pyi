import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List
from enum import Enum

class AdvancedCompareOptions:
    """Allows to set advanced compare options.
    
    These options have no equivalence in Microsoft Word and might help to produce more precise comparison result."""
    
    def __init__(self):
        ...
    
    @property
    def ignore_dml_unique_id(self) -> bool:
        """Specifies whether to ignore difference in DrawingML unique Id.
        
        Default value is ``False``."""
        ...
    
    @ignore_dml_unique_id.setter
    def ignore_dml_unique_id(self, value: bool):
        ...
    
    @property
    def ignore_store_item_id(self) -> bool:
        """Specifies whether to ignore difference in StructuredDocumentTag store item Id.
        
        Default value is ``False``."""
        ...
    
    @ignore_store_item_id.setter
    def ignore_store_item_id(self, value: bool):
        ...
    
    ...

class CompareOptions:
    """Allows to choose additional options for document comparison operation.
    To learn more, visit the `Compare Documents <https://docs.aspose.com/words/python-net/compare-documents/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def compare_moves(self) -> bool:
        """Specifies whether to compare differences   between the two documents.
        
        By default move revisions are not produced."""
        ...
    
    @compare_moves.setter
    def compare_moves(self, value: bool):
        ...
    
    @property
    def ignore_case_changes(self) -> bool:
        """True indicates that documents comparison is case insensitive.
        
        By default comparison is case sensitive."""
        ...
    
    @ignore_case_changes.setter
    def ignore_case_changes(self, value: bool):
        ...
    
    @property
    def ignore_tables(self) -> bool:
        """Specifies whether to compare the differences in data contained in tables.
        
        By default tables are not ignored."""
        ...
    
    @ignore_tables.setter
    def ignore_tables(self, value: bool):
        ...
    
    @property
    def ignore_fields(self) -> bool:
        """Specifies whether to compare differences in fields.
        
        By default fields are not ignored."""
        ...
    
    @ignore_fields.setter
    def ignore_fields(self, value: bool):
        ...
    
    @property
    def ignore_footnotes(self) -> bool:
        """Specifies whether to compare differences in footnotes and endnotes.
        
        By default footnotes are not ignored."""
        ...
    
    @ignore_footnotes.setter
    def ignore_footnotes(self, value: bool):
        ...
    
    @property
    def ignore_comments(self) -> bool:
        """Specifies whether to compare differences in comments.
        
        By default comments are not ignored."""
        ...
    
    @ignore_comments.setter
    def ignore_comments(self, value: bool):
        ...
    
    @property
    def ignore_textboxes(self) -> bool:
        """Specifies whether to compare differences in the data contained within text boxes.
        
        By default textboxes are not ignored."""
        ...
    
    @ignore_textboxes.setter
    def ignore_textboxes(self, value: bool):
        ...
    
    @property
    def ignore_formatting(self) -> bool:
        """True indicates that formatting is ignored.
        
        By default document formatting is not ignored."""
        ...
    
    @ignore_formatting.setter
    def ignore_formatting(self, value: bool):
        ...
    
    @property
    def ignore_headers_and_footers(self) -> bool:
        """True indicates that headers and footers content is ignored.
        
        By default headers and footers are not ignored."""
        ...
    
    @ignore_headers_and_footers.setter
    def ignore_headers_and_footers(self, value: bool):
        ...
    
    @property
    def target(self) -> aspose.words.comparing.ComparisonTargetType:
        """Specifies which document shall be used as a target during comparison."""
        ...
    
    @target.setter
    def target(self, value: aspose.words.comparing.ComparisonTargetType):
        ...
    
    @property
    def granularity(self) -> aspose.words.comparing.Granularity:
        """Specifies whether changes are tracked by character or by word.
        
        Default value is :attr:`Granularity.WORD_LEVEL`."""
        ...
    
    @granularity.setter
    def granularity(self, value: aspose.words.comparing.Granularity):
        ...
    
    @property
    def advanced_options(self) -> aspose.words.comparing.AdvancedCompareOptions:
        """Specifies advanced compare options that might help to produce more precise comparison output."""
        ...
    
    @property
    def ignore_dml_unique_id(self) -> bool:
        """Specifies whether to ignore difference in DrawingML unique Id.
        
        Default value is ``False``."""
        ...
    
    @ignore_dml_unique_id.setter
    def ignore_dml_unique_id(self, value: bool):
        ...
    
    ...

class ComparisonTargetType(Enum):
    """Allows to specify base document which will be used during comparison.  Default value is :attr:`ComparisonTargetType.CURRENT`.
    
    Relates to Microsoft Word "Show changes in" option in "Compare Documents" dialog box."""
    
    """This document is used as a base during comparison."""
    CURRENT: int
    
    """Other document is used as a base during comparison."""
    NEW: int
    

class Granularity(Enum):
    """Specifies the granularity of changes to track when comparing two documents."""
    
    """Specifies changes at the character level."""
    CHAR_LEVEL: int
    
    """Specifies changes at the word level."""
    WORD_LEVEL: int
    

