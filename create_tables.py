from db.database import engine , Base
from db.database import models

print("Creating tables...")

Base.metadata.creat_all(
    bind = engine
)

print("Tables created successfully!")