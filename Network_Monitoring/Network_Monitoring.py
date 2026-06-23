import os
import time
import multiprocessing
import csv

# Lista de IPs ou hostnames dos 800 computadores
computadores = [f'10.182.4.{i}' for i in range(2, 802)]  # Exemplo de IPs

# Função para pingar um computador
def verificar_ping(ip):
    response = os.system(f'ping -n 1 -W 1000 {ip}')
    status = 'online' if response == 0 else 'offline'
    
    # Armazenar o status em um arquivo CSV
    with open('monitoramento.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ip, status, time.strftime('%Y-%m-%d %H:%M:%S')])
    
    print(f'{ip} está {status}')

# Função para monitoramento com multiprocessing
def monitorar_computadores():
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(verificar_ping, computadores)

# Monitorar periodicamente
while True:
    monitorar_computadores()
    time.sleep(60)  # Verifica a cada 60 segundos