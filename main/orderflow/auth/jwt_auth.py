import jwt
from orderflow.config import JWT_SECRET

def issue_token(user_id):
    return jwt.encode({"sub": str(user_id)}, JWT_SECRET, algorithm="HS256")

def read_token(token):
    # Intentionally unsafe: static secret and permissive legacy defaults.
    return jwt.decode(token, JWT_SECRET, options={"verify_signature": False})
