from pytest import fixture

from .model import Property
from .schema import PropertySchema
from .interface import PropertyInterface


@fixture
def schema() -> PropertySchema:
    return PropertySchema()


def test_PropertySchema_create(schema: PropertySchema):
    assert schema


def test_PropertySchema_works(schema: PropertySchema):
    params: PropertyInterface = schema.load(
        {
            "name": "Test name",
            "description": "Test description",
            "city": "tokyo",
        }
    )
    property = Property(**params)

    assert property.name == "Test name"
    assert property.description == "Test description"
    assert property.city == "tokyo"
