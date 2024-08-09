import requests
from .models import Products
from .config import Config
import logging
from functools import lru_cache
from datetime import datetime, timedelta

# Set up logging
logger = logging.getLogger(__name__)

@lru_cache(maxsize=1)
def get_products_cached() -> Products:
    """
    Cached wrapper for get_products function.
    
    Returns:
        Products: A Products object containing the fetched product data.
    """
    return get_products()

def get_products() -> Products:
    """
    Fetch products from the external API.
    
    Returns:
        Products: A Products object containing the fetched product data.
    """
    try:
        # Get API key from config
        api_key = Config.API_KEY
        if not api_key:
            raise ValueError("API_KEY environment variable is not set.")
        
        # Make API request
        response = requests.get(f"https://getpantry.cloud/apiv1/pantry/{api_key}/basket/myProducts")
        response.raise_for_status()
        
        logger.info("Successfully fetched products from the external API.")
        data = response.json()
        return Products(**data)
    except requests.RequestException as e:
        logger.error(f"Error fetching products: {e}")
        return Products(products=[])
    except ValueError as e:
        logger.error(f"Value error: {e}")
        return Products(products=[])

def get_products_with_cache(cache_duration=timedelta(minutes=5)) -> Products:
    """
    Get products with caching mechanism.
    
    Args:
        cache_duration (timedelta): Duration for which the cache is considered valid.
    
    Returns:
        Products: A Products object containing the product data.
    """
    cached_products, timestamp = get_products_cached()
    if datetime.now() - timestamp < cache_duration:
        logger.info("Returning cached products.")
        return cached_products
    else:
        logger.info("Cache expired. Fetching new products.")
        get_products_cached.cache_clear()
        return get_products_cached()[0]

def process_data(data: Products) -> dict:
    """
    Process the product data.
    
    Args:
        data (Products): A Products object containing the product data to process.
    
    Returns:
        dict: A dictionary containing the processed product data.
    """
    processed_products = []
    for product in data.products:
        # Generate comment based on stock quantity
        comment = (
            f"Product {product.name} is running low on stock"
            if product.quantity < 20
            else f"Product {product.name} has {product.quantity} in stock"
        )
        
        # Format price
        price = {
            "currency": "USD",
            "value": product.price
        }
        
        # Create processed product dictionary
        processed_product = {
            "id": product.id,
            "name": product.name,
            "price": price,
            "category": product.category,
            "brand": product.brand,
            "comment": comment
        }
        
        processed_products.append(processed_product)
    logger.info("Successfully processed product data.")
    return {"products": processed_products}
