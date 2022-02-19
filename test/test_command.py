"""test user classes
"""
import pytest

@pytest.fixture()
def user_default_details():
    """_summary_

    Returns:
        _type_: _description_
    """
    yield {"user": "Anthony", "password": "123456789"}


@pytest.fixture(name="user_with_details")
def new_user_with_details():
    """_summary_

    Returns:
        _type_: _description_
    """


@pytest.fixture(name="user_without_details")
def new_user_without_details():
    """_summary_

    Returns:
        _type_: _description_
    """


def test_user_added(user_with_details) -> bool:
    """_summary_

    Returns:
        bool: _description_
    """
    print(user_with_details.username)
