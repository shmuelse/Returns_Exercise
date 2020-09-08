import sqlite3
import pandas as pd
import os


# CREATE
def add_customer(customer_id, f_name, l_name, e_address, p_num, address, g_area, active):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # add the customer to the table
    param_to_insert = """INSERT INTO customers 
    (customer_id , first_name, last_name, email_address, phone_number, address, geo_area, active)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""

    data_tuple = (customer_id, f_name, l_name, e_address, p_num, address, g_area, active)
    cursor.execute(param_to_insert, data_tuple)
    # commit our command
    connection.commit()
    # close our connection
    connection.close()


def add_driver(driver_id, f_name, l_name, p_num, e_address, branch, active):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # add the customer to the table
    param_to_insert = """INSERT INTO drivers
                   (driver_ID, first_name, last_name, phone_number, email_address, branch, active) 
                   VALUES (?, ?, ?, ?, ?, ?, ?);"""

    data_tuple = (driver_id, f_name, l_name, p_num, e_address, branch, active)
    cursor.execute(param_to_insert, data_tuple)

    # commit our command
    connection.commit()
    # close our connection
    connection.close()


def add_van(v_id, d_id, g_area, branch, active):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # add the customer to the table
    param_to_insert = """
    INSERT INTO vans 
    (van_ID, driver_ID, geo_area, branch, active)
     VALUES (?, ?, ?, ?, ?);"""

    data_tuple = (v_id, d_id[0], g_area, branch, active)
    cursor.execute(param_to_insert, data_tuple)

    # commit our command
    connection.commit()
    # close our connection
    connection.close()


def add_consignment(barcode, van_id, customer_id, ret_date, is_ret, active):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # add the customer to the table
    param_to_insert = """INSERT INTO consignments
    (barcode, van_ID, customer_id, date_of_return, returned, active)
    VALUES (?, ?, ?, ?, ?, ?);"""

    data_tuple = (barcode, van_id[0], customer_id, ret_date, is_ret, active)
    cursor.execute(param_to_insert, data_tuple)

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
    select_query = """SELECT * FROM drivers where branch = ?"""
    cursor.execute(select_query, (branch_,))
    records = cursor.fetchall()
    to_ret = None
    for row in records:
        to_ret += ("first name = ", row[1])
        to_ret += ("last name = ", row[2])
        to_ret += ("phone number = ", row[3])
    cursor.close()

    # close our connection
    connection.close()
    return to_ret


def get_all_drivers_ids_by_branch(branch):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    select_query = """SELECT driver_ID FROM drivers where branch = ?"""
    cursor.execute(select_query, (branch,))
    all_ids = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return all_ids


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

    # close our connection
    connection.close()

    return to_ret


def get_customer_geo_area_by_id(customer_id_):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    param = """
           SELECT geo_area 
           FROM customers 
           WHERE customer_id = ? 
           AND active = 'Y' """

    cursor.execute(param, [customer_id_])
    to_ret = cursor.fetchone()
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

    param_to_select = """
      SELECT van_ID
      FROM vans
      WHERE geo_area = ?"""

    cursor.execute(param_to_select, geo_area_)

    rows = cursor.fetchall()
    # commit our command
    connection.commit()
    # close our connection
    connection.close()
    return rows


def get_all_vans_id_belonging_to_specific_branch(branch_):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    # get all the drivers that work on a specific branch
    cursor.execute("""
      SELECT van_ID
      FROM vans
      WHERE branch = %(branch_)s 
      AND active = 'Y'""", {"branch_": branch_})

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
        WHERE active = 'Y' 
        AND driver_ID  IN (SELECT driver_ID 
        FROM vans 
        WHERE %(geo_area))s = %(geo_area_)s""", {"geo_area_": geo_area_})

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret


def get_all_returned_consignments_id_in_date_range(date_start, date_end):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    cursor.execute("""
          SELECT barcode
          FROM consignments
          WHERE date_of_return >= %(date_start)s 
          AND date_of_return <= %(date_end)s
          AND returned = 'Y'
          AND active = 'Y'""", {'date_start': date_start, 'date_end': date_end})

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret


def get_all_returned_consignments_id_that_returned_to_specific_customer(customer_id_):
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    cursor.execute("""
             SELECT barcode
             FROM Consignments
             WHERE customer_id = %(customer_id_)s 
             AND returned = 'Y'
             AND active = 'Y'""", {'customer_id_': customer_id_})

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret


def get_the_consignments_id_that_are_not_already_returned():
    # connect to database
    connection = sqlite3.connect('returns.db')

    # create a cursor
    cursor = connection.cursor()

    cursor.execute("""
               SELECT barcode
               FROM consignments
               WHERE returned = 'Y' 
               AND active = 'Y'""", )

    to_ret = cursor.fetchall()

    # commit our command
    connection.commit()
    # close our connection
    connection.close()

    return to_ret


def get_consignments_van_location_to_csv_file():
    if os.path.isfile('csv_file_num.txt'):
        with open('csv_file_num.txt', 'r+') as new_csv_file:
            data = int(new_csv_file.read())
            new_csv_file.seek(0)
            new_csv_file.truncate()
            new_csv_file.write(str(data + 1))
    else:
        with open('new_csv_file.txt', 'w') as new_csv_file:
            new_csv_file.write('1')
            data = 1

    connect = sqlite3.connect('returns.db')
    sql = """SELECT barcode, van_ID  FROM consignments;"""
    df = pd.read_sql_query(sql, connect)
    df.to_csv('Consignment_data_' + str(data) + '.csv')


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


def update_consignment_returned(date, barcode_):
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


def update_van_geo_area(van_id, new_geo):
    # connect to database
    connection = sqlite3.connect('returns.db')
    # create a cursor
    cursor = connection.cursor()

    cursor.execute("""
                   UPDATE vans 
                   SET geo_area = %(new_geo)s 
                   WHERE van_ID = %(van_id)s 
                   AND active = 'Y'""", {'new_geo': new_geo, 'van_id': van_id})
    # commit our command
    connection.commit()
    # close our connection
    connection.close()


def update_van_branch(van_id, new_branch):
    # connect to database
    connection = sqlite3.connect('returns.db')
    # create a cursor
    cursor = connection.cursor()

    cursor.execute("""
                    UPDATE vans 
                    SET geo_area = %(new_branch)s 
                    WHERE van_ID = %(van_id)s 
                    AND active = 'Y'""", {'new_branch': new_branch, 'van_id': van_id})
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



