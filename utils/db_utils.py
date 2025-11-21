from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
import geopandas as geopandas
from .config import DB_CONFIG

def get_engine(config=DB_CONFIG):
    """
    Create SQLalchemy engine from config dictionary
    dialect+driver://username:password@host:port/database
    """
    url = (
        f"postgresql://{DB_CONFIG['username']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )
    return create_engine(url, pool_pre_ping=True)

def test_connection(engine=None):
    engine = engine or get_engine()
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            print("Connection successful!")
            print("PostgreSQL version:", result.fetchone()[0])
            return True
    except Exception as e:
        print("Connection failed!", e)
        return False

def load_query(query: str, engine=None):
    """
    Jalankan query SQL dan return DataFrame
    """
    engine = engine or get_engine()
    with engine.connect() as conn:
        return pd.read_sql_query(text(query), conn)