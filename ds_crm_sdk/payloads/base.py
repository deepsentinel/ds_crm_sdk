from abc import ABC, abstractmethod
from pydantic import BaseModel


class PayloadBuilder(ABC):

    @abstractmethod
    def build_main_payload(self, client_type: str) -> BaseModel:
        """
        Build and return the payload as a Pydantic model.
        This method should be implemented by subclasses to define the specific main payload structure.
        """
        pass
