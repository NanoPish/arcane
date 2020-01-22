from marshmallow import fields, Schema

class PropertySchema(Schema):
    """Property"""

    class Meta:
        ordered = True

    propertyId = fields.Number(attribute="property_id")
    name = fields.String(attribute="name")
    description = fields.String(attribute="description")
    city = fields.String(attribute="city")
    typeId = fields.Number(attribute="type_id")

