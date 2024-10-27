import requests

response=requests.get("http://localhost:5002/get_pod_id")

if response.status_code==200:
    print("Successfully")
    print(response.content)
else:
    print("Error: %s" % response.status_code)