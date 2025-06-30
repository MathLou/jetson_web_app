import subprocess
import time
import json
import os
import requests
import signal
# lista de programa de sensores para serem lidos
server_link = "http://172.31.46.12:5000/"
SENSOR_SCRIPTS = ["GPS.py", "alerta.py", "link_send.py", "image_send.py"]
SENSOR_FILES = ["logs/GPS.json", "logs/alerta.json"]
POST_ROUTES = {
    "GPS": server_link+ "gps",
    "alerta": server_link + "alerta"
}
periodo = 4

# Guarda o número da última linha enviada de cada sensor
last_index_sent = {}

def start_sensors():
    processes = []
    for script in SENSOR_SCRIPTS:
        p = subprocess.Popen(["python3", script])
        processes.append(p)
        print(f"[main] Sensor {script} iniciado com PID {p.pid}")
    return processes

def read_sensor_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)  # Espera uma lista de dicts
    except Exception as e:
        print(f"[main] Erro ao ler {filename}:", e)
        return []

def post_to_flask(route, payload):
    try:
        url = POST_ROUTES.get(route)
        if not url:
            print(f"[main] Rota desconhecida: {route}")
            return
        r = requests.post(url, json=payload)
        print(f"[main] POST para {route}: {r.status_code}")
    except Exception as e:
        print(f"[main] Falha no POST para {route}:", e)

def stop_sensors(processes):
    for p in processes:
        print(f"[main] Encerrando sensor PID {p.pid}")
        p.send_signal(signal.SIGINT)
        p.wait()

if __name__ == "__main__":
    processes = start_sensors()

    try:
        while True:
            for file in SENSOR_FILES:
                sensor_name = os.path.basename(file).replace(".json", "")
                data_list = read_sensor_data(file)

                if not isinstance(data_list, list):
                    continue

                last_index = last_index_sent.get(sensor_name, -1)

                if len(data_list) > last_index + 1:
                    new_data = data_list[last_index + 1:]
                    for entry in new_data:
                        post_to_flask(sensor_name, entry)
                    last_index_sent[sensor_name] = len(data_list) - 1
                else:
                    print(f"[main] Nenhum novo dado para {sensor_name}")
            time.sleep(periodo)
    except KeyboardInterrupt:
        print("[main] Encerrando subprocessos...")
        stop_sensors(processes)
