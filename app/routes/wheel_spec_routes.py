from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import SessionLocal
from .. import models, schemas

router = APIRouter()

# Get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/forms/wheel-specifications", response_model=schemas.WheelSpecificationResponse)
def create_wheel_spec(spec: schemas.WheelSpecificationCreate, db: Session = Depends(get_db)):
    db_spec = models.WheelSpecification(
        form_number=spec.formNumber,
        submitted_by=spec.submittedBy,
        submitted_date=spec.submittedDate,
        fields=spec.fields
    )
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)
    return db_spec

@router.get("/api/forms/wheel-specifications", response_model=List[schemas.WheelSpecificationResponse])
def get_wheel_specs(
    formNumber: Optional[str] = Query(None),
    submittedBy: Optional[str] = Query(None),
    submittedDate: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.WheelSpecification)

    if formNumber:
        query = query.filter(models.WheelSpecification.form_number == formNumber)
    if submittedBy:
        query = query.filter(models.WheelSpecification.submitted_by == submittedBy)
    if submittedDate:
        query = query.filter(models.WheelSpecification.submitted_date == submittedDate)

    return query.all()
