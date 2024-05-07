import mysql.connector
from faker import Faker
import random
import datetime

from test import connect_mysql_db


# Function to generate fake data
def generate_fake_employee():
    fake = Faker()
    name = fake.name()
    email = fake.email()
    gender = random.choice(['Male', 'Female'])
    contact = fake.phone_number()
    dob = fake.date_of_birth().strftime('%Y-%m-%d')
    doj = fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S')
    password = fake.password(length=8)
    utype = random.choice(['Admin', 'Employee'])
    address = fake.address()
    salary = round(random.uniform(20000, 80000), 2)
    return name, email, gender, contact, dob, doj, password, utype, address, salary


# Connect to MySQL database
conn = connect_mysql_db()
cursor = conn.cursor()
try:




        # Insert 50 rows of data

    for _ in range(50):
        employee_data = generate_fake_employee()
        cursor.execute("""
                INSERT INTO employee(name, email, gender, contact, dob, doj, pass, utype, address, salary)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, employee_data)

    conn.commit()
    print("Inserted 50 rows of data into the employee table!")

except mysql.connector.Error as e:
    print("Error:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection closed.")
