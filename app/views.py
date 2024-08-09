from flask import request, jsonify, send_file
from flask_restful import Resource
from .services import get_products_cached, process_data
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class FetchDataResource(Resource):
    def get(self):
        products = get_products_cached()
        return products.model_dump(by_alias=True)

class LogResource(Resource):
    def get(self):
        try:
            with open("app.log", "r") as log_file:
                logs = log_file.readlines()
            return jsonify({"logs": logs})
        except Exception as e:
            logger.error(f"Error fetching logs: {e}")
            return jsonify({"error": "Failed to fetch logs"}), 500

class HealthCheckResource(Resource):
    def get(self):
        return jsonify({"status": "healthy", "timestamp": datetime.utcnow().isoformat()})

class HomeResource(Resource):
    def get(self):
        return jsonify({
            "endpoints": [
                {"name": "Fetch Raw Data", "url": request.url_root + "fetch-data"},
                {"name": "Get Processed Data", "url": request.url_root + "get-processed-data"},
                {"name": "Logs", "url": request.url_root + "logs"},
                {"name": "Health Check", "url": request.url_root + "healthcheck"}
            ]
        })

class ProcessedDataResource(Resource):
    def get(self):
        products = get_products_cached()
        processed_data = process_data(products)
        return jsonify(processed_data)
