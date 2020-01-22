from pytest import fixture

from .model import Type
from .interface import TypeInterface


@fixture
def interface() -> TypeInterface:

    params: TypeInterface = {
        "type_id": 1,
        "name": "Test name",
        "description": "Test description",
    }
    return params


def test_TypeInterface_create(interface: TypeInterface):
    assert interface


def test_TypeInterface_works(interface: TypeInterface):
    assert Type(**interface)