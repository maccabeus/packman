
from abc import ABC, abstractmethod


class PackageInterface(ABC):
    """ The package Interface. All our packages must implements
    """
    @abstractmethod
    def run_action(self) -> None:
        """The action runnable on a package instance.

      """
    @abstractmethod
    def set_name(self, package_name: str) -> None:
        """Set the name of the package to work on
        """
