from sqlalchemy.orm import Session
from data_contract.schemas import EstoqueUpdate,EstoqueCreate
from database.models import Estoque

def get_item(db: Session,item_id: int):
    return db.query(Estoque).filter(Estoque.id_produto == item_id).first()

def get_items(db:Session):
    return db.query(Estoque).all()

def create_item(db:Session,item:EstoqueCreate):
    db_estoque = Estoque(**item.model_dump())
    db.add(db_estoque)
    db.commit()
    db.refresh(db_estoque)
    return db_estoque

def update_item(db:Session, item_id: int,item:EstoqueUpdate):
    db_estoque = db.query(Estoque).filter(Estoque.id_produto == item_id).first()

    if db_estoque is None:
        return None
    if db_estoque.nome_produto:
        db_estoque.nome_produto = item.nome_produto
    if db_estoque.quantidade:
        db_estoque.quantidade = item.quantidade
    if db_estoque.marca:
        db_estoque.marca = item.marca
    if db_estoque.valor:
        db_estoque.valor = item.valor

    db.commit()
    return db_estoque

def delete_item(db:Session,item_id:Estoque):
    db_estoque = db.query(Estoque).filter(Estoque.id_produto == item_id).first()
    db.delete(db_estoque)
    db.commit()
    return db_estoque
