import os
from sqla_wrapper import SQLAlchemy
# load environmental variables from .env file
from dotenv import load_dotenv
# Environment variables need to be imported before modules import
load_dotenv()

db_url = os.getenv("DATABASE_URL") \
                  .replace("postgres://", "postgresql://", 1)

db = SQLAlchemy(db_url)
