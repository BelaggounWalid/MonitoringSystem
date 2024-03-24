import sqlite3
import os 

backup_dir ="/home/anis/Secondstep"
def backup_database():
    # Create a connection to the main database
    main_conn = sqlite3.connect('anisdatabase.db')

    # Create a connection to the backup database
    backup_conn = sqlite3.connect(os.path.join(backup_dir, 'database_backup.db'))

    # Use the backup API to copy the main database to the backup database
    main_conn.backup(backup_conn)

    # Close connections
    main_conn.close()
    backup_conn.close()


backup_database()
