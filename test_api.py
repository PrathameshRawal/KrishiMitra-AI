import requests

API_KEY = "PASTE_YOUR_DATA_GOV_API_KEY_HERE"

url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"

params = {
    "api-key": API_KEY,
    "format": "json",
    "limit": 2,
    "filters[commodity]": "Soyabean"
}

print("Sending request...")

response = requests.get(url, params=params, timeout=60)

print("Status:", response.status_code)
print(response.text)