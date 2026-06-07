import os
import hashlib

from utils.constants import (
    AES_KEY_SIZE,
    SALT_SIZE,
    PBKDF2_ITERATIONS,
    MIN_PASSWORD_LENGTH
)

def generate_key(password: str,salt: bytes) -> bytes:

    validate_password(password)

    return hashlib.pbkdf2_hmac("sha256",password.encode("utf-8"),salt,PBKDF2_ITERATIONS,dklen=AES_KEY_SIZE)


def validate_password(password: str) -> None:

    password = password.strip()

    if not password:
        raise ValueError("La contraseña no puede estar vacía.")

    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValueError(f"La contraseña debe tener al menos "f"{MIN_PASSWORD_LENGTH} caracteres.")

def generate_salt() -> bytes:

    return os.urandom(SALT_SIZE)