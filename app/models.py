from sqlalchemy import Column, Integer, String, Text, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = "Usuarios"
    usuarioID = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(100), nullable=False)
    direccion = Column(String(255), nullable=False)

class Categorias(Base):
    __tablename__ = "Categorias"
    categoriaID = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)

class Productos(Base):
    __tablename__ = "Productos"
    productoID = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
    precio = Column(DECIMAL(10, 2), nullable=False)
    categoriaID = Column(Integer, ForeignKey("Categorias.categoriaID"), nullable=False)
    stock = Column(Integer, nullable=False)

class Pedidos(Base):
    __tablename__ = "Pedidos"
    pedidoID = Column(Integer, primary_key=True, index=True)
    usuarioID = Column(Integer, ForeignKey("Usuarios.usuarioID"), nullable=False)
    fecha = Column(DateTime, nullable=False)
    total = Column(DECIMAL(10, 2), nullable=False)

class Pedido_Productos(Base):
    __tablename__ = "Pedido_Productos"
    pedidoID = Column(Integer, ForeignKey("Pedidos.pedidoID"), primary_key=True)
    productoID = Column(Integer, ForeignKey("Productos.productoID"), primary_key=True)
    cantidad = Column(Integer, nullable=False)
    subtotal = Column(DECIMAL(10, 2), nullable=False)
