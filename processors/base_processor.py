""" This module provides a base class for processing cryptocurrency data. """

from abc import ABC, abstractmethod
from typing import List
from models import Transaction

class BaseProcessor(ABC):
    @abstractmethod
    def process(self, raw: List[dict]) -> List[Transaction]:
        """Map raw data to list of Transaction objects."""
        pass