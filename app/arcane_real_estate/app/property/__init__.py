from .model import Property  # noqa
from .schema import PropertySchema  # noqa


def register_routes(root_api, root="/api"):
    from .controller import api as property_api

    root_api.add_namespace(property_api, path=f"{root}/property")
    return root_api