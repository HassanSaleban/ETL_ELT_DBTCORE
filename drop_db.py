from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, drop_database
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv(".env_pass")

username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
print("URL ciblée :", url)

if database_exists(url):
    print("Suppression de la base...")
    drop_database(url)
    print("Base supprimée.")
else:
    print("Base non trouvée.")
