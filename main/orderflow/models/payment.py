from dataclasses import dataclass

@dataclass
class Payment:
    id: int = 0
    order_id: int = 0
    amount: float = 0
    status: str = ''
