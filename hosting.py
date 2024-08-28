from flask import Flask
from pyngrok import ngrok

# Ustawienie authtoken, jeśli jeszcze tego nie zrobiłeś
ngrok.set_auth_token('Wpisać token z konta Ngrok.')

# Tworzenie aplikacji Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, ngrok!"

# Uruchomienie tunelu ngrok
http_tunnel = ngrok.connect(5000)  # Użyj dostępnego portu, np. 5000
print(f'Public URL: {http_tunnel.public_url}')

# Uruchomienie serwera
if __name__ == '__main__':
    app.run(port=5000)  # Użyj tego samego portu co w ngrok.connect()
