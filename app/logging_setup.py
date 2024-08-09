import logging

def setup_logging(app):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='app.log',
        filemode='a'
    )
    logger = logging.getLogger(__name__)
    logger.info("Logging setup completed.")
