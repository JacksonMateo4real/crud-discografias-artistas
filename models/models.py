from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')


Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario = Column(String(15))
    nivel = Column(String(15))


class ArtistaModel(Base):
    __tablename__ = 'Artistas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30))
    nombre_artistico = Column(String(30))
    origen = Column(String(30))
    biografia = Column(Text)
    imagen_url = Column(Text)
    
    albums = relationship('AlbumModel', back_populates="artista")
    canciones = relationship('CancionModel', back_populates="artista")


class AlbumModel(Base):
    __tablename__ = 'Albumes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30))
    genero = Column(String(30))
    fecha_estreno = Column(Date)
    artist_id = Column(Integer, ForeignKey('Artistas.id'))
    
    canciones = relationship('CancionModel', back_populates="album")
    artista = relationship('ArtistaModel', back_populates="albums")


class CancionModel(Base):
    __tablename__ = 'Canciones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30))
    genero = Column(String(30))
    fecha_estreno = Column(Date)
    artist_id = Column(Integer, ForeignKey('Artistas.id'))
    album_id = Column(Integer, ForeignKey('Albumes.id'))

    artista = relationship('ArtistaModel', back_populates="canciones")
    album = relationship('AlbumModel', back_populates="canciones")

engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}', echo=True)

Base.metadata.create_all(bind=engine)