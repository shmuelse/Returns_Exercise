import Dl
import cv2
import pyqrcode
import requests
from urllib.parse import urlencode
from pyzbar.pyzbar import decode

apiKey = "Insert_Your_API_here"

# data_type = 'json'
# endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
# params = {"address": "1600 Amphitheatre Parkway, Mountain View, CA", "key": apiKey}
# url_params = urlencode(params)
# sample = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY"


def extract_geo_area(address_or_geo_area, data_type='json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_geo_area, "key": apiKey}
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
    params = {"address": address_or_geo_area, "key": apiKey}
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
    return street_number.get("short_name"), route.get("short_name"), geo_area.get("short_name"), state.get("short_name"), zip_code.get("short_name")


# s = extract_address("520 maple street brooklyn ny")
# print(' '.join([str(elem) for elem in s]))


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
    Dl.add_customer([(customer_id_gen(), f_name, l_name, e_address, p_num, address, geo_area, 'Y')])


def add_new_driver(f_name, l_name, p_number, e_address, branch):
    Dl.add_driver([(driver_id_gen(), f_name, l_name, p_number, e_address, branch, 'Y')])


def add_new_van(driver_id, geo_area, branch):
    Dl.add_van([(van_id_gen(), driver_id, geo_area, branch, 'Y')])


def add_new_consignment(van_id, geo_area, branch):
    Dl.add_consignment([(consignment_id_and_barcode_gen(), van_id, geo_area, branch, 'Y')])


add_new_driver('john', 'gross', '2026567700', "john@ldtglobal.com", 'Brooklyn')








