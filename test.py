# import mysql.connector
#
# # Establish connection to MySQL
# conn = mysql.connector.connect(
#     host="localhost",  # or the IP address of your Docker container if it's not running on localhost
#     user="root",
#     password="root",
#     database="inventory_management"
# )
#
# # Check if the connection is successful
# if conn.is_connected():
#     print("Connected to MySQL!")
#
# # Perform database operations here...
#
# # Remember to close the connection when you're done
# conn.close()


def connect_mysql_db():
    from mysql.connector import connect, Error

    try:
        co = connect(host="localhost",
                user="root",
                password="root",
                database="inventory_management")
        if co.is_connected():
            return co
        # with connect(
        #         host="localhost",
        #         user="root",
        #         password="root",
        #         database="inventory_management",
        # ) as connection:
        #     print('connection')
        #     if connection.is_connected():
        #         print('connected')
        #         return connection.cursor()
    except Error as e:
        print(e)



