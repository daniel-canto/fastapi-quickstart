from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./app.db"

# Cria o engine para manipular o SQLite
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Instância da sessão (usada em cada request)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()