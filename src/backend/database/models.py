from sqlalchemy import String, Integer,Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Estoque(Base):
    __tablename__ = 'Estoque'
    id_produto: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    nome_produto: Mapped[str] = mapped_column(String())
    quantidade: Mapped[int] = mapped_column(Integer())
    marca: Mapped[str] = mapped_column(String())
    valor: Mapped[float] = mapped_column(Float())