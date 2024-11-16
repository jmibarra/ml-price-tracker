# email_service.py
import smtplib
from email.mime.text import MIMEText

class EmailService:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send_email(self, subject, body, recipient_email):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.email
        msg["To"] = recipient_email

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.sendmail(self.email, recipient_email, msg.as_string())
                print("Correo enviado exitosamente!")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
