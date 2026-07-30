from cars.domain.entities import Car
from fastapi import APIRouter, Depends, HTTPException, status
from presentation.schemas import (
    CarList,
    CarPartialUpdate,
    CarPublic,
    CarSchema,
)
from shared.database.base import get_session
from sqlalchemy import select
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)


@router.post(
    '/', response_model=CarPublic, status_code=status.HTTP_201_CREATED
)
def create_car(
    car: CarSchema,
    session: Session = Depends(get_session),
):
    car = Car(**car.model_dump())
    session.add(car)
    session.commit()
    session.refresh(car)
    return car


@router.get('/', response_model=CarList)
def list_cars(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    query = session.scalars(select(Car).offset(offset).limit(limit))
    cars = query.all()
    return {'cars': cars}


@router.get('/{car_id}', response_model=CarPublic)
def get_car(
    car_id: int,
    session: Session = Depends(get_session),
):
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Car not found'
        )
    return car


@router.put('/{car_id}', response_model=CarPublic)
def update_car(
    car_id: int,
    car: CarSchema,
    session: Session = Depends(get_session),
):
    db_car = session.get(Car, car_id)
    if not db_car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Car not found'
        )
    for field, value in car.model_dump().items():
        setattr(db_car, field, value)
    session.commit()
    session.refresh(db_car)
    return db_car


@router.patch('/{car_id}', response_model=CarPublic)
def patch_car(
    car_id: int,
    car: CarPartialUpdate,
    session: Session = Depends(get_session),
):
    db_car = session.get(Car, car_id)
    if not db_car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Car not found'
        )
    update_data = {k: v for k, v in car.model_dump(exclude_unset=True).items()}
    for field, value in update_data.items():
        setattr(db_car, field, value)
    session.commit()
    session.refresh(db_car)
    return db_car


@router.delete('/{car_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_car(
    car_id: int,
    session: Session = Depends(get_session),
):
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Car not found'
        )
    session.delete(car)
    session.commit()
