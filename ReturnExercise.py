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


def add_consignment(consignment):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # add the customer to the table
    cursor.execute("INSERT INTO vans VALUES (?,?,?,?,?)", consignment)

    # commit our command
    connection.commit()
    # close our connection
    connection.close()


# READ
def get_all_drivers_from_branch(branch_):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # get all the drivers that work on a specific branch
    cursor.execute("""
    SELECT first_name, last_name 
    FROM drivers 
    WHERE branch = %(branch_)s""", {"branch_": branch_})

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret


def get_driver_details_by_id(driver_id):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # get all driver driver details by driver id
    cursor.execute("""
       SELECT first_name, last_name, phone_number, email_address, branch 
       FROM drivers 
       WHERE driver_id = %(driver_id)s 
       AND active = 'Y' """, {"driver_id": driver_id})

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret


def get_drivers_details_by_first_name(driver_name):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # get all driver driver details by driver id
    cursor.execute("""
       SELECT first_name, last_name, phone_number, email_address, branch 
       FROM drivers 
       WHERE first_name = %(driver_name)s 
       AND active = 'Y' """, {"driver_name": driver_name})

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret


def get_customers_details_by_geo(geo_area_):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # get all driver driver details by driver id
    cursor.execute("""
       SELECT first_name, last_name, phone_number, email_address, address, geo_area 
       FROM customers 
       WHERE geo_area = %(geo_area_)s
       AND active = 'Y' """, {"geo_area_": geo_area_})

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret


def get_customers_details_by_address(address_):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # get all driver driver details by driver id
    cursor.execute("""
         SELECT first_name, last_name, phone_number, email_address, address, geo_area 
         FROM customers 
         WHERE address = %(address_)s 
         AND active = 'Y' """, {"address_": address_})

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret


def get_customer_details_by_id(customer_id_):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # get all driver driver details by driver id
    cursor.execute("""
           SELECT first_name, last_name, phone_number, email_address, address, geo_area 
           FROM customers 
           WHERE customer_id_ = %(customer_id_)s 
           AND active = 'Y' """, {"customer_id_": customer_id_})

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret


def get_all_drivers_who_drove_a_specific_van(van_id):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    cursor.execute("""
      SELECT first_name, last_name
      FROM drivers
      WHERE driver_ID  IN (SELECT driver_ID 
      FROM vans 
      WHERE %(van_id))s = %(van_id)s""", {"van_id": van_id})

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret


def get_all_vans_id_belonging_to_particular_geo_area(geo_area_):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    cursor.execute("""
      SELECT van_ID
      FROM vans
      WHERE geo_area = %(geo_area_)s""", {"geo_area_": geo_area_})

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret


def get_all_vans_id_belonging_to_specific_branch(branch_):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # get all the drivers that work on a specific branch
    cursor.execute("""
      SELECT van_ID
      FROM vans
      WHERE branch = %(branch_)s""", {"branch_": branch_})

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret


def get_drivers_who_drove_in_specific_geo_area(geo_area_):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    cursor.execute("""
        SELECT first_name, last_name
        FROM drivers
        WHERE driver_ID  IN (SELECT driver_ID 
        FROM vans 
        WHERE %(geo_area))s = %(geo_area_)s""", {"geo_area_": geo_area_})

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret




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
            AND active = 'Y'""", {'item': item, 'id_key': id_key})

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
            AND active = 'Y'""", {'item': item, 'id_key': id_key})

        elif item_to_update == 'email_address':
            cursor.execute("""
            UPDATE drivers 
            SET email_address = %(item)s 
            WHERE driver_ID = %(id_key)s
            AND active = 'Y'""", {'item': item, 'id_key': id_key})

        elif item_to_update == 'branch':
            cursor.execute("""
            UPDATE drivers 
            SET branch = %(item)s 
            WHERE driver_ID = %(id_key)s
            AND active = 'Y'""", {'item': item, 'id_key': id_key})

    # commit our command
    connection.commit()
    # close our connection
    connection.close()


def update_consignment_return(date, barcode_):
    # connect to database
    connection = sqlite3.connect('returns.db')
    # create a cursor
    cursor = connection.cursor()

    cursor.execute("""
                UPDATE consignments 
                SET date_of_return = %(date)s, returned = 'Y' 
                WHERE barcode = %(barcode_)s 
                AND active = 'Y'""", {'date': date, 'barcode_': barcode_})
    # commit our command
    connection.commit()
    # close our connection
    connection.close()


# DELETE
def delete_customer_from_db(customer_to_remove):
    # connect to database
    connection = sqlite3.connect('returns.db')
    # create a cursor
    cursor = connection.cursor()

    # mark customer as no active
    cursor.execute("""
               UPDATE customers 
               SET active = 'N'
               WHERE customer_id = %(customer_to_remove)s
               AND active = 'Y'""", {'customer_to_remove': customer_to_remove})
    # commit our command
    connection.commit()
    # close our connection
    connection.close()


def delete_driver_from_db(driver_to_delete):
    # connect to database
    connection = sqlite3.connect('returns.db')
    # create a cursor
    cursor = connection.cursor()

    # mark driver as no active
    cursor.execute("""
                 UPDATE drivers 
                 SET active = 'N'
                 WHERE driver_ID = %(driver_to_delete)s
                 AND active = 'Y'""", {'driver_to_delete': driver_to_delete})
    # commit our command
    connection.commit()
    # close our connection
    connection.close()


def delete_van_from_db(van_to_delete):
    # connect to database
    connection = sqlite3.connect('returns.db')
    # create a cursor
    cursor = connection.cursor()

    # mark van as no active
    cursor.execute("""
                 UPDATE drivers 
                 SET active = 'N'
                 WHERE van_ID = %(van_to_delete)s
                 AND active = 'Y'""", {'driver_to_delete': van_to_delete})
    # commit our command
    connection.commit()
    # close our connection
    connection.close()


def delete_consignment_from_db(consignment_to_delete):
    # connect to database
    connection = sqlite3.connect('returns.db')
    # create a cursor
    cursor = connection.cursor()

    # mark consignment as no active
    cursor.execute("""
                   UPDATE consignments 
                   SET active = 'N'
                   WHERE van_ID = %(consignment_to_delete)s
                   AND active != 'N'""", {'consignment_to_delete': consignment_to_delete})
    # commit our command
    connection.commit()
    # close our connection
    connection.close()

