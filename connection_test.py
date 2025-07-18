import ollama
import requests

# RunPod'un external port'unu kullan
RUNPOD_HOST = "http://157.157.221.29:19687"

# Direkt HTTP API testi
def test_connection():
    try:
        response = requests.get(f"{RUNPOD_HOST}/api/tags")
        print(f"Connection Status: {response.status_code}")
        print(f"Available models: {response.json()}")
        return True
    except Exception as e:
        print(f"Connection failed: {e}")
        return False

# Ollama client ile bağlantı
client = ollama.Client(host=RUNPOD_HOST)

# Model listesi
try:
    models = client.list()
    print("Available models:", models)
except Exception as e:
    print("Error:", e)

# Chat testi
try:
    response = client.chat(model='llama3.1:8b', messages=[
        {'role': 'user', 'content': 'Hello! How are you?'}
    ])
    print("Response:", response['message']['content'])
except Exception as e:
    print("Chat error:", e)