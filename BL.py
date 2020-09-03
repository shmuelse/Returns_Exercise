import ReturnExercise
import cv2
import numpy as np
from pyzbar.pyzbar import decode

customers_ids = 0
drivers_ids = 0


def read_barcode(file_name):
    barcode_to_read = cv2.imread(file_name)
    for barcode in decode(barcode_to_read):
        my_data = barcode.data.decode('utf-8')
        return my_data


def add_new_customer(f_name, l_name, e_address, p_num, address, geo_area):
    global customers_ids
    customer_id = customers_ids
    customers_ids = customers_ids+1
    new_customer = [(customer_id, f_name, l_name, e_address, p_num, address, geo_area)]
    ReturnExercise.add_customer(new_customer)


def add_new_driver(f_name, l_name, p_number, e_address, branch):
    global drivers_ids
    driver_id = drivers_ids
    drivers_ids = drivers_ids + 1
    new_driver = [(driver_id, f_name, l_name, p_number, e_address, branch)]
    ReturnExercise.add_driver(new_driver)



