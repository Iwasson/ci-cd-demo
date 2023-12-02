import os
from dotenv import load_dotenv

load_dotenv()

SUPER_SECRET_PASSWORD = os.getenv("SUPER_SECRET_PASSWORD")
print(f"THIS IS MY PASSWORD {SUPER_SECRET_PASSWORD}")
