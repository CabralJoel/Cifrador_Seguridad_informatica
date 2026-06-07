# Cifrador_Seguridad_informatica

Cifrador de Archivos AES-256

Cifrador de archivos usando python para TP2 la materia de seguridad informática

Tecnologías utilizadas

Python 3.13.2
Cryptography 48.0.0
AES-256-GCM
PBKDF2-HMAC-SHA256

Instalación

Crear y activar un entorno virtual:

python -m venv venv

Windows:

venv\Scripts\activate

Instalar dependencias:

pip install -r requirements.txt
Uso

Cifrar un archivo:

python src/main.py encrypt "C:\Users\Usuario\Documentos\documento.pdf"

Descifrar un archivo:

python src/main.py decrypt "C:\Users\Usuario\Documentos\documento.pdf.enc"

Durante la ejecución se solicitará una contraseña.

Debe utilizarse la misma contraseña posteriormente para recuperar el archivo original.

El archivo cifrado o descifrado se generará en la misma ubicación del archivo de entrada.
