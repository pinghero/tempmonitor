from hmac import compare_digest
from database.db_models import users
import hashlib

def verify_password(username, password):
    # Query users using given username
    user = users.query.filter(users.username == username).first()
    if user is not None:

        # Generate password hash using salt stored in Users table and password given from frontend
        generated_hash = hashlib.sha256(user.salt.encode() + password.encode()).hexdigest()

        # Compare generated password and stored password
        # When true authentication succeeded, else authentication failed
        if compare_digest(user.pwd_hash, generated_hash):
            print("Authenticated!")
            return username

    return False
