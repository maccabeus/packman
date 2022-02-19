
import json
from pathlib import Path


class PackageConfigLoader():
    """Package configurations loader
    """
    @staticmethod
    def load_package_info(package_name: str, package_version: str = None, package_file_name: str = "packman.json") -> dict:
        """load package list

        Args:
            package_name (str): The name of the package to install
            package_version (str, optional): _description_. Defaults to None.
            package_file_name (str, optional): _description_. Defaults to "packman.json".
        """
        PackageConfigLoader.__package_name = package_name
        PackageConfigLoader.__version = package_version
        PackageConfigLoader.__package_path = "./"+package_file_name

        with open(PackageConfigLoader.__package_path) as installed_packages:
            package_list = PackageConfigLoader.__read_and_parse_file(
                PackageConfigLoader.__package_path,
                PackageConfigLoader.__package_name
            )
            print(package_list)
            return package_list if package_list else dict()

    @staticmethod
    def load_package_dot_lock(lock_file_name: str = "packman.lock.json") -> dict:
        with open(PackageConfigLoader.__package_path) as installed_packages:
            package_list = PackageConfigLoader.__read_and_parse_file(
                PackageConfigLoader.__package_path,
                PackageConfigLoader.__package_name
            )
            print(package_list)
            return package_list if package_list else dict()

    def __read_and_parse_file(file_path: str, load_index: str = None) -> dict:
        """Load a file and parse  keys as dictionary object

        Args:
            file_path (str): path to file to load
            load_index (str, optional): object key index to load. Defaults to None.

        Returns:
            dict: _description_
        """
        with open(file_path) as loaded_file:
            loaded_file_object = json.loads(loaded_file.read())
            return loaded_file_object.get(load_index) if load_index else loaded_file_object
