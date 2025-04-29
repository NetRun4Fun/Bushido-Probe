from flask import Flask, request
import socket
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/..."  # Replace with your BotGhost webhook URL

@app.route('/')
def home():
    return "Recon bot is live!"

@app.route('/recon', methods=['POST'])
def recon():
    data = request.json
    domain = data.get("domain")

    try:
        ip = socket.gethostbyname(domain)
        result = f"{domain} resolves to {ip}"
    except Exception as e:
        result = f"Error: {str(e)}"

    # Send the result back to Discord
    requests.post(DISCORD_WEBHOOK_URL, json={"content": result})
    return {"status": "done"}, 200
