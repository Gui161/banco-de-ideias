from dotenv import load_dotenv
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError


import os


load_dotenv(".env")

host = os.getenv("DB_HOST")
dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = quote_plus(os.getenv("DB_PASSWORD"))
port = os.getenv("DB_PORT")

url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

engine = create_engine(url)
Sessao = sessionmaker(autocommit= False, autoflush=False, bind=engine)
base = declarative_base()
def get_sessao():
    return Sessao

