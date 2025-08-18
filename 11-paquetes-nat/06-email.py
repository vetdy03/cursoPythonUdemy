from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

mensaje = MIMEMultipart()
mensaje['From'] = "vetdy03@gmail.com"
mensaje['To'] = "cocaever0@gmail.com"
mensaje['Subject'] = "Mi primer email y mi primer mensaje"

cuerpo = MIMEText("Cuerpo del mensaje", "plain")
mensaje.attach(cuerpo)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("vetdy03@gmail.com", "kpwnjsxcpvfyaotx")  # tu contraseña de aplicación
    smtp.sendmail(mensaje['From'], mensaje['To'], mensaje.as_string())
    print("Mensaje enviado exitosamente.")
