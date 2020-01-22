from marshmallow import fields, Schema


class TypeSchema(Schema):
    """Type"""

    class Meta:
        ordered = True

    typeId = fields.Number(attribute="type_id")
    name = fields.String(attribute="name")
    description = fields.String(attribute="description")
