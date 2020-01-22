from .model import Type  # noqa
from .schema import TypeSchema  # noqa


def register_routes(root_api, root="/api"):
    from .controller import api as type_api

    root_api.add_namespace(type_api, path=f"{root}/type")
    return root_api