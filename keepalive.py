from flask import Flask, jsonify
import schedule
import time
import requests
import threading
from datetime import datetime

app = Flask(__name__)

# Variáveis globais para armazenar o status e hora da última requisição
last_status = None
last_request_time = None
API_URL = "https://mercantilsantamaria-api.onrender.com/swagger-ui/index.html#/"  # Substitua pela sua URL

# Função que faz a requisição para a API
def keep_alive():
    global last_status, last_request_time
    try:
        response = requests.get(API_URL)
        last_status = response.status_code
        last_request_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Ping bem-sucedido: {last_status} - {last_request_time}")
    except Exception as e:
        last_status = "Falha"
        last_request_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Erro ao tentar fazer o ping: {str(e)}")

# Agendar para rodar a cada 5 minutos
schedule.every(14).minutes.do(keep_alive)

# Função que roda o agendamento em segundo plano
def run_schedule():
    while True:
        print("requisicao feita")
        schedule.run_pending()
        time.sleep(1)

# Rota Flask para verificar o status da última requisição
@app.route('/status', methods=['GET'])
def status():
    if last_status is not None and last_request_time is not None:
        return jsonify({
            "status": last_status,
            "time": last_request_time
        })
    else:
        return jsonify({
            "message": "Nenhuma requisição feita ainda."
        })

# Iniciar o agendamento em uma thread separada
if __name__ == '__main__':
    t = threading.Thread(target=run_schedule)
    t.start()
    # Iniciar o servidor Flask
    app.run(host='0.0.0.0', port=5000)
