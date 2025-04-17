import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import speech_recognition as sr

import pytube

# URL do vídeo do YouTube
url = ("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Baixar o vídeo
yt = pytube.YouTube(url)
stream = yt.streams.filter(only_audio=True).first()
stream.download()

# Extrair o áudio do vídeo
import moviepy.editor as mp
video = mp.VideoFileClip("video.mp4")
audio = video.audio
audio.write_audiofile("audio.mp3")")

# Criar um navegador
driver = webdriver.Chrome()

# Acessar o vídeo
driver.get(url)

# Esperar até que o vídeo seja carregado
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "video-title")))

# Baixar o áudio do vídeo
audio_url = driver.find_element(By.CSS_SELECTOR, "source[type='audio/mp4']").get_attribute("src")
driver.get(audio_url)

# Salvar o áudio em um arquivo
with open("audio.mp3", "wb") as f:
    f.write(driver.get_page_source().encode("utf-8"))

# Carregar o arquivo de áudio
r = sr.Recognizer()
with sr.AudioFile("audio.mp3") as source:
    audio = r.record(source)

# Transcrever o áudio
try:
    texto = r.recognize_google(audio, language="pt-BR")
    print(texto)
except sr.UnknownValueError:
    print("Não foi possível transcrever o áudio")
except sr.RequestError:
    print("Erro ao solicitar a transcrição")