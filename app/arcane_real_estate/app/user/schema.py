from marshmallow import fields, Schema


class UserSchema(Schema):
    """User"""

    class Meta:
        ordered = True
        dateformat = '%Y-%m-%d'

    userId = fields.Number(attribute="user_id")
    firstName = fields.String(attribute="first_name")
    lastName = fields.String(attribute="last_name")
    birthDate = fields.Date(attribute="birth_date")
    mail = fields.String(attribute="mail")
    password = fields.String(attribute="password")