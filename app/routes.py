from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends, Path
from models.models import ArtistaModel, AlbumModel, CancionModel
from schemas.schemas import ArtistaCreate, ArtistaUpdate, ArtistaOut
from schemas.schemas import AlbumCreate, AlbumUpdate, AlbumOut
from schemas.schemas import CancionCreate, CancionUpdate, CancionOut
from schemas.schemas import ArtistaOut
from utils.database import get_db
from typing import Annotated


manager = APIRouter()



@manager.get('/artista/{id}', response_model=ArtistaOut)
async def get_artista_discografia(id = Annotated[int, Path(gt=0)], db:Session = Depends(get_db)):
    
    artista_discografia = db.query(ArtistaModel)\
    .options(joinedload(ArtistaModel.albums), joinedload(ArtistaModel.canciones))\
    .filter(ArtistaModel.id == id)\
    .first()
    
    if not artista_discografia:
        raise HTTPException(HTTP_NOT_FOUND_404, status_code = 404, detail = "Sin resultados en la busqueda.")
    return artista_discografia

@manager.post('/artista', response_model = ArtistaOut)
async def post_nuevo_artista(artista_data: ArtistaCreate, db:Session = Depends(get_db)):
    
    artista = ArtistaModel(
        nombre=artista_data.nombre,
        nombre_artistico=artista_data.nombre_artistico,
        origen=artista_data.origen,
        biografia=artista_data.biografia,
        imagen_url=artista_data.imagen_url
    )

    db.add(artista)
    db.commit()
    db.refresh(artista)

    return artista

@manager.post('/album', response_model = AlbumOut)
async def post_nuevo_album(album_data: AlbumCreate, db:Session = Depends(get_db)):
    
    album = AlbumModel(
        nombre=album_data.nombre,
        genero=album_data.genero,
        fecha_estreno=album_data.fecha_estreno,
        artista_id=album_data.artista_id
    )

    db.add(album)
    db.commit()
    db.refresh(album)

    return album

@manager.post('/cancion', response_model = CancionOut)
async def post_nueva_cancion(cancion_data: CancionCreate, db:Session = Depends(get_db)):
    
    cancion = CancionModel(
        nombre=cancion_data.nombre,
        genero=cancion_data.genero,
        fecha_estreno=cancion_data.fecha_estreno,
        artista_id=cancion_data.artista_id,
        album_id=cancion_data.album_id
    )

    db.add(cancion)
    db.commit()
    db.refresh(cancion)

    return cancion


@manager.delete('/artista/{id}')
async def delete_artista(id: Annotated[int, Path(gt=0)], db:Session = Depends(get_db)):
    artista_a_eliminar = db.query(ArtistaModel).filter(ArtistaModel.id == id).first()
    
    if not artista_a_eliminar:
        raise HTTPException(HTTP_NOT_FOUND_404, status_code = 404, detail = "Sin resultados en la busqueda.")

    # Eliminar las relaciones con albums y canciones
    db.query(AlbumModel).filter(AlbumModel.artista_id == id).delete()
    db.query(CancionModel).filter(CancionModel.artista_id == id).delete()   

    db.delete(artista_a_eliminar)
    db.commit()
    return JSONResponse({"Mensaje": f"Artista {artista_a_eliminar} eliminado"})




@manager.delete('/album/{id}')
async def delete_album(id: Annotated[int, Path(gt=0)], db:Session = Depends(get_db)):
    album_a_eliminar = db.query(AlbumModel).filter(AlbumModel.id == id).first()
    
    if not album_a_eliminar:
        raise HTTPException(HTTP_NOT_FOUND_404, status_code = 404, detail = "Sin resultados en la busqueda.")
    
    # Eliminar las relaciones con canciones
    db.query(CancionModel).filter(CancionModel.album_id == id).delete()     
    db.delete(album_a_eliminar)
    return JSONResponse({"Mensaje": f"Album {album_a_eliminar} eliminado"})



@manager.delete('/cancion/{id}')
async def delete_cancion(id: Annotated[int, Path(gt=0)], db:Session = Depends(get_db)):
    cancion_a_eliminar = db.query(CancionModel).filter(CancionModel.id == id).first()
    
    if not cancion_a_eliminar:
        raise HTTPException(HTT_NOT_FOUND_404, status_code = 404, detail = "Sin resultados en la busqueda.")
     
    db.delete(cancion_a_eliminar)
    return JSONResponse({"Mensaje": f"Cancion {cancion_a_eliminar} eliminada"})