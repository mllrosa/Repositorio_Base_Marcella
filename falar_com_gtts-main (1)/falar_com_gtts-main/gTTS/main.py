
from gtts import gTTS # Importa a biblioteca para converter texto em fala
import pygame # Importa a biblioteca para tocar áudio

texto = "Olá, turma! Vamos aprender Python falando!" # Texto que será convertido em voz

# Cria o objeto que converte texto para áudio em português
tts = gTTS(texto, lang="pt")

# Salva o áudio gerado em um arquivo MP3
tts.save("fala.mp3")

# Inicializa o mixer de áudio do pygame
pygame.mixer.init()

# Carrega o arquivo de áudio salvo
pygame.mixer.music.load("fala.mp3")

# Começa a tocar o áudio
pygame.mixer.music.play()

# Mantém o programa rodando até o áudio terminar
while pygame.mixer.music.get_busy():
    pass
