from pydantic import BaseModel,PositiveFloat,PositiveInt
from typing import Optional

class EstoqueBase(BaseModel):
    '''Esquema Base para validação dos Dados'''
    nome_produto: str
    quantidade: PositiveInt
    marca: str
    valor: PositiveFloat

class EstoqueCreate(EstoqueBase):
    '''Esquema de validação para o POST(Inserção de novos dados)'''
    pass

class EstoqueResponse(EstoqueBase):
    '''Esquema de validação do GET Items - Valida a inserção'''
    id_produto:int

class EstoqueUpdate(EstoqueBase):
    '''Esquema de validação do PUT(Atualiza o dado)'''
    nome_produto: Optional[str] = None
    quantidade: Optional[PositiveInt] = None
    marca: Optional[str] = None
    valor: Optional[PositiveFloat] = None

class EstoqueDelete(EstoqueBase):
    '''Esquema de validação do Delete'''
    id_produto:int  