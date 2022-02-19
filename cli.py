import sys
from typing import List
import argparse


def parse_args() -> List:
    """Parse arguments from the CLI and return

    Returns:
        List: _description_
    """
    parser = argparse.ArgumentParser("packman package manager")
    parser.add_argument(
        "action",
        help="Provide action toperform. Can either be INSTALL or DELETE",
        type=str)
    parser.add_argument(
        "package", help="Provide the package name", type=str)
    args = parser.parse_args()
    return args
