from vng_api_common.conf.api import *  # noqa - imports white-listed

API_VERSION = "1.0.0-alpha"

REST_FRAMEWORK = BASE_REST_FRAMEWORK.copy()

SECURITY_DEFINITION_NAME = "JWT-Claims"

SWAGGER_SETTINGS = BASE_SWAGGER_SETTINGS.copy()

SWAGGER_SETTINGS.update(
    {
        "DEFAULT_INFO": "klantnotificaties.api.schema.info",
        "SECURITY_DEFINITIONS": {
            SECURITY_DEFINITION_NAME: {
                # OAS 3.0
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
                # not official...
                # 'scopes': {},  # TODO: set up registry that's filled in later...
                # Swagger 2.0
                # 'name': 'Authorization',
                # 'in': 'header'
                # 'type': 'apiKey',
            }
        },
    }
)

GEMMA_URL_INFORMATIEMODEL_VERSIE = "1.0"

# API spec links for resource validation
repo = "vng-Realisatie/klanten-api"
commit = "16458270233b2f3a350b1eeca3331d9acf5d19f8"
KLANTEN_API_SPEC = (
    f"https://raw.githubusercontent.com/{repo}/{commit}/src/openapi.yaml"
)
