from hmac import compare_digest
from database.db_models import users

def verify_password(username, password):
    user = users.query.filter(users.username == username).first()
    if user is not None:
        generated_hash = hashlib.sha256(user.salt.encode() + password.encode()).hexdigest()
        if compare_digest(user.pwd_hash, generated_hash):
            print("Pass is right")
            return username
    return False