# -*- coding: utf-8 -*-
# MySQL Workbench Python script
# <description>
# Written in MySQL Workbench 8.0.38

import grt
#import mforms
def create_database():
    try:
        # Connect to the MySQL server (not specifying a database)
        connection = mysql.connector.connect(
            host='localhost',         # Update as needed
            user='root',              # Update with your MySQL username
            password='your_password'  # Update with your MySQL password
        )
        
        if connection.is_connected():
            print('Connected to MySQL server successfully.')

            cursor = connection.cursor()
            # SQL statement to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Commit the transaction (not strictly necessary for database creation, but good practice)
            connection.commit()

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()