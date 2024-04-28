from typing import TYPE_CHECKING

import database
import models
import schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def add_tables():
    return database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# async def create_ability(
#     loan_ability: schemas.CreateLoanAbility,
#     db: "Session"
# ) -> schemas.LoanAbility:
#     loan_ability = models.LoanAbility()
#     db.add(loan_ability)
#     db.commit()
#     db.refresh(loan_ability)
#     return schemas.LoanAbility.from_orm(loan_ability)
