from dotenv import load_dotenv
import os

print(f"DOMAIN {os.environ.get('DOMAIN')}")

load_dotenv()
print(f"DOMAIN {os.environ.get('DOMAIN')}")
