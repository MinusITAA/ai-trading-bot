from data_fetcher import get_price
from model import predict_trade
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import time

EMAIL = "sminoliti@libero.it"
PASSWORD = "LA_TUA_PASSWORD_LIBERO"
TO = "stefanominoliti@gmail.com"

def send_email(subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = TO
    with smtplib.SMTP_SSL("smtp.libero.it", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, TO, msg.as_string())

def analyze_and_send():
    assets = {
        "EUR/USD": "EUR/USD",
        "XAU/USD": "XAU/USD",
        "BTC/USD": "BTC/USD"
    }

    for name, symbol in assets.items():
        price = get_price(symbol.replace("/", ""))
        if price:
            prediction, prob = predict_trade([price])
            if prediction == 1 and prob > 0.7:
    signal = (
    "Segnale AI - " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\\n"
    + f"{name}: LONG @ {price}\\n"
    + f"Take Profit: {round(price * 1.01, 4)}\\n"
    + f"Stop Loss: {round(price * 0.995, 4)}\\n"
    + f"Probabilità stimata: {round(prob * 100, 2)}%"
)
                send_email(f"AI Trading Signal: {name}", signal)
                print(signal)

# Esegui ogni 15 minuti
while True:
    analyze_and_send()
    time.sleep(900)
