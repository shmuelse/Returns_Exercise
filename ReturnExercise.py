import sqlite3

# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode
#
# img = cv2.imread('frame.png')
# for barcode in decode(img):
#     my_data = barcode.data.decode('utf-8')
#     print(my_data)


# connect to database
connection = sqlite3.connect('returns.db')

# create a cursor
cursor = connection.cursor()

# create Customers table
cursor.execute("""CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email_address TEXT,
    phone_number TEXT,
    address TEXT,
    geo_area TEXT,
    active TEXT
)
""")

# create Drivers table
cursor.execute("""CREATE TABLE drivers (
    driver_ID INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    phone_number TEXT,
    email_address TEXT,
    branch TEXT,
    active TEXT
)
""")

# create Consignments table
cursor.execute("""CREATE TABLE Consignments (
    barcode TEXT PRIMARY KEY,
    driver_ID INTEGER,
    customer_id INTEGER,
    date_of_return TEXT,
    returned TEXT,
    active TEXT,
    FOREIGN KEY (driver_ID) REFERENCES drivers(driver_ID),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

# create Vans table
cursor.execute("""CREATE TABLE vans (
    van_ID INTEGER PRIMARY KEY,
    driver_ID INTEGER,
    geo_area TEXT,
    branch TEXT,
    active TEXT,
    FOREIGN KEY (driver_ID) REFERENCES drivers(driver_ID)
)
""")


# commit our command
connection.commit()
# close our connection
connection.close()
