from pytest import fixture

from .model import Property
from .interface import PropertyInterface


@fixture
def interface() -> PropertyInterface:

    params: PropertyInterface = {
        "property_id": 1,
        "name": "Test name",
        "description": "Test description",
    }
    return params


def test_PropertyInterface_create(interface: PropertyInterface):
    assert interface


def test_PropertyInterface_works(interface: PropertyInterface):
    assert Property(**interface)