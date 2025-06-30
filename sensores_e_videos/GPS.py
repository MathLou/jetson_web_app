import json
import time
import random
from datetime import datetime
from zoneinfo import ZoneInfo

now_sp = datetime.now(ZoneInfo("America/Sao_Paulo"))
timestamp = now_sp.isoformat()
# file = f"logs/GPS_{timestamp}.json"
file = "logs/GPS.json"

time.sleep(5) # simulating GPS
periodo = 2
data = []
try:
    with open(file, "r") as f:
        data = json.load(f)
except:
    data = []

while True:
    latitude = -23.5 + random.uniform(-0.01, 0.01)
    longitude = -46.6 + random.uniform(-0.01, 0.01)
    data.append({
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": timestamp
    })

    with open(file, "w") as f:
        json.dump(data, f, indent=2)

    time.sleep(periodo)