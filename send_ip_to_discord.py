import requests
import time

DISCORD_WEBHOOK_URL = "VOTRE_URL_DISCORD_WEBHOOK"
LAST_IP = "0.0.0.0" # Mettez ici l'@ IP connu

def send_discord_message(ip):
    embed = {
      "title": "⚙️ __Nouvelle IP publique du serveur :__",
      "description": f"L'adresse IP publique de votre serveur est maintenant **{ip}**.",
      "color": 3553599 # Coleur en décimal
    }
    requests.post(DISCORD_WEBHOOK_URL, json={"embeds": [embed]})

while True:
    response = requests.get("http://checkip.dyndns.org").text
    current_ip = response.split("Current IP Address: ")[1].strip()
    current_ip = current_ip.split("<",1)[0]

    print(current_ip)
    if current_ip != LAST_IP:
        LAST_IP = current_ip
        send_discord_message(current_ip)
    time.sleep(60) # Remplacez le "60" si vous voulez modifier le temps (en secondes)
