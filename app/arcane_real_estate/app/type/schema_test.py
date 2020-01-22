from pytest import fixture

from .model import Type
from .schema import TypeSchema
from .interface import TypeInterface


@fixture
def schema() -> TypeSchema:
    return TypeSchema()


def test_TypeSchema_create(schema: TypeSchema):
    assert schema


def test_TypeSchema_works(schema: TypeSchema):
    params: TypeInterface = schema.load(
        {"typeId": 1, "name": "Test name", "description": "Test description"}
    )
    type = Type(**params)

    assert type.type_id == 1
    assert type.name == "Test name"
    assert type.description == "Test description"
