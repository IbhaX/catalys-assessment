from flask import Flask
from flask_restful import Api
from .logging_setup import setup_logging

def create_app():
    app = Flask(__name__)
    setup_logging(app)
    api = Api(app)
    
    from .views import HomeResource, FetchDataResource, ProcessedDataResource, LogResource, HealthCheckResource
    api.add_resource(HomeResource, '/')
    api.add_resource(LogResource, '/logs')
    api.add_resource(HealthCheckResource, '/health')
    api.add_resource(FetchDataResource, '/fetch-data')
    api.add_resource(ProcessedDataResource, '/get-processed-data')
    
    return app
