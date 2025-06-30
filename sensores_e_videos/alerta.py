# sensor_2.py
import json
import time
import random
from datetime import datetime
from zoneinfo import ZoneInfo
import video_record
import main

file = "logs/alerta.json"
periodo = 2
data = []
alerta_id = 0
url_server = main.server_link

try:
    with open(file, "r") as f:
        data = json.load(f)
except:
    data = []

while True:
    # Simulate an alert detection
    alerta_list = ["ALERTA","normal","normal","normal","normal","normal"]
    alerta = random.choice(alerta_list)
    alerta_id += 1

    # If IA detect something, record a video
    now_sp = datetime.now(ZoneInfo("America/Sao_Paulo"))
    # if alerta == "ALERTA":
    #     video_file = f"static/videos/alerta_{alerta_id}_{now_sp.isoformat()}.avi"
    #     video_record.gravar_video(video_file, duracao=3, fps=20, camera_index=0)
    #     video_record.enviar_video(video_file,url_server)

    data.append({
        "alerta": alerta,
        "timestamp": now_sp.isoformat(),
        "alerta_id": alerta_id
    })

    with open(file, "w") as f:
        json.dump(data, f, indent=2)

    time.sleep(periodo)