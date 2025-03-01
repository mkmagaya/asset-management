from sqlalchemy import create_engine
import psycopg2

# Database connection details
DB_NAME = "logistics_db"
DB_USER = "postgres"
DB_PASSWORD = "admin"
DB_HOST = "localhost"  # Change to your DB host if remote
DB_PORT = "5432"

# Create the database engine
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def get_connection():
    return engine.connect()
