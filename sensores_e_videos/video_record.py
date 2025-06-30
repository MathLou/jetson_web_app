import cv2
import requests
import os

def gravar_video(nome_arquivo, duracao=3, fps=20, camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    width = int(cap.get(3))
    height = int(cap.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(nome_arquivo, fourcc, fps, (width, height))

    for _ in range(int(fps * duracao)):
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    cap.release()
    out.release()

def enviar_video(caminho_video, url_server):
    url = f"{url_server}/video"
    with open(caminho_video, "rb") as f:
        files = {"video": (os.path.basename(caminho_video), f, "video/avi")}
        response = requests.post(url, files=files)
    print("Status envio vídeo:", response.status_code)
