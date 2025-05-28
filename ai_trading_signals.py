import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Email di destinazione
TO = "stefanominoliti@gmail.com"

# Email di invio (tuo account Gmail)
GMAIL_USER = "stefanominoliti@gmail.com"
GMAIL_PASSWORD = "la-tua-password-app-gmail-qui"  # ← incolla qui la password a 16 cifre

def invia_segnale(subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = GMAIL_USER
    msg["To"] = TO

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, TO, msg.as_string())

# Esempio di segnale
segnale = f"""Segnale AI - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
✅ EUR/USD: SHORT @ 1.1320
🎯 Take Profit: 1.1250
⛔ Stop Loss: 1.1350"""

invia_segnale("🔔 Nuovo Segnale AI Trading", segnale)
print("Segnale inviato con successo.")
