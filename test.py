import os
from dotenv import load_dotenv
import jwt
from auth.jwt import create_access_token

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

token = create_access_token(data={"sub": "1"})
print(f"Generated Token: {token}\n")

parts = token.split(".")
print(f"Number of parts in JWT: {len(parts)} (Should be 3)")

decoded_data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
print(f"Decoded Data: {decoded_data}")