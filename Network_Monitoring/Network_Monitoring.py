import os
import time
import multiprocessing
import csv

ip = input('Insira as 3 primeiras camadas do IP: ')
equipment_quantity = int(input('Insira a quantidades de equipamentos: '))


# List of IP addresses or hostnames of 100 computers.
computers = [f'{ip}.{i}' for i in range(2, equipment_quantity + 1)]  # Example of IPs

# Function to ping a computer.
def check_ping(ip):
    
    response = os.system(f'ping -n 1 -W 1000 {ip}')
    status = 'Online' if response == 0 else 'Offline'
    
    # Store the status in a CSV file.
    with open('NetworkMonitoring.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ip, status, time.strftime('%Y-%m-%d | %H:%M:%S')])
    
    print(f'{ip} this {status}')

# Function for monitoring with multiprocessing.
def monitor_computers():
    
    # Creation of the CSV file.
    with open('NetworkMonitoring.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['IP','STATUS', 'DATE | TIME'])
    
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(check_ping, computers)

# Monitor periodically.
while True:
    monitor_computers()
    time.sleep(10)  # Check every 60 seconds.