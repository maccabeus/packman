
from typing import Any
from library.package.delete_package import DeletePackage
from library.package.install_package import InstallPackage


class PackageFactory:
    """Factory class for the creation of packages instance
    """
    @staticmethod
    def create(package_type: str) -> Any:
        """create a package instance

        Args:
            package_type (str): The type pf package to create. Could be install or delete

        Returns:
            Any: The package instance
        """
        package_type_lower_case = package_type.lower()
        if package_type_lower_case == "install":
            return InstallPackage()
        elif package_type_lower_case == "delete":
            return DeletePackage()
        assert 0, "Invalid package type provided"
