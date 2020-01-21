from pytest import fixture

from .model import Property
from .interface import PropertyInterface


@fixture
def interface() -> PropertyInterface:

    params: PropertyInterface = {
        "name": "Test name",
        "description": "Test description",
        "city": "san francisco"
    }
    return params


def test_PropertyInterface_create(interface: PropertyInterface):
    assert interface


def test_PropertyInterface_works(interface: PropertyInterface):
    assert Property(**interface)