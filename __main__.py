from calendar import TUESDAY
from library.command import Command
from library.command_runner import CommandRunner
from library.package.package_factory import PackageFactory
import os
import sys
from cli import parse_args


def main():
    """The main entry point to our CLI application
    """

    cli_args=parse_args()

    package_action=  cli_args.action
    package_name= cli_args.package

    package = PackageFactory.create(package_action)
    package.set_name(package_name)
    command = Command(package)
    runner = CommandRunner(command)
    run_result=runner.execute()

    # if run_result is False or run_result is None: 
    #     raise Exception(f" Could not {package_action} {package_name}")

if __name__ == "__main__":
    main()
