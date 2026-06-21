import os
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

mensagem = """
📱 ALERTA LG IMPORT

🔥 iPhone encontrado para revenda

Modelo: iPhone 13
Preço: R$ 1.700
Lucro estimado: R$ 300+

Link:
https://www.olx.com.br/

"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": mensagem
})
