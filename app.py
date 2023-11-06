import os
import requests
import time

ping_url = os.environ.get("ping_url")
ping_interval = int(os.environ.get("ping_interval"))
ping_timeout = int(os.environ.get("ping_timeout"))

while True:
    try:
        print('Attempting to ping...')
        requests.get(f'{ping_url}', timeout=ping_timeout)
        print('Ping was successful!')
    except requests.RequestException as e:
        print("Ping failed: %s" % e)
    print(f'Waiting {ping_interval} seconds before retrying...\n')
    time.sleep(ping_interval)
    
