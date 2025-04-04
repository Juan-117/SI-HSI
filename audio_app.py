"""App de procesamiento de audio con filtros y visualización en Gradio."""

import gradio as gr
import librosa
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from scipy.signal import butter, lfilter


def apply_filter(
    audio, sr, filter_type, cutoff, order, low_cut=None, high_cut=None
):
    """Aplica un filtro digital al audio según el tipo y parámetros dados."""
    nyquist = 0.5 * sr
    if filter_type == "Pasa-bajas":
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype="low", analog=False)
    elif filter_type == "Pasa-altas":
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype="high", analog=False)
    elif (
        filter_type == "Pasa-banda"
        and low_cut is not None
        and high_cut is not None
    ):
        low = low_cut / nyquist
        high = high_cut / nyquist
        b, a = butter(order, [low, high], btype="band")
    else:
        return audio

    return lfilter(b, a, audio)


def process_audio(
    file, filter_type, cutoff, low_cut, high_cut, order, apply_fft
):
    """Procesa el archivo de audio, aplica filtros, grafica."""
    audio, sr = librosa.load(file, sr=None)

    if filter_type == "Pasa-banda":
        audio_filtered = apply_filter(
            audio, sr, filter_type, None, order, low_cut, high_cut
        )
    else:
        audio_filtered = apply_filter(audio, sr, filter_type, cutoff, order)

    max_val = max(np.max(np.abs(audio)), np.max(np.abs(audio_filtered)))

    # Señal original
    plt.figure(figsize=(10, 4))
    plt.plot(audio, label="Original")
    plt.title("Señal Original")
    plt.xlabel("Muestras")
    plt.ylabel("Amplitud")
    plt.ylim(-max_val, max_val)
    plt.legend()
    plt.savefig("original.png", dpi=80)
    plt.close()

    # Señal filtrada
    plt.figure(figsize=(10, 4))
    plt.plot(audio_filtered, label="Filtrada", color="orange")
    plt.title("Señal Filtrada")
    plt.xlabel("Muestras")
    plt.ylabel("Amplitud")
    plt.ylim(-max_val, max_val)
    plt.legend()
    plt.savefig("filtered.png", dpi=80)
    plt.close()

    fft_original_image = fft_filtered_image = None

    if apply_fft:
        fft_audio_original = np.abs(np.fft.fft(audio))
        freqs_original = np.fft.fftfreq(len(fft_audio_original), 1 / sr)[
            : len(fft_audio_original) // 2
        ]
        fft_audio_original = fft_audio_original[: len(fft_audio_original) // 2]
        mask = freqs_original <= 1000

        fft_audio_filtered = np.abs(np.fft.fft(audio_filtered))
        freqs_filtered = np.fft.fftfreq(len(fft_audio_filtered), 1 / sr)[
            : len(fft_audio_filtered) // 2
        ]
        fft_audio_filtered = fft_audio_filtered[: len(fft_audio_filtered) // 2]
        mask_filtered = freqs_filtered <= 1000

        max_fft_val = max(
            np.max(fft_audio_original[mask]),
            np.max(fft_audio_filtered[mask_filtered]),
        )

        plt.figure(figsize=(10, 4))
        plt.plot(freqs_original[mask], fft_audio_original[mask])
        plt.title("Transformada de Fourier de la Señal Original")
        plt.xlabel("Frecuencia (Hz)")
        plt.ylabel("Magnitud")
        plt.ylim(0, max_fft_val)
        plt.savefig("fft_original.png", dpi=80)
        plt.close()
        fft_original_image = "fft_original.png"

        plt.figure(figsize=(10, 4))
        plt.plot(
            freqs_filtered[mask_filtered], fft_audio_filtered[mask_filtered]
        )
        plt.title("Transformada de Fourier de la Señal Filtrada")
        plt.xlabel("Frecuencia (Hz)")
        plt.ylabel("Magnitud")
        plt.ylim(0, max_fft_val)
        plt.savefig("fft_filtered.png", dpi=80)
        plt.close()
        fft_filtered_image = "fft_filtered.png"

    sf.write("processed_audio.wav", audio_filtered, sr)

    return (
        "original.png",
        "filtered.png",
        fft_original_image,
        fft_filtered_image,
        "processed_audio.wav",
    )


with gr.Blocks(title="Procesador de Audio con Filtros") as demo:
    gr.Markdown("### 🎧 Procesador de Audio con Filtros Digitales")

    with gr.Row():
        file_input = gr.Audio(type="filepath", label="Archivo de Audio")

    with gr.Row():
        filter_type = gr.Dropdown(
            ["Ninguno", "Pasa-bajas", "Pasa-altas", "Pasa-banda"],
            value="Ninguno",
            label="Tipo de Filtro",
        )
        apply_fft = gr.Checkbox(
            label="Aplicar Transformada de Fourier", value=True
        )

    cutoff_slider = gr.Slider(
        100, 5000, value=1000, label="Frecuencia de Corte (Hz)", visible=True
    )
    band_low = gr.Slider(
        100, 5000, value=300, label="Frecuencia Baja (Hz)", visible=False
    )
    band_high = gr.Slider(
        100, 5000, value=1500, label="Frecuencia Alta (Hz)", visible=False
    )

    order_slider = gr.Slider(1, 6, value=4, label="Orden del Filtro")

    with gr.Row():
        btn = gr.Button("Aplicar Filtro")

    with gr.Row():
        out_original = gr.Image(label="Señal Original")
        out_filtered = gr.Image(label="Señal Filtrada")

    with gr.Group(visible=True) as fft_block:
        with gr.Row():
            fft_orig = gr.Image(label="FFT Original")
            fft_filt = gr.Image(label="FFT Filtrada")

    out_file = gr.File(label="Archivo Procesado")

    def update_visibility(f_type):
        """Actualiza la visibilidad de sliders según el filtro seleccionado."""
        return {
            cutoff_slider: gr.update(
                visible=f_type in ["Pasa-bajas", "Pasa-altas"]
            ),
            band_low: gr.update(visible=f_type == "Pasa-banda"),
            band_high: gr.update(visible=f_type == "Pasa-banda"),
        }

    def toggle_fft_visibility(show_fft):
        """Muestra u oculta los bloques de FFT según el checkbox."""
        return gr.update(visible=show_fft)

    filter_type.change(
        update_visibility, filter_type, [cutoff_slider, band_low, band_high]
    )
    apply_fft.change(toggle_fft_visibility, apply_fft, fft_block)

    btn.click(
        fn=process_audio,
        inputs=[
            file_input,
            filter_type,
            cutoff_slider,
            band_low,
            band_high,
            order_slider,
            apply_fft,
        ],
        outputs=[
            out_original,
            out_filtered,
            fft_orig,
            fft_filt,
            out_file,
        ],
    )


if __name__ == "__main__":
    demo.launch()
