from gtts import gTTS
import pygame

# Criar um programa que receba texto do usuário e fale em português
# Alterar para outro idioma
# Criar um atendimento

texto = input("Digite o texto:")
try:
    idioma = input("Escolha o idioma (pt, fr, en, es):")
except:
    print("Digite corretamente!")
nome_arquivo = input("escolha um nome para seu audio:")
arquivo = nome_arquivo + ".mp3"

tts = gTTS(texto, lang= idioma)
tts.save(arquivo)

pygame.mixer.init()
pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
