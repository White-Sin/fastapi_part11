from sqlalchemy.orm import Session
from . import models, schemas

def create_advertisement(db: Session, advertisement: schemas.AdvertisementCreate):
    db_advertisement = models.Advertisement(**advertisement.dict())
    db.add(db_advertisement)
    db.commit()
    db.refresh(db_advertisement)
    return db_advertisement

def get_advertisement(db: Session, advertisement_id: int):
    return db.query(models.Advertisement).filter(models.Advertisement.id == advertisement_id).first()

def get_advertisements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Advertisement).offset(skip).limit(limit).all()

def update_advertisement(db: Session, advertisement_id: int, advertisement: schemas.AdvertisementUpdate):
    db_advertisement = db.query(models.Advertisement).filter(models.Advertisement.id == advertisement_id).first()
    if db_advertisement:
        for key, value in advertisement.dict(exclude_unset=True).items():
            setattr(db_advertisement, key, value)
        db.commit()
        db.refresh(db_advertisement)
    return db_advertisement

def delete_advertisement(db: Session, advertisement_id: int):
    db_advertisement = db.query(models.Advertisement).filter(models.Advertisement.id == advertisement_id).first()
    if db_advertisement:
        db.delete(db_advertisement)
        db.commit()
    return db_advertisement
