from datetime import datetime
import sqlite3
import pytz

# Define the timezone for Europe/Paris
paris_timezone = pytz.timezone('Europe/Paris')

# Establish connection to the database
connecte = sqlite3.connect('anisdatabase.db')
connected = connecte.cursor()

# Get the current time in the timezone of Europe/Paris
dateNow = datetime.now(paris_timezone)

# Retrieve all information from the database
connected.execute('SELECT * FROM dataBase')
tab = connected.fetchall()

# Retrieve the threshold data
connected.execute('SELECT * FROM Seuil')
seuil_data = connected.fetchone()  # Assuming you only have one row in the 'Seuil' table, adjust if necessary

# Loop through the retrieved data
for info in tab:
    # Retrieve the saved date from the database
    dateOfSave = datetime.strptime(info[4], '%Y-%m-%d %H:%M:%S')
    # Make the saved date timezone-aware
    dateOfSave = paris_timezone.localize(dateOfSave)
    # Calculate the time difference
    time_difference = dateNow - dateOfSave

    # Check if the time interval is reached for proceeding with the deletion of information
    if time_difference.total_seconds() / 60 >= seuil_data[3]:
        # Proceed with the deletion of information
        requette = 'DELETE FROM dataBase WHERE date = ?'
        connected.execute(requette, (info[4],))

# Commit changes to the database
connecte.commit()
# Close the database connection
connecte.close()

