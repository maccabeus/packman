
from typing import Any
from library.command_interface import CommandInterface

class Command (CommandInterface):
    """Process

    Args:
        CommandInterface (class): The bse comand class to inherit from
    """
    def __init__(self, package: Any) -> None:
      self.__package= package

    def process(self)-> bool:
        """Process the command
        Returns:
            bool: return true or false based on the process status
        """
        self.__package.run_action()
