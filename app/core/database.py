from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///app/db/tasks.db", echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
        