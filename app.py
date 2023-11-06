import os
import requests
import time
# from dotenv import load_dotenv
#
# load_dotenv()
ping_url = os.environ.get("ping_url")
ping_interval = int(os.environ.get("ping_interval"))

while True:
    try:
        print('Attempting to ping...')
        requests.get(f'{ping_url}', timeout=10)
        print('Ping was successful!')
    except requests.RequestException as e:
        print("Ping failed: %s" % e)
    print(f'Waiting {ping_interval} seconds before retrying...\n')
    time.sleep(ping_interval)
    