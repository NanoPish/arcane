from marshmallow import fields, Schema


class UserSchema(Schema):
    """User"""

    class Meta:
        ordered = True

    userId = fields.Number(attribute="user_id")
    name = fields.String(attribute="name")
    description = fields.String(attribute="description")
