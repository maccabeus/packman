
from typing import Any
class CommandRunner:
    """Run package managements commands
    """
    def __init__(self, command: Any) -> None:
      self.__command= command

    def execute(self)-> bool:
        """Execute the required command on the command object instance

        Returns:
            bool: true of false
        """
        self.__command.process()