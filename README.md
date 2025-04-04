🎧 Procesador de Audio con Filtros Digitales

Este proyecto permite aplicar filtros digitales (pasa-bajas, pasa-altas y pasa-banda) a archivos de audio .wav mediante una interfaz web desarrollada con Gradio.
También puedes visualizar la señal original, la señal filtrada y su análisis de frecuencia (FFT).
🧪 Instructivo paso a paso

    Abre tu terminal.

    Entra a la carpeta del proyecto:

cd SI_HSI

Activa el entorno virtual (si usas uno):

source hsiv/bin/activate

Instala las librerías necesarias:

pip install -r requirements.txt

Ejecuta la aplicación:

python audio_app.py

Abre tu navegador y entra a:

    http://localhost:7860

    En la interfaz web:

        Sube un archivo de audio .wav

        Selecciona el tipo de filtro que quieres aplicar

        Ajusta la frecuencia de corte o banda

        Activa o desactiva la visualización FFT

        Haz clic en "Aplicar Filtro"

        Descarga el archivo procesado si lo deseas

🛠 Requisitos

    Python 3.10

    Las siguientes librerías (incluidas en requirements.txt):

        gradio

        librosa

        matplotlib

        numpy

        scipy

        soundfile

📁 Estructura del Proyecto

SI_HSI/
│
├── audio_app.py         # Código principal de la aplicación
├── requirements.txt     # Librerías necesarias
├── README.md            # Este archivo con el instructivo
├── pyproject.toml       # Configuración de Black
└── .gitignore           # Archivos ignorados por Git

👨‍💻 Autor

Juan Antonio
Proyecto académico — Tecnológico de Monterrey (2025)
