# -*- coding: utf-8 -*-
import sqlite3
import pygal
from pygal.style import Style

# Connect to the database
connection = sqlite3.connect('/home/anis/Secondstep/anisdatabase.db')
cursor = connection.cursor()

# Retrieve all information from the database table
cursor.execute('SELECT * FROM dataBase')
data = cursor.fetchall()

# Initialize lists
dates = []
cpu_usage = []
memory_usage = []
ram_usage = []

# Extract data from each row and append to respective lists
for row in data:
    dates.append(row[4])
    cpu_usage.append(row[1])
    memory_usage.append(row[2] )  # Convert memory to gigabytes
    ram_usage.append(row[3]/1024)

# Close database connection
connection.close()

# Create a line chart
line_chart = pygal.Line(x_label_rotation=20)
line_chart.title = 'System Usage Over Time'
line_chart.x_labels = dates
line_chart.add('CPU Usage (%)', cpu_usage)
line_chart.add('Memory Usage (MB)', memory_usage)
line_chart.add('RAM Usage (MB)', ram_usage)

# Render the chart to SVG file
line_chart.render_to_file('line_chart.svg')

