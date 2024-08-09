from flask import Flask
from flask_restful import Api
from .logging_setup import setup_logging

def create_app():
    """
    Create and configure an instance of the Flask application.

    This function initializes the Flask app, sets up logging, creates an API
    instance, and registers all the resource endpoints.

    Returns:
        Flask: A configured Flask application instance.
    """
    # Initialize the Flask application
    app = Flask(__name__)

    # Set up logging for the application
    setup_logging(app)

    # Create an API instance
    api = Api(app)
    
    # Import resources
    from .views import HomeResource, FetchDataResource, ProcessedDataResource, LogResource, HealthCheckResource

    # Register resources with their respective endpoints
    api.add_resource(HomeResource, '/')
    api.add_resource(LogResource, '/logs')
    api.add_resource(HealthCheckResource, '/health')
    api.add_resource(FetchDataResource, '/fetch-data')
    api.add_resource(ProcessedDataResource, '/get-processed-data')
    
    return app
