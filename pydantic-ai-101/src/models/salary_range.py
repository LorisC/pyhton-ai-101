from typing import Optional
from pydantic import BaseModel, Field


class SalaryRange(BaseModel):
    min_salary: Optional[int] = Field(None, description="Salaire minimum annuel en USD")
    max_salary: Optional[int] = Field(None, description="Salaire maximum annuel en USD")
    currency: str = Field("USD", description="Devise, ex: USD, EUR")
