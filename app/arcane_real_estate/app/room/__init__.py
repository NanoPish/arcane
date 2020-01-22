from .model import Room  # noqa
from .schema import RoomSchema  # noqa


def register_routes(root_api, root="/api"):
    from .controller import api as room_api

    root_api.add_namespace(room_api, path=f"{root}/room")
    return root_api