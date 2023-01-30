import requests
import time

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1069644939195076608/YUN2nnRIdiOyIxO54Yyk-wKv-57lDzNJLGfDj8b-MUdhBbA6Gb2CfW7lqyQG6--FZw5T"
LAST_IP = "86.207.124.162" # Mettez ici l'@ IP connu

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
    time.sleep(60)
