import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
import locale

# Set the locale to French
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

# Function to parse the French date format
def parse_french_date(date_str):
    return datetime.strptime(date_str, "%d %B %Y")

# Fetch the HTML content of the website
url = "http://www.cert.ssi.gouv.fr/"
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all CERT alert items
cert_alerts = soup.find_all("div", class_="item cert-alert open")

# Initialize variables to store information about the latest CERT alert
latest_date = None
latest_reference = None
latest_title = None
latest_status = None

# Iterate over all CERT alert items to find the latest one based on the date
for alert in cert_alerts:
    date_str = alert.find("span", class_="item-date").text.strip()
    date = parse_french_date(date_str)

    if latest_date is None or date > latest_date:
        latest_date = date
        latest_reference = alert.find("span", class_="item-ref").text.strip()
        latest_title = alert.find("span", class_="item-title").text.strip()
        latest_status = alert.find("span", class_="item-status").text.strip()

# Store the extracted information in the database
conn = sqlite3.connect('anisdatabase.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS cert_alert (
                date TEXT,
                reference TEXT,
                title TEXT,
                status TEXT
            )''')

# Insert the latest CERT alert into the table
cursor.execute('''INSERT INTO cert_alert (date, reference, title, status) 
                VALUES (?, ?, ?, ?)''', (latest_date.strftime("%Y-%m-%d"), latest_reference, latest_title, latest_status))

# Commit changes and close connection
conn.commit()
conn.close()

