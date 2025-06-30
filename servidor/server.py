from flask import Flask, request, render_template, send_from_directory
import json
from datetime import datetime
import os

app = Flask(__name__)

# Armazenar os últimos dados recebidos
gps_data = {"latitude": "esperando", "longitude": "esperando", "epoch_time": "esperando"}
link_data = {"link": "esperando"}
image_data = {"image_base64": "esperando"}
alerta_data = {"alerta": "esperando"}


# Template HTML com CSS
HTML_TEMPLATE = 'index.html'

@app.route('/')
def index():
    return render_template(
        HTML_TEMPLATE,
        gps=gps_data,
        link=link_data,
        alerta=alerta_data,
        image=image_data
    )

@app.route('/gps', methods=['POST'])
def receive_gps():
    global gps_data
    data = request.get_json() or {}
    
    # Atualiza os dados, usando "esperando" para campos vazios ou ausentes
    gps_data = {
        "latitude": str(data.get('latitude', 'esperando')) or "esperando",
        "longitude": str(data.get('longitude', 'esperando')) or "esperando",
        "timestamp": str(data.get('timestamp', 'esperando')) or "esperando"
    }
    
    return render_template(
        HTML_TEMPLATE,
        gps=gps_data,
        link=link_data,
        alerta=alerta_data,
        image=image_data
    )

@app.route('/link', methods=['POST'])
def receive_link():
    global link_data
    data = request.get_json() or {}
    
    # Atualiza o link, usando "esperando" se vazio ou ausente
    link_data = {
        "link": str(data.get('link', 'esperando')) or "esperando"
    }
    return render_template(
        HTML_TEMPLATE,
        gps=gps_data,
        link=link_data,
        alerta=alerta_data,
        image=image_data
    )

@app.route('/alerta', methods=['POST'])
def receive_alerta():
    global alerta_data
    data = request.get_json() or {}
    
    # Atualiza o link, usando "esperando" se vazio ou ausente
    alerta_data = {
        "alerta": str(data.get('alerta', 'esperando')) or "esperando"
    }
    
    return render_template(
        HTML_TEMPLATE,
        gps=gps_data,
        link=link_data,
        alerta=alerta_data,
        image=image_data
    )

@app.route('/image', methods=['POST'])
def receive_image():
    global image_data
    data = request.get_json() or {}
    
    # Atualiza a imagem, usando "esperando" se vazio ou ausente
    image_data = {
        "image_base64": str(data.get('image_base64', 'esperando')) or "esperando"
    }
    
    return render_template(
        HTML_TEMPLATE,
        gps=gps_data,
        link=link_data,
        alerta=alerta_data,
        image=image_data
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)