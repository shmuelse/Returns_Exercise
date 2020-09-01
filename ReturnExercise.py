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



cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
available_table = (cursor.fetchall())
print(available_table)


# commit our command
connection.commit()
# close our connection
connection.close()

# CREATE
def add_customer(customer):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # add the customer to the table
    cursor.execute("INSERT INTO customers VALUES (?,?,?,?,?,?,?,?)", customer)

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

def add_driver(driver):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # add the customer to the table
    cursor.execute("INSERT INTO drivers VALUES (?,?,?,?,?,?,?)", driver)

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

def add_van(van):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # add the customer to the table
    cursor.execute("INSERT INTO vans VALUES (?,?,?,?,?,?,?)", van)

    # commit our command
    connection.commit()
    # close our connection
    connection.close()



# UPDATE
def update_customer_details(item_to_update,item, id_key):

    # connect to database
    connection = sqlite3.connect('returns.db')
    # create a cursor
    cursor = connection.cursor()

    # Record update
    if item_to_update == 'phone_num':
        cursor.execute("""UPDATE customers SET phone_number = %item WHERE customer_id = %id_key""" % (item, id_key))
    elif item_to_update == 'email_address':
        cursor.execute("""UPDATE customers SET email_address = %item WHERE customer_id = %id_key""" % (item, id_key))
    elif item_to_update == 'address':
        cursor.execute("""UPDATE customers SET address = %item WHERE customer_id = %id_key""" % (item, id_key))
    elif item_to_update == 'geo_area':
        cursor.execute("""UPDATE customers SET geo_area = %item WHERE customer_id = %id_key""" % (item, id_key))

    # commit our command
    connection.commit()
    # close our connection
    connection.close()









