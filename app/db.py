from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://rubenpatrones:elgranfernan1$@patrones.database.windows.net:1433/taskcontrol?driver=ODBC+Driver+18+for+SQL+Server"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()  
    except:
        db.rollback() 
        raise
    finally:
        db.close()

