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

 1. Sube un archivo de audio .wav o graba directo en el navegador otorgando permisos a la aplicación (Sección 1)

 2. Selecciona el tipo de filtro que quieres aplicar (Sección 2)

 3. Ajusta la frecuencia de corte o banda (Sección 3)

 4. Activa o desactiva la visualización FFT (Sección 2)

 5. Haz clic en "Procesar" y visualiza tanto la señal filtrada como la original y su respectiva transformada de Fourier

 6. Descarga el audio procesado si lo deseas (Sección final)

![Interfaz 1](https://github.com/user-attachments/assets/24799652-ae59-4cfd-acb9-44d9ed0bfebe)
![Interfaz 2](https://github.com/user-attachments/assets/ec8899fd-f2f9-4a60-bda0-72e4ccad231a)



# 🛠 Requisitos

Python 3.10

## Instalación rápida

Requiere Python 3.8+

```bash
git clone https://github.com/Juan-117/SI-HSI.git
cd SI-HSI
pip install -r requirements.txt
```


## Se utilizan las siguientes librerías:

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
Juan Antonio Mancera Velasco

Proyecto académico — Tecnológico de Monterrey (2025)
