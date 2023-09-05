import requests
import time

endpoint = 'http://127.0.0.1:5000/'  

for _ in range(10):  # Send 10 requests
    response = requests.get(endpoint)
    if response.status_code == 200:
        print("Status Code: ", response.status_code)
    elif response.status_code == 429:
        print("Status Code: (Rate Limit Exceeded) ", response.status_code)
    time.sleep(0.1)  
