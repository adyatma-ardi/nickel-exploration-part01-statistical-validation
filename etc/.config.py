import os
from dotenv import load_dotenv

# Coba ambil folder berdasarkan __file__, kalau gagal fallback ke cwd
try:
    BASE_DIR = os.path.dirname(__file__)  # .py script
except NameError:
    BASE_DIR = os.getcwd()                # notebook / interactive shell

dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=dotenv_path)

DB_CONFIG = {
    "username": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
}