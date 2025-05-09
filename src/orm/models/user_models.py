from typing import Optional
from dataclasses import dataclass

@dataclass
class UserModel:
    id: Optional[int] = None  # Auto-increment primary key
    name: Optional[str] = None  # VARCHAR(45)
    email: Optional[str] = None  # VARCHAR(45)
    age: Optional[int] = None  # Integer
