
from abc import ABC, abstractmethod
from hashlib import sha256


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

    def create_hash(self, hashable_keys: dict, encoding: str = "utf-8") -> str:
        """Create an hash for the package using the 

        Args:
            hashable_keys (dict): _description_
            encoding (str, optional): _description_. Defaults to "utf-8".

        Returns:
            str: _description_
        """
        hash_string = sha256(bytes(hashable_keys.__str__(), encoding))
        return hash_string.hexdigest()
