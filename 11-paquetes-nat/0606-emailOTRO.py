import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor SMTP (ejemplo para Gmail)
servidor_smtp = "smtp.gmail.com"
puerto = 587  # Para conexión TLS
usuario = "vetdy03@gmail.com"
contraseña = "kpwnjsxcpvfyaotx"  # En 2025, probablemente necesites una contraseña de aplicación

# Crear el mensaje
mensaje = MIMEMultipart()
mensaje["From"] = usuario
mensaje["To"] = "cocaever0@gmail.com"
mensaje["Subject"] = "Prueba de correo desde Python - Agosto 2025"

cuerpo = """
Hola,

Este es un correo de prueba enviado desde Python en agosto de 2025.

Saludos,
Python
"""
mensaje.attach(MIMEText(cuerpo, "plain"))

# Enviar el correo
try:
    with smtplib.SMTP(servidor_smtp, puerto) as servidor:
        servidor.starttls()  # Encriptación TLS
        servidor.login(usuario, contraseña)
        servidor.sendmail(usuario, mensaje["To"], mensaje.as_string())
    print("Correo enviado exitosamente!")
except Exception as e:
    print(f"Error al enviar el correo: {e}")