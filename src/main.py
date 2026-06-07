import os
import sys

from getpass import getpass

from crypto.aes_cipher import (encrypt_file,decrypt_file)


def show_usage() -> None:

    print("Uso: ejecute alguna de las siguientyes lineas de comando\n""  python src/main.py encrypt <archivo>\n""  python src/main.py decrypt <archivo>")


def main() -> None:

    try:

        if len(sys.argv) != 3:
            show_usage()
            return

        operation = sys.argv[1].lower()

        file_path = sys.argv[2]

        if not os.path.isfile(file_path):
            print("Error: el archivo especificado no existe.")
            return

        password = getpass( "Ingrese contraseña: ")

        if operation == "encrypt":

            output_file = (file_path + ".enc")

            encrypt_file(file_path,output_file,password)

            print(f"Archivo cifrado correctamente: "f"{output_file}")

        elif operation == "decrypt":

            if file_path.endswith(".enc"):

                output_file = (file_path[:-4])

            else:
                output_file = (file_path + ".dec")

            decrypt_file(file_path, output_file,password)

            print(f"Archivo descifrado correctamente: "f"{output_file}")

        else:
            show_usage()

    except Exception as e:

        print(f"Error: {e}")


if __name__ == "__main__":
    main()