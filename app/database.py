from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://rubenpatrones:elgranfernan1$@patrones.database.windows.net:1433/taskcontrol?driver=ODBC+Driver+18+for+SQL+Server"

class Database:
    _engine = None
    _SessionLocal = None

    @classmethod
    def get_engine(cls):
        if cls._engine is None:
            cls._engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
        return cls._engine

    @classmethod
    def get_session(cls):
        if cls._SessionLocal is None:
            cls._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls.get_engine())
        return cls._SessionLocal

Base = declarative_base()

