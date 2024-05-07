from faker import Faker
import random
from utils import get_db_conn


def generate_fake_admin():
    fake = Faker()
    name = fake.name()
    email = fake.email()
    gender = random.choice(['Male', 'Female'])
    contact = fake.phone_number()
    dob = fake.date_of_birth().strftime('%Y-%m-%d')
    doj = fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S')
    password = fake.password(length=8)
    utype = random.choice(['Admin'])
    address = fake.address()
    salary = round(random.uniform(20000, 80000), 2)
    return name, email, gender, contact, dob, doj, password, utype, address, salary

def create_admin():
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        # name = input("Enter name: ").capitalize()
        # email = input("Enter email: ").capitalize()
        # gender = input("Enter gender: ").capitalize()
        # contact = input("Enter contact: ")
        # # dob = input("Enter date of birth (in format dd-mm-yyyy): ")
        # # doj = input("Enter date of joining (in format dd-mm-yyyy): ")
        # password = input("Enter password: ")
        # user_type = "Admin"
        #
        # cur.execute(
        #     "INSERT INTO employee(name,email,gender,contact,pass,utype) "
        #     "VALUES (?, ?, ?, ?, ?, ?)",
        #     (name, email, gender, contact, password, user_type)
        # )
        admin_data = generate_fake_admin()
        cur.execute(
            "Insert into employee(name,email,gender,contact,dob,doj,pass,utype,address,salary) "
            "values(?,?,?,?,?,?,?,?,?,?)", admin_data)
        conn.commit()

        print("admin user created")
        # Get the last inserted row id
        user_id = cur.lastrowid
        print(user_id)
        # Fetch the inserted password
        cur.execute("SELECT pass, email FROM employee WHERE eid = ?", (user_id,))
        # print(cur.fetchone())
        data = cur.fetchone()
        inserted_password = data[0]
        user_email = data[1]

        print("User ID:", user_id)
        print("Email:", user_email)
        print("Inserted Password:", inserted_password)
        cur.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    create_admin()
