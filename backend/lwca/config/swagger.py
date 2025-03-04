def get_swagger_config():
    """
        Get the configuration for the Swagger UI
    """
    return {
        "headers": [
        ],
        "securityDefinitions": {
            'bearerAuth': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header',
                'description': 'JWT Authorization header using the Bearer scheme. Example: "Authorization: Bearer {token}"'
            },
        },
        "specs": [
            {
                "endpoint": 'lwca',
                "route": '/lwca.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger/"
    }