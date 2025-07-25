"""
Base class for payload builders.
"""
from abc import ABC, abstractmethod


class PayloadBuilder(ABC):
    """
    Abstract base class for building payloads.
    """

    @abstractmethod
    def build_main_payload(self, **extra) -> dict:
        """
        Build and return the payload as a dict.
        This method should be implemented by subclasses
        to define the specific main payload structure.
        """

