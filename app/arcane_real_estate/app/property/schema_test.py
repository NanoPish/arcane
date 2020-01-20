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
        {"propertyId": 1, "name": "Test name", "description": "Test description"}
    ).data
    property = Property(**params)

    assert property.property_id == 1
    assert property.name == "Test description"
    assert property.description == "Test description"
