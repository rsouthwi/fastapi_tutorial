from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
