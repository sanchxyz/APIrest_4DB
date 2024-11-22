from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuración de conexión
DATABASE_URL = "mysql+pymysql://root:F1ngerpr@nt@localhost/mi_base_datos"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)

# Configurar la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
