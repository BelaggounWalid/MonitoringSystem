import requests
from bs4 import BeautifulSoup
import sqlite3

# Fetch the HTML content of the website
url = "http://www.cert.ssi.gouv.fr/"
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the latest CERT alert
latest_alert = soup.find("div", class_="item cert-alert open")

# Extract information about the latest CERT alert
date = latest_alert.find("span", class_="item-date").text.strip()
reference = latest_alert.find("span", class_="item-ref").text.strip()
title = latest_alert.find("span", class_="item-title").text.strip()
status = latest_alert.find("span", class_="item-status").text.strip()

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
                VALUES (?, ?, ?, ?)''', (date, reference, title, status))

# Commit changes and close connection
conn.commit()
conn.close()

