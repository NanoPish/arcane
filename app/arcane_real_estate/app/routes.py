def register_routes(api, app, root="/api"):
    from .property import register_routes as attach_property
    from .type import register_routes as attach_type
    from .room import register_routes as attach_room
    from .user import register_routes as attach_user

    # Add routes
    attach_property(api, root)
    attach_type(api, root)
    attach_room(api, root)
    attach_user(api, root)
