def register_routes(api, app, root="/api"):
    from app.property import register_routes as attach_property
    from app.type import register_routes as attach_type

    # Add routes
    attach_property(api, root)
    attach_type(api, root)
