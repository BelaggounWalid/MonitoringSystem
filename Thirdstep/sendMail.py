import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def load_email_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Define sender email and receiver emails
sender_email = "anis-walid-ramdan.belaggoun@alumni.univ-avignon.fr"
receiver_emails = ["aniswalidbelaggoun@gmail.com", "anisphysiquebac21@gmail.com"]

# SMTP configuration
smtp_ssl_host = 'smtpz.univ-avignon.fr'
smtp_ssl_port = 465  # SSL port (e.g., 465 for Gmail)
smtp_username = "anis-walid-ramdan.belaggoun@alumni.univ-avignon.fr"
smtp_password = "645222Anis2003#@"

# Load email template from file
email_template_file = "/home/anis/Thirdstep/template.html"
email_template = load_email_template(email_template_file)

# Replace placeholders in the template with actual values
username_in_template = "Anis"  # Replace this with the real username
email_content = email_template.replace("{username}", username_in_template)

# Create message object instance
msg = MIMEMultipart('alternative')
msg['From'] = sender_email
msg['To'] = ', '.join(receiver_emails)
msg['Subject'] = "System Crisis Alert"

# Attach HTML content to the message
msg.attach(MIMEText(email_content, 'html'))

# Connect to SMTP server and send the email
with smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port) as server:
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_emails, msg.as_string())

