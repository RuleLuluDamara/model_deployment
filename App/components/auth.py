import hashlib

# User database
users_db = {
    "rule": {
        "name": "Admin",
        # sha256 of "password"
        "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
    }
}


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
