from pydantic import BaseModel,PositiveFloat,PositiveInt
from typing import Optional

class EstoqueBase(BaseModel):
    nome_produto: str
    quantidade: PositiveInt
    marca: str
    valor: PositiveFloat

class EstoqueCreate(EstoqueBase):
    pass

class EstoqueResponse(EstoqueBase):
    id_produto:int

class EstoqueUpdate(EstoqueBase):
    nome_produto: Optional[str] = None
    quantidade: Optional[PositiveInt] = None
    marca: Optional[str] = None
    valor: Optional[PositiveFloat] = None

class EstoqueDelete(EstoqueBase):
    id_produto:int  