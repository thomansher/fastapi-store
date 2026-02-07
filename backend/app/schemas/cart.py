from pydantic import BaseModel, Field
from typing import Optional


class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Cart product id")
    quantity: int = Field(..., qt=0, description="Cart quantity")


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product id")
    quantity: int = Field(..., qt=0, description="New Cart quantity")


class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., qt=0, description="Product price")
    quantity: int = Field(..., qt=0, description="Quantity in cart")
    subtotal: float = Field(
        ..., description="Total price for this item (price*quantity)"
    )
    image_url: Optional[str] = Field(None, description="Product url")


class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in cart")
    total: float = Field(..., description="Total cart price")
    items_count: int = Field(..., description="Total number of items in cart")
