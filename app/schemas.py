from pydantic import BaseModel, Field
from typing import Optional, Dict

class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: Optional[Dict] = {}

class WheelSpecificationResponse(BaseModel):
    formNumber: str = Field(..., alias="form_number")
    submittedBy: str = Field(..., alias="submitted_by")
    submittedDate: str = Field(..., alias="submitted_date")
    fields: Optional[Dict]

    class Config:
        from_attributes = True
        populate_by_name = True  # 🔑 This allows FastAPI to use aliases
