from pydantic import BaseModel, Field


class Item(BaseModel):
    id: int = Field(alias="product_id")
    name: str = Field(alias="product_name")
    price: float 
    category: str
    brand: str
    quantity: int = Field(alias="stock")
    

class Products(BaseModel):
    products: list[Item]
    
