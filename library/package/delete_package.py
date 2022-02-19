from library.package.package_interface import PackageInterface


class DeletePackage(PackageInterface):
    """The package Instance
    """

    def run_action(self) -> None:
        """The action runnable on a package instance. 
        """
        print("delete package")

    def set_set_name(self, package_name: str) -> None:
        """Set the name of the package to work on
        """
        self.__package_name = package_name