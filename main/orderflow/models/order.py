from dataclasses import dataclass

@dataclass
class Order:
    id: int = 0
    customer_id: int = 0
    total: float = 0
    status: str = ''
