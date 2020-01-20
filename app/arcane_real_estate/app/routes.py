def register_routes(api, app, root="/api"):
    from app.property import register_routes as attach_property

    # Add routes
    attach_property(api, root)
