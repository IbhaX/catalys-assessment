from pydantic import BaseModel, Field


class Item(BaseModel):
    """
    Represents an individual product item.
    """
    id: int = Field(alias="product_id")  # Unique identifier for the product
    name: str = Field(alias="product_name")  # Name of the product
    price: float  # Price of the product
    category: str  # Category the product belongs to
    brand: str  # Brand of the product
    quantity: int = Field(alias="stock")  # Available quantity in stock
    

class Products(BaseModel):
    """
    Represents a collection of product items.
    """
    products: list[Item]  # List of Item objects representing multiple products
