from .model import User  # noqa
from .schema import UserSchema  # noqa


def register_routes(root_api, root="/api"):
    from .controller import api as user_api

    root_api.add_namespace(user_api, path=f"{root}/user")
    return root_api