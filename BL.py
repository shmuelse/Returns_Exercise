import ReturnExercise
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import pyqrcode


def customer_id_gen():
    customer_id_gen.count += 1
    return customer_id_gen.count


def driver_id_gen():
    driver_id_gen.count += 1
    return driver_id_gen.count


def van_id_gen():
    van_id_gen.count += 1
    return van_id_gen.count


def consignment_id_and_barcode_gen():
    consignment_id_and_barcode_gen.count += 1
    qr = pyqrcode.create(consignment_id_and_barcode_gen.count)
    qr.png(str(consignment_id_and_barcode_gen.count) + '.png', scale=10)
    return consignment_id_and_barcode_gen.count


customer_id_gen.count = 0
driver_id_gen.count = 0
van_id_gen.count = 0
consignment_id_and_barcode_gen.count = 0


def read_barcode(file_name):
    barcode_to_read = cv2.imread(str(file_name)+'.png')
    for barcode in decode(barcode_to_read):
        my_data = barcode.data.decode('utf-8')
        return my_data


def add_new_customer(f_name, l_name, e_address, p_num, address, geo_area):
    ReturnExercise.add_customer([(customer_id_gen(), f_name, l_name, e_address, p_num, address, geo_area, 'Y')])


def add_new_driver(f_name, l_name, p_number, e_address, branch):
    ReturnExercise.add_driver([(driver_id_gen(), f_name, l_name, p_number, e_address, branch, 'Y')])


def add_new_van(driver_id ,geo_area, branch):
    ReturnExercise.add_van([(van_id_gen(), driver_id, geo_area, branch, 'Y')])


def add_new_consignment(driver_id, geo_area, branch):
    ReturnExercise.add_consignment([(consignment_id_and_barcode_gen(), driver_id, geo_area, branch, 'Y')])







