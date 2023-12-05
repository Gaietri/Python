
import requests

result = requests.get("http://127.0.0.1:5000/get_data?name=gaya")

assert dict(result.json()).get("caller_name") == "sachin", "name not matching"

