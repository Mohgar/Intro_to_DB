import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        # Connect to the MySQL server (not specifying a database)
        connection = mysql.connector.connect(
            host='localhost',  # Update as needed
            user='root',  # Update with your MySQL username
            password='Mamado$m3s7007' # Update with your MySQL password
            database = "alx_book_store"
        )

        if connection.is_connected():
            print('Connected to MySQL server successfully.')

            cursor = connection.cursor()
            # SQL statement to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Commit the transaction (not strictly necessary for database creation, but good practice)
            connection.commit()

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


if __name__ == "__main__":
    create_database()
