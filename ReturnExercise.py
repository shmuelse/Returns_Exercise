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
cursor.execute("""CREATE TABLE vans (
    barcode TEXT PRIMARY KEY,
    driver_ID INTEGER,
    date_of_return TEXT,
    active TEXT
)
""")



