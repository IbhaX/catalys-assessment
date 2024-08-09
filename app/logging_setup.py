import logging

def setup_logging(app):
    """
    Set up logging configuration for the application.

    Args:
        app: The Flask application instance.

    This function configures the logging system with the following settings:
    - Log level: INFO
    - Log format: timestamp - log level - message
    - Log file: app.log
    - File mode: Append
    """
    # Configure the basic logging settings
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='app.log',
        filemode='a'
    )

    # Create a logger instance for this module
    logger = logging.getLogger(__name__)

    # Log a message indicating that the logging setup is complete
    logger.info("Logging setup completed.")
