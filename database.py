from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from model import Base

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="nivedita",
    host="localhost",
    database="postgres",
    port=5432
)

engine = create_engine(url)
print(url)

Base.metadata.create_all(engine) # create all the database tables under base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # create a database session
