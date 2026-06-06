import os

from cryptography.hazmat.primitives.ciphers import (
    Cipher,
    algorithms,
    modes
)

from utils.constants import (
    NONCE_SIZE,
    BUFFER_SIZE,
    TAG_SIZE,
    SALT_SIZE
)

from crypto.key_manager import (
    generate_salt,
    generate_key
)


def generate_nonce() -> bytes:
    """
    Genera un nonce seguro para AES-GCM.
    """

    return os.urandom(NONCE_SIZE)


def encrypt_file(
    input_file: str,
    output_file: str,
    password: str
) -> None:
    """
    Cifra un archivo utilizando AES-256-GCM.
    """

    salt = generate_salt()

    nonce = generate_nonce()

    key = generate_key(
        password,
        salt
    )

    cipher = Cipher(
        algorithms.AES(key),
        modes.GCM(nonce)
    )

    encryptor = cipher.encryptor()

    with open(input_file, "rb") as infile, \
         open(output_file, "wb") as outfile:

        # Salt
        outfile.write(salt)

        # Nonce
        outfile.write(nonce)

        # Datos cifrados
        while True:

            chunk = infile.read(
                BUFFER_SIZE
            )

            if not chunk:
                break

            encrypted_chunk = encryptor.update(
                chunk
            )

            outfile.write(
                encrypted_chunk
            )

        # Finalizar cifrado
        outfile.write(
            encryptor.finalize()
        )

        # Tag GCM
        outfile.write(
            encryptor.tag
        )


def decrypt_file(input_file: str,output_file: str,password: str) -> None:

    file_size = os.path.getsize(input_file)

    with open(input_file, "rb") as infile:

        salt = infile.read(SALT_SIZE)

        nonce = infile.read(NONCE_SIZE)

        infile.seek(file_size - TAG_SIZE)

        tag = infile.read(TAG_SIZE)

        key = generate_key(password,salt)

        cipher = Cipher(algorithms.AES(key),modes.GCM(nonce,tag))

        decryptor = cipher.decryptor()

        infile.seek(SALT_SIZE +NONCE_SIZE)

        ciphertext_size = (file_size- SALT_SIZE- NONCE_SIZE- TAG_SIZE)

        remaining = ciphertext_size

        with open(output_file,"wb") as outfile:

            while remaining > 0:

                chunk_size = min(BUFFER_SIZE,remaining)

                chunk = infile.read(chunk_size)

                remaining -= len(chunk)

                decrypted_chunk = (decryptor.update(chunk))

                outfile.write(decrypted_chunk)

            outfile.write(decryptor.finalize())