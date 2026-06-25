import os
import time
import multiprocessing
import csv

# List of IP addresses or hostnames of 100 computers.
computers = [f'0.0.0.{i}' for i in range(2, 103)]  # Example of IPs

# Creation of the CSV file.
with open('NetworkMonitoring.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['IP','STATUS', 'DATE | TIME'])

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
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(check_ping, computers)

# Monitor periodically.
while True:
    monitor_computers()
    time.sleep(10)  # Check every 60 seconds.