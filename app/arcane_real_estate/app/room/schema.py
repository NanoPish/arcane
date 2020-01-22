from marshmallow import fields, Schema


class RoomSchema(Schema):
    """Room"""

    class Meta:
        ordered = True

    roomId = fields.Number(attribute="room_id")
    name = fields.String(attribute="name")
    description = fields.String(attribute="description")
