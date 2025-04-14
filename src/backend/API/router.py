from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database_conf import Config
from data_contract.schemas import EstoqueUpdate,EstoqueDelete,EstoqueCreate,EstoqueResponse
from typing import List
from API.crud import (delete_item,get_item,get_items,create_item,update_item)

router = APIRouter()
config = Config()

@router.get("/Estoque/", response_model=List[EstoqueResponse])
def get_all_items(db: Session = Depends(config.get_db)):
    '''Endpoint que exibe todos os items do banco'''
    return get_items(db)

@router.get("/Estoque/{item_id}", response_model=EstoqueResponse)
def get_a_single_item(item_id: int, db: Session = Depends(config.get_db)):
    '''Endpoint que exibe apenas o dado solicitado pelo usuario baseando-se no item_id'''
    item = get_item(db, item_id=item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Product not found")

@router.post("/Estoque/", response_model=EstoqueCreate)
def create_one_item(item: EstoqueCreate, db: Session = Depends(config.get_db)):
    '''Endpoint que permite criar novas inserções no banco'''
    return create_item(item=item, db=db)

@router.delete("/Estoque/{item_id}", response_model=EstoqueDelete)
def delete_one_item(item_id: int, db: Session = Depends(config.get_db)):
    '''Endpoint que permite deletar um item com item_id especifico'''
    item = delete_item(item_id=item_id, db=db)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Product not found")

@router.put("/Estoque/{item_id}", response_model=EstoqueUpdate)
def update_one_item(item_id: int, item: EstoqueUpdate, db: Session = Depends(config.get_db)):
    '''Endpoint para atualização de um item_id'''
    item = update_item(db=db, item_id=item_id, item=item)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Product not found")
