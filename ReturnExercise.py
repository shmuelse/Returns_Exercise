import sqlite3


# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode
#
# img = cv2.imread('frame.png')
# for barcode in decode(img):
#     my_data = barcode.data.decode('utf-8')
#     print(my_data)


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


def add_consignments(consignments):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # add the customer to the table
    cursor.execute("INSERT INTO vans VALUES (?,?,?,?)", consignments)

    # commit our command
    connection.commit()
    # close our connection
    connection.close()


# UPDATE
def update_user_details(item_to_update, item, id_key, user_type):
    # connect to database
    connection = sqlite3.connect('returns.db')
    # create a cursor
    cursor = connection.cursor()

    # Record update
    if user_type == 'customer':

        if item_to_update == 'phone_num':
            cursor.execute("""
            UPDATE customers 
            SET phone_number = %(item)s 
            WHERE customer_id = %(id_key)s 
            AND active = 'Y'""", {'item': item, 'id_key': id_key} )

        elif item_to_update == 'email_address':
            cursor.execute("""
            UPDATE customers 
            SET email_address =%(item)s 
            WHERE customer_id = %(id_key)s 
            AND active = 'Y'""", {'item': item, 'id_key': id_key})

        elif item_to_update == 'address':
            cursor.execute("""
            UPDATE customers 
            SET address = %(item)s 
            WHERE customer_id = %(id_key)s
            AND active = 'Y'""", {'item': item, 'id_key': id_key})

        elif item_to_update == 'geo_area':
            cursor.execute("""
            UPDATE customers 
            SET geo_area = %(item)s 
            WHERE customer_id = %(id_key)s
            AND active = 'Y'""", {'item': item, 'id_key': id_key})

    elif user_type == 'driver':

        if item_to_update == 'phone_num':
            cursor.execute("""
            UPDATE drivers 
            SET phone_number = %(item)s 
            WHERE driver_ID = %(id_key)s
            AND active = 'Y'""", {'item': item, 'id_key':  id_key})

        elif item_to_update == 'email_address':
            cursor.execute("""
            UPDATE drivers 
            SET email_address = %(item)s 
            WHERE driver_ID = %(id_key)s
            AND active = 'Y'""", {'item': item, 'id_key':  id_key})

        elif item_to_update == 'branch':
            cursor.execute("""
            UPDATE drivers 
            SET branch = %(item)s 
            WHERE driver_ID = %(id_key)s
            AND active = 'Y'""", {'item': item, 'id_key':  id_key})

    # commit our command
    connection.commit()
    # close our connection
    connection.close()


def delete_customer_from_db(customer_to_remove):
    # connect to database
    connection = sqlite3.connect('returns.db')
    # create a cursor
    cursor = connection.cursor()
    cursor.execute("""
               UPDATE customers 
               SET active = 'N'
               WHERE customer_id = %(customer_to_remove)s
               AND active = 'Y'""", {'customer_to_remove': customer_to_remove})
    # commit our command
    connection.commit()
    # close our connection
    connection.close()
