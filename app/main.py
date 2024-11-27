from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/advertisement", response_model=schemas.AdvertisementInDB)
def create_advertisement(advertisement: schemas.AdvertisementCreate, db: Session = Depends(get_db)):
    return crud.create_advertisement(db=db, advertisement=advertisement)

@app.get("/advertisement/{advertisement_id}", response_model=schemas.AdvertisementInDB)
def get_advertisement(advertisement_id: int, db: Session = Depends(get_db)):
    db_advertisement = crud.get_advertisement(db=db, advertisement_id=advertisement_id)
    if db_advertisement is None:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return db_advertisement

@app.patch("/advertisement/{advertisement_id}", response_model=schemas.AdvertisementInDB)
def update_advertisement(advertisement_id: int, advertisement: schemas.AdvertisementUpdate, db: Session = Depends(get_db)):
    db_advertisement = crud.update_advertisement(db=db, advertisement_id=advertisement_id, advertisement=advertisement)
    if db_advertisement is None:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return db_advertisement

@app.delete("/advertisement/{advertisement_id}", response_model=schemas.AdvertisementInDB)
def delete_advertisement(advertisement_id: int, db: Session = Depends(get_db)):
    db_advertisement = crud.delete_advertisement(db=db, advertisement_id=advertisement_id)
    if db_advertisement is None:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return db_advertisement

@app.get("/advertisement", response_model=list[schemas.AdvertisementInDB])
def search_advertisements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    advertisements = crud.get_advertisements(db=db, skip=skip, limit=limit)
    return advertisements
