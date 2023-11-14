import cv2
import numpy as np
from moviepy.editor import *

def image_to_mp4(image_path, output_path):
    audio_duration = 10
    
    image = cv2.imread(image_path)

    # Obtener el ancho y alto de la imagen
    image_width = image.shape[1]
    image_height = image.shape[0]

    # Definir el ancho y alto del video basado en la imagen
    video_width = image_width
    video_height = image_height

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = 30  # Ejemplo: 30 fotogramas por segundo
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (video_width, video_height))

    # Generar el video fotograma por fotograma
    for t in np.linspace(0, audio_duration, int(audio_duration * fps)):
        # Superponer la imagen en cada fotograma del video
        frame = np.copy(image)

        video_writer.write(frame)

    # Guarda Video
    video_writer.release()

def apply_audio(audio_path, output_path):
    videoclip = VideoFileClip(output_path)
    audioclip = AudioFileClip(audio_path)

    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(output_path)


audio_path = "Out.wav"
image_path = "3.jpg"
output_path = "ruta_de_salida_arwwwchivo.mp4"

image_to_mp4(image_path, output_path)
apply_audio(audio_path, output_path)
