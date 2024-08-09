from flask import request, jsonify, send_file
from flask_restful import Resource
from .services import get_products_cached, process_data
import logging
from datetime import datetime

# Set up logging
logger = logging.getLogger(__name__)

class FetchDataResource(Resource):
    """Resource for fetching raw product data."""

    def get(self):
        """
        GET method to retrieve cached product data.
        
        Returns:
            dict: Serialized product data
        """
        products = get_products_cached()
        return products.model_dump(by_alias=True)

class LogResource(Resource):
    """Resource for retrieving application logs."""

    def get(self):
        """
        GET method to fetch application logs.
        
        Returns:
            dict: JSON response containing logs or error message
        """
        try:
            with open("app.log", "r") as log_file:
                logs = log_file.readlines()
            return jsonify({"logs": logs})
        except Exception as e:
            logger.error(f"Error fetching logs: {e}")
            return jsonify({"error": "Failed to fetch logs"}), 500

class HealthCheckResource(Resource):
    """Resource for performing health checks."""

    def get(self):
        """
        GET method to check the health status of the application.
        
        Returns:
            dict: JSON response with health status and timestamp
        """
        return jsonify({"status": "healthy", "timestamp": datetime.utcnow().isoformat()})

class HomeResource(Resource):
    """Resource for the home page, listing available endpoints."""

    def get(self):
        """
        GET method to retrieve a list of available endpoints.
        
        Returns:
            dict: JSON response containing endpoint information
        """
        return jsonify({
            "endpoints": [
                {"name": "Fetch Raw Data", "url": request.url_root + "fetch-data"},
                {"name": "Get Processed Data", "url": request.url_root + "get-processed-data"},
                {"name": "Logs", "url": request.url_root + "logs"},
                {"name": "Health Check", "url": request.url_root + "healthcheck"}
            ]
        })

class ProcessedDataResource(Resource):
    """Resource for retrieving processed product data."""

    def get(self):
        """
        GET method to fetch and process product data.
        
        Returns:
            dict: JSON response containing processed product data
        """
        products = get_products_cached()
        processed_data = process_data(products)
        return jsonify(processed_data)
