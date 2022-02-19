
from abc import ABC, abstractmethod

class CommandInterface (ABC):
    """All command object will implements this interface 

    Args:
        ABC (class): The base class for interfacing
    """

    @abstractmethod
    def process(self) -> bool:
        """an interface for the process action

        Returns:
            bool: return true of false depending on process status
        """