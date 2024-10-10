from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date

class User(BaseModel):
    id: int
    name: Optional[str] = Field(None, max_length=10)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=1, le=100)
    birthdate: Optional[date] = None