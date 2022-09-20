import os
from sqla_wrapper import SQLAlchemy

db_url = os.getenv("DATABASE_URL") \
                  .replace("postgres://", "postgresql://", 1)


db = SQLAlchemy(db_url)
