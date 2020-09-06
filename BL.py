import Dl
import cv2
import pyqrcode
import requests
from urllib.parse import urlencode
from pyzbar.pyzbar import decode
import os


# data_type = 'json'
# endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
# params = {"address": "1600 Amphitheatre Parkway, Mountain View, CA", "key": apiKey}
# url_params = urlencode(params)
# sample = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY"


def get_api_key():
    with open('customer_id.txt', 'r+') as api_key:
        return str(api_key.read())


def extract_geo_area(address_or_geo_area, data_type='json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_geo_area, "key": get_api_key()}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}
    geo_area = {}
    try:
        geo_area = r.json()['results'][0]['address_components'][3]
    except:
        pass
    return geo_area.get("long_name")


def extract_address(address_or_geo_area, data_type='json'):
    end_point = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_geo_area, "key": get_api_key()}
    url_params = urlencode(params)
    url = f"{end_point}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}
    street_number = {}
    route = {}
    geo_area = {}
    state = {}
    zip_code = {}
    try:
        street_number = r.json()['results'][0]['address_components'][0]
        route = r.json()['results'][0]['address_components'][1]
        geo_area = r.json()['results'][0]['address_components'][3]
        state = r.json()['results'][0]['address_components'][5]
        zip_code = r.json()['results'][0]['address_components'][7]
    except:
        pass
    return street_number.get("short_name"), route.get("short_name"), geo_area.get("short_name"), state.get(
        "short_name"), zip_code.get("short_name")


# s = extract_address("520 maple street brooklyn ny")
# print(' '.join([str(elem) for elem in s]))


def customer_id_gen():
    if os.path.isfile('customer_id.txt'):
        with open('customer_id.txt', 'r+') as new_customer_id:
            data = int(new_customer_id.read())
            new_customer_id.seek(0)
            new_customer_id.truncate()
            new_customer_id.write(str(data + 1))
            return data
    else:
        with open('customer_id.txt', 'w') as new_customer_id:
            new_customer_id.write('1')
        return 1


def driver_id_gen():
    if os.path.isfile('driver_id.txt'):
        with open('driver_id.txt', 'r+') as new_driver_id:
            data = int(new_driver_id.read())
            new_driver_id.seek(0)
            new_driver_id.truncate()
            new_driver_id.write(str(data + 1))
            return data
    else:
        with open('driver_id.txt', 'w') as new_driver_id:
            new_driver_id.write('1')
        return 1


def van_id_gen():
    if os.path.isfile('van_id.txt'):
        with open('van_id.txt', 'r+') as new_van_id:
            data = int(new_van_id.read())
            new_van_id.seek(0)
            new_van_id.truncate()
            new_van_id.write(str(data + 1))
            return data
    else:
        with open('van_id.txt', 'w') as new_van_id:
            new_van_id.write('1')
        return 1


def consignment_id_and_barcode_gen():
    def create_qr_code(value):
        qr = pyqrcode.create(value)
        qr.png(str(value) + '.png', scale=10)
        return value

    if os.path.isfile('consignment_id.txt'):
        with open('consignment_id.txt', 'r+') as new_consigment_id:
            data = int(new_consigment_id.read())
            new_consigment_id.seek(0)
            new_consigment_id.truncate()
            new_consigment_id.write(str(data + 1))
            create_qr_code(data)
    else:
        with open('consignment_id.txt', 'w') as new_consigment_id:
            new_consigment_id.write('1')
            create_qr_code(1)


def read_barcode(file_name):
    barcode_to_read = cv2.imread(str(file_name) + '.png')
    for barcode in decode(barcode_to_read):
        my_data = barcode.data.decode('utf-8')
        return my_data


def add_new_customer(f_name, l_name, e_address, p_num, address, geo_area):
    Dl.add_customer([(customer_id_gen(), f_name, l_name, e_address, p_num, address, geo_area, 'Y')])


def add_new_driver(f_name, l_name, p_number, e_address, branch):
    Dl.add_driver([driver_id_gen(), f_name, l_name, p_number, e_address, branch, 'Y'])


def add_new_van(driver_id, geo_area, branch):
    Dl.add_van([(van_id_gen(), driver_id, geo_area, branch, 'Y')])


def add_new_consignment(van_id, geo_area, branch):
    Dl.add_consignment([(consignment_id_and_barcode_gen(), van_id, geo_area, branch, 'Y')])


add_new_driver('john', 'gross', '2026567700', "john@ldtglobal.com", 'Brooklyn')
