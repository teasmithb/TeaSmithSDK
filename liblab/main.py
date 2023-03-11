from flask import Flask


from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


SWAGGER_URL = '/the-one-api.dev/v2'
# API URL
API_URL = '/static/openapi.json'

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Lord Of the Rings API"
    }
)

app.register_blueprint(swaggerui_blueprint)


app.run()

# Now point your browser to localhost:5000/the-one-api.dev/v2
