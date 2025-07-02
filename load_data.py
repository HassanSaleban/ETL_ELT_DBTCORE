import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd

# Charger les variables d'environnement
load_dotenv(".env_pass")

username = os.getenv("DB_USER").strip()
password = os.getenv("DB_PASSWORD").strip()
host = os.getenv("DB_HOST").strip()
port = os.getenv("DB_PORT").strip()
database = os.getenv("DB_NAME").strip()

# Construire l'URL SQLAlchemy
DATABASE_URL = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
print("URL =", DATABASE_URL)

# Créer l'engine
engine = create_engine(DATABASE_URL)

# Créer la base si elle n'existe pas
if not database_exists(engine.url):
    create_database(engine.url)
    print("✅ Base de données créée.")
else:
    print("ℹ️ La base de données existe déjà.")

# Liste des tables à charger
liste_tables = ["customers", "items", "orders", "products", "stores", "supplies"]

# Charger et insérer les données pour chaque table
for table in liste_tables:
    try:
        csv_url = f"https://raw.githubusercontent.com/dsteddy/jaffle_shop_data/main/raw_{table}.csv"
        print(f"\n🔄 Lecture du fichier : {csv_url}")
        df = pd.read_csv(csv_url)
        df.to_sql(table, con=engine, if_exists="replace", index=False)
        print(f"✅ Table '{table}' insérée ({len(df)} lignes).")
    except Exception as e:
        print(f"❌ Erreur pour '{table}' ➜ {e}")
