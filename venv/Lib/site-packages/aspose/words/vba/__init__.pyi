import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List
from enum import Enum

class VbaExecutableAttribute:
    
    def __init__(self):
        ...
    
    ...

class VbaModule:
    """Provides access to VBA project module.
    To learn more, visit the `Working with VBA Macros <https://docs.aspose.com/words/python-net/working-with-vba-macros/>` documentation article."""
    
    def __init__(self):
        """Creates an empty module."""
        ...
    
    def clone(self) -> aspose.words.vba.VbaModule:
        """Performs a copy of the :class:`VbaModule`.
        
        :returns: The cloned :class:`VbaModule`."""
        ...
    
    @property
    def name(self) -> str:
        """Gets or sets VBA project module name."""
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def source_code(self) -> str:
        """Gets or sets VBA project module source code."""
        ...
    
    @source_code.setter
    def source_code(self, value: str):
        ...
    
    @property
    def type(self) -> aspose.words.vba.VbaModuleType:
        """Specifies whether the module is a procedural module, document module, class module, or designer module."""
        ...
    
    @type.setter
    def type(self, value: aspose.words.vba.VbaModuleType):
        ...
    
    ...

class VbaModuleCollection:
    """Represents a collection of :class:`VbaModule` objects.
    To learn more, visit the `Working with VBA Macros <https://docs.aspose.com/words/python-net/working-with-vba-macros/>` documentation article."""
    
    def __getitem__(self, index: int) -> aspose.words.vba.VbaModule:
        """Retrieves a :class:`VbaModule` object by index.
        
        :param index: Zero-based index of the module to retrieve."""
        ...
    
    def add(self, vba_module: aspose.words.vba.VbaModule) -> None:
        """Adds a module to the collection."""
        ...
    
    def get_by_name(self, name: str) -> aspose.words.vba.VbaModule:
        """Retrieves a :class:`VbaModule` object by name, or Null if not found."""
        ...
    
    def remove(self, module: aspose.words.vba.VbaModule) -> None:
        """Removes the specified module from the collection.
        
        :param module: The module to remove."""
        ...
    
    @property
    def count(self) -> int:
        """Returns the number of VBA modules in the collection."""
        ...
    
    ...

class VbaProject:
    """Provides access to VBA project information.
    A VBA project inside the document is defined as a collection of VBA modules.
    To learn more, visit the `Working with VBA Macros <https://docs.aspose.com/words/python-net/working-with-vba-macros/>` documentation article."""
    
    def __init__(self):
        """Creates a blank :class:`VbaProject`."""
        ...
    
    def clone(self) -> aspose.words.vba.VbaProject:
        """Performs a copy of the :class:`VbaProject`.
        
        :returns: The cloned :class:`VbaProject`."""
        ...
    
    @property
    def name(self) -> str:
        """Gets or sets VBA project name."""
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def modules(self) -> aspose.words.vba.VbaModuleCollection:
        """Returns collection of VBA project modules."""
        ...
    
    @property
    def code_page(self) -> int:
        """Gets or sets the VBA project’s code page.
        
        Please note that VBA is pre-Unicode feature and you have to explicitly set appropriate code page
        to preserve regional character sets."""
        ...
    
    @code_page.setter
    def code_page(self, value: int):
        ...
    
    @property
    def is_signed(self) -> bool:
        """Shows whether the :class:`VbaProject` is signed or not."""
        ...
    
    @property
    def is_protected(self) -> bool:
        """Shows whether the :class:`VbaProject` is password protected."""
        ...
    
    @property
    def references(self) -> aspose.words.vba.VbaReferenceCollection:
        """Gets a collection of VBA project references."""
        ...
    
    ...

class VbaReference:
    """Implements a reference to an Automation type library or VBA project.
    To learn more, visit the `Working with VBA Macros <https://docs.aspose.com/words/python-net/working-with-vba-macros/>` documentation article."""
    
    @property
    def type(self) -> aspose.words.vba.VbaReferenceType:
        """Gets :class:`VbaReferenceType` object that indicates the type of reference that a :class:`VbaReference` object represents."""
        ...
    
    @property
    def lib_id(self) -> str:
        """Gets a string value containing the identifier of an Automation type library.
        
        Depending on reference type, the value of this property can be:
        
        * a LibidReference specified at 2.1.1.8 LibidReference of [MS-OVBA]:
          https://docs.microsoft.com/en-us/openspecs/office_file_formats/ms-ovba/3737ef6e-d819-4186-a5f2-6e258ddf66a5
        
        * a ProjectReference specified at 2.1.1.12 ProjectReference of [MS-OVBA]:
          https://docs.microsoft.com/en-us/openspecs/office_file_formats/ms-ovba/9a45ac1a-f1ff-4ebd-958e-537701aa8131"""
        ...
    
    ...

class VbaReferenceCollection:
    """Represents a collection of :class:`VbaReference` objects.
    To learn more, visit the `Working with VBA Macros <https://docs.aspose.com/words/python-net/working-with-vba-macros/>` documentation article."""
    
    def __getitem__(self, index: int) -> aspose.words.vba.VbaReference:
        """Gets :class:`VbaReference` object at the specified index.
        
        :param index: The zero-based index of the reference to get."""
        ...
    
    def remove(self, item: aspose.words.vba.VbaReference) -> None:
        """Removes the first occurrence of a specified :class:`VbaReference` item from the collection."""
        ...
    
    def remove_at(self, index: int) -> None:
        """Removes the :class:`VbaReference` element at the specified index of the collection."""
        ...
    
    @property
    def count(self) -> int:
        """Returns the number of VBA references in the collection."""
        ...
    
    ...

class VbaModuleType(Enum):
    """Specifies the type of a model in a VBA project."""
    
    """A type of VBA project item that specifies a module for embedded macros and programmatic access operations
    that are associated with a document."""
    DOCUMENT_MODULE: int
    
    """A collection of subroutines and functions."""
    PROCEDURAL_MODULE: int
    
    """A module that contains the definition for a new object. Each instance of a class creates a new object,
    and procedures that are defined in the module become properties and methods of the object."""
    CLASS_MODULE: int
    
    """A VBA module that extends the methods and properties of an ActiveX control that has been registered with the project."""
    DESIGNER_MODULE: int
    

class VbaReferenceType(Enum):
    """Allows to specify the type of a :class:`VbaReference` object."""
    
    """Specifies an Automation type library reference type.
    
    This type corresponds to 2.3.4.2.2.5 REFERENCEREGISTERED Record of [MS-OVBA]:
    https://docs.microsoft.com/en-us/openspecs/office_file_formats/ms-ovba/6c39388e-96f5-4b93-b90a-ae625a063fcf"""
    REGISTERED: int
    
    """Specified an external VBA project reference type.
    
    This type corresponds to 2.3.4.2.2.6 REFERENCEPROJECT Record of [MS-OVBA]:
    https://docs.microsoft.com/en-us/openspecs/office_file_formats/ms-ovba/08280eb0-d628-495c-867f-5985ed020142"""
    PROJECT: int
    
    """Specifies an original Automation type library reference type.
    
    This type corresponds to 2.3.4.2.2.4 REFERENCEORIGINAL Record of [MS-OVBA]:
    https://docs.microsoft.com/en-us/openspecs/office_file_formats/ms-ovba/3ba66994-8c7a-4634-b2da-f9331ace6686"""
    ORIGINAL: int
    
    """Specifies a twiddled type library reference type.
    
    This type corresponds to 2.3.4.2.2.3 REFERENCECONTROL Record of [MS-OVBA]:
    https://docs.microsoft.com/en-us/openspecs/office_file_formats/ms-ovba/d64485fa-8562-4726-9c5e-11e8f01a81c0"""
    CONTROL: int
    

