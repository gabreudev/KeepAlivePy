import requests
import time
import schedule

# Configurações da API e tempo de intervalo
API_URL = "https://mercantilsantamaria-api.onrender.com/swagger-ui/index.html#/"
INTERVALO_MINUTOS = 14

# Função para fazer o ping na API
def ping_api():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            print(f"Ping bem-sucedido: API ativa. Status: {response.status_code}")
        else:
            print(f"Falha no ping: Status {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao tentar fazer o ping: {e}")

# Função para converter minutos em milissegundos
def minutos_para_milisegundos(minutos):
    return minutos * 60 * 1000

# Agendar o ping a cada INTERVALO_MINUTOS
schedule.every(INTERVALO_MINUTOS).minutes.do(ping_api)

# Loop principal para manter o agendador rodando
if __name__ == "__main__":
    print(f"Iniciando KeepAlive. Verificando a cada {INTERVALO_MINUTOS} minutos.")
    
    # Executa o primeiro ping antes do loop
    ping_api()
    
    while True:
        # Executa as tarefas agendadas
        schedule.run_pending()
        time.sleep(1)
