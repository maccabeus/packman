from library.package.package_interface import PackageInterface
from library.package.package_config_loader import PackageConfigLoader


class InstallPackage(PackageInterface):
    """The package Instance
    """

    def set_name(self, package_name: str) -> None:
        """Set the name of the package to work on
        """
        self.__package_name = package_name

    def run_action(self) -> None:
        """The action runnable on a package instance. 
        """
        package_locked_info = PackageConfigLoader.load_package_dot_lock(self.__package_name)
        package_info=PackageConfigLoader.load_package_info(self.__package_name)
        if(package_locked_info is None and package_info is None):
            raise Exception("You must add package to install in package.json file ")

        print("locked info:", package_locked_info)
        self.create_hash()

        # if not installed_package or installed_package == None:
        #     # Install package  as new
        #     # install all dependencies first
        #     dependencies= installed_package.get("deps")
        #     for dependency in  enumerate(dependencies or []):
        #         print(dependency)
        # else:
        #     print("package already installed")

        return True