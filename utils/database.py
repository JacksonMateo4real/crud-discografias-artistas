from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOOST = os.getenv('DB_HOOST')
DB_NAME = os.getenv('DB_NAME')

# esto solo crea la conexion...
engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOOST}', echo=True)


with engine.connect() as conn:
    conn.execute(text('CREATE DATABASE IF NOT EXISTS Discografias'))


# esto crea la conexion pero a la base de datos, importante para que asi Session se conecte a esta.
engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOOST}/{DB_NAME}', echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
    
