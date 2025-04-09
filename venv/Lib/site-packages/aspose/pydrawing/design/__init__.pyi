import aspose.pydrawing
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class CategoryNameCollection:
    
    @overload
    def __init__(self, value: aspose.pydrawing.design.CategoryNameCollection):
        ...
    
    @overload
    def __init__(self, value: list[str]):
        ...
    
    def __getitem__(self, index: int) -> str:
        ...
    
    def copy_to(self, array: list[str], index: int) -> None:
        ...
    
    def index_of(self, value: str) -> int:
        ...
    
    ...

