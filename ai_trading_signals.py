import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Credenziali Libero
LIBERO_EMAIL = "sminoliti@libero.it"
LIBERO_PASSWORD = "Sonounobeso1!"  # ← Inserisci qui la tua vera password

# Email destinatario
TO = "stefanominoliti@gmail.com"

def invia_segnale(subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = LIBERO_EMAIL
    msg["To"] = TO

    with smtplib.SMTP_SSL("smtp.libero.it", 465) as server:
        server.login(LIBERO_EMAIL, LIBERO_PASSWORD)
        server.sendmail(LIBERO_EMAIL, TO, msg.as_string())

# Esempio di segnale da inviare
segnale = f"""Segnale AI - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
✅ EUR/USD: SHORT @ 1.1320
🎯 Take Profit: 1.1250
⛔ Stop Loss: 1.1350"""

invia_segnale("🔔 Nuovo Segnale AI Trading", segnale)
print("Email inviata con successo.")
