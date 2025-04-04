# 🎧 Procesador de Audio con Filtros Digitales

Este proyecto permite aplicar filtros digitales (pasa-bajas, pasa-altas y pasa-banda) a archivos de audio .wav (mismos que se pueden subir o grabar directamente) mediante una interfaz web desarrollada con Gradio.También se puede visualizar la señal original, la señal filtrada y su análisis de frecuencia (FFT).


# 🧪 Instructivo paso a paso
 1. Abre tu terminal
 2. Entra a la carpeta del proyecto

        cd SI_HSI

 3. Activa el entorno virtual (si usas uno):

        source hsiv/bin/activate

Instala las librerías necesarias:

        pip install -r requirements.txt

Ejecuta la aplicación:

        python audio_app.py

Abre tu navegador y entra a:

    http://localhost:7860

    

 # En la interfaz web:

 1. Sube un archivo de audio .wav o graba directo en el navegador otorgando permisos a la aplicación

 2. Selecciona el tipo de filtro que quieres aplicar

 3. Ajusta la frecuencia de corte o banda

 4. Activa o desactiva la visualización FFT

 5. Haz clic en "Procesar"

 6. Descarga el archivo procesado si lo deseas



# 🛠 Requisitos

Python 3.10



# Se utilizan las siguientes librerías (incluidas en requirements.txt):

 gradio

 librosa

 matplotlib

 numpy

 scipy

 soundfile



# 📁 Estructura del Proyecto

    SI_HSI/
          │
          ├── audio_app.py         # Código principal de la aplicación
          ├── requirements.txt     # Librerías necesarias
          ├── README.md            # Este archivo con el instructivo
          ├── pyproject.toml       # Configuración de Black
          └── .gitignore           # Archivos ignorados por Git

# 👨‍💻 Autor
Juan Antonio
Proyecto académico — Tecnológico de Monterrey (2025)
