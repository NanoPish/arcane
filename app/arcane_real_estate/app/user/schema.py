from marshmallow import fields, Schema

class ExistingUserSchema(Schema):
    """ExistingUser"""

    class Meta:
        ordered = True
        dateformat = '%Y-%m-%d'

    userId = fields.Number(attribute="user_id")
    firstName = fields.String(attribute="first_name")
    lastName = fields.String(attribute="last_name")
    birthDate = fields.Date(attribute="birth_date")
    mail = fields.String(attribute="mail")

class NewUserSchema(ExistingUserSchema):
    """NewUser"""

    password = fields.String(attribute="password")