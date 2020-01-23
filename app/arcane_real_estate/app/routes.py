def register_routes(api, app, root="/api"):
    from app.property import register_routes as attach_property
    from app.type import register_routes as attach_type
    from app.room import register_routes as attach_room
    from app.user import register_routes as attach_user

    # Add routes
    attach_property(api, root)
    attach_type(api, root)
    attach_room(api, root)
    attach_user(api, root)
