from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date



class ArtistaBase(BaseModel):
    nombre: str = Field(max_length=30, description="Nombre del artista")
    nombre_artistico: str = Field(max_length=30, description="Nombre artístico del artista")
    origen: str = Field(max_length=30, description="Origen del artista")
    biografia: str = Field(description="Cuentanos un poco del artista")
    imagen_url: str = Field(description="URL imagen del artista")

class ArtistaCreate(ArtistaBase):
    pass


class ArtistaUpdate(BaseModel):
    nombre:Optional[str]= Field(max_length=30, default_factory=None, description="Nombre del artista")
    nombre_artistico:Optional[str] = Field(max_length=30, default_factory=None, description="Nombre artístico del artista")
    origen:Optional[str] = Field(max_length=30, default_factory=None, description="Origen del artista")
    biografia:Optional[str] = Field(default_factory=None, description="Cuentanos un poco del artista")
    imagen_url:Optional[str] = Field(default_factory=None, description="URL imagen del artista")

class ArtistaOut(ArtistaUpdate):
    id:Optional[int] 

    class Config:
        from_attributes = True

class AlbumBase(BaseModel):
    nombre: str = Field(max_length=30, description="Nombre del album")
    genero: str = Field(max_length=30, description="Genero musical del album")
    fecha_estreno: date = Field(description="Fecha estreno del album")
    artista_id: int 

class AlbumCreate(AlbumBase):
    pass

class AlbumUpdate(BaseModel):
    nombre:Optional[str]= Field(max_length=30, default_factory=None, description="Nombre del album")
    genero:Optional[str] = Field(max_length=30, default_factory=None, description="Genero musical del album")
    fecha_estreno:Optional[date] = Field(default_factory=None, description="Fecha estreno del album")
    

class AlbumOut(AlbumUpdate):
    id:Optional[int]

    class Config:
        from_attributes = True


class CancionBase(BaseModel):
    nombre:str= Field(max_length=30, description="Nombre de la cancion")
    genero:str = Field(max_length=30, description="Genero musical de la cancion")
    fecha_estreno:date = Field(description="Fecha estreno de la cancion")
    artista_id: int 
    album_id:Optional[int] = Field(default=None, description="ID del album al que pertenece la cancion")

class CancionCreate(CancionBase):
    pass

class CancionUpdate(BaseModel):
    nombre:Optional[str]= Field(max_length=30, default_factory=None, description="Nombre del album")
    genero:Optional[str] = Field(max_length=30, default_factory=None, description="Genero musical del album")
    fecha_estreno:Optional[date] = Field(default_factory=None, description="Fecha estreno del album")
    artista_id:Optional[int] 
    album_id:Optional[int]
    
class CancionOut(CancionUpdate):
    id:Optional[int]

    class Config:
        from_attributes = True



class ArtistaOut(ArtistaOut):
    albums:List[AlbumOut]
    canciones: List[CancionOut]

    class Config:
        from_attributes = True