import Dl
import cv2
import requests
from urllib.parse import urlencode
from pyzbar.pyzbar import decode
import os
import random
import qrcode


# data_type = 'json'
# endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
# params = {"address": "1600 Amphitheatre Parkway, Mountain View, CA", "key": apiKey}
# url_params = urlencode(params)
# sample = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY"


def get_api_key():
    with open('API_KEY.txt', 'r+') as api_key:
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
    return street_number.get("short_name"), \
           route.get("short_name"), \
           geo_area.get("short_name"), \
           state.get("short_name"), \
           zip_code.get("short_name")


def shortest_distance(origin, destination, data_type='json'):
    end_point = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    origin_params = {"address": origin, "key": get_api_key()}
    destination_params = {"address": destination, "key": get_api_key()}
    url_params_origin = urlencode(origin_params)
    url_params_destination = urlencode(destination_params)
    url_origin = f"{end_point}?{url_params_origin}"
    url_dest = f"{end_point}?{url_params_destination}"
    r_o = requests.get(url_origin)
    r_d = requests.get(url_dest)
    if r_o.status_code not in range(200, 299) or r_d not in range():
        return {}
    latlng_o = {}
    latlng_d = {}
    try:
        latlng_o = r_o.json()['results'][0]['geometry']['location']
        latlng_d = r_d.json()['results'][0]['geometry']['location']
    except:
        pass
    orig_coord = latlng_o.get("lat"), latlng_o.get("lng")
    dest_coord = latlng_d.get("lat"), latlng_d.get("lng")
    url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(
        str(orig_coord), str(dest_coord))
    result = requests.get(url)
    driving_time = result['rows'][0]['elements'][0]['duration']['value']
    return driving_time


# s = extract_address("5901 Myrtle Ave, Ridgewood, NY 11385")
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
        qr = qrcode.make(str(value))
        qr.save(str(value) + '.png', scale=10)
        return value

    if os.path.isfile('consignment_id.txt'):
        with open('consignment_id.txt', 'r+') as new_consigment_id:
            data = int(new_consigment_id.read())
            new_consigment_id.seek(0)
            new_consigment_id.truncate()
            new_consigment_id.write(str(data + 1))
            return create_qr_code(data)
    else:
        with open('consignment_id.txt', 'w') as new_consigment_id:
            new_consigment_id.write('1')
            return create_qr_code(1)


def read_barcode(file_name):
    barcode_to_read = cv2.imread(str(file_name) + '.png')
    for barcode in decode(barcode_to_read):
        my_data = barcode.data.decode('utf-8')
        return my_data


# CREATE
def add_new_customer(f_name, l_name, e_address, p_num, address):
    Dl.add_customer(
        int(customer_id_gen()),
        str(f_name),
        str(l_name),
        str(e_address),
        str(p_num),
        str(extract_address(address)),
        str(extract_geo_area(address)),
        'Y'
    )


def add_new_driver(f_name, l_name, p_number, e_address, branch):
    Dl.add_driver(
        int(driver_id_gen()),
        str(f_name),
        str(l_name),
        str(p_number),
        str(e_address),
        str(branch),
        'Y'
    )


def add_new_van(branch):
    Dl.add_van(
        van_id_gen(),
        get_driver_id_by_branch(branch),
        branch,
        branch,
        'Y'
    )


def add_new_consignment(customer_id):
    Dl.add_consignment(
        consignment_id_and_barcode_gen(),
        select_van_for_consignment(customer_id),
        customer_id,
        'EMPTY',
        'NO',
        'Y'
    )


def generate_consignments_van_location_to_csv_file():
    return Dl.get_consignments_van_location_to_csv_file()


def get_driver_id_by_branch(branch):
    drivers = Dl.get_all_drivers_ids_by_branch(branch)
    return drivers[random.randrange(0, len(drivers))]


def select_van_for_consignment(customer_id):
    customer_geo_area = Dl.get_customer_geo_area_by_id(customer_id)
    get_van = Dl.get_all_vans_id_belonging_to_particular_geo_area(customer_geo_area)
    return get_van[random.randrange(0, len(get_van))]


def check_if_consignment_returned(barcode_data):
    # if Dl.check_if_consignment_returned(read_barcode(barcode_data)) == 'Y':
    if Dl.check_if_consignment_returned(barcode_data) == 'Y':
        print("The consignment returned to the customer")
    else:
        print("The consignment are not yet returned to the customer")


def get_route_to_customer(origin, customer_id):
    dest = Dl.get_customer_address_by_id(customer_id)


def get_all_drivers_who_drove_a_specific_van(van_id):
    return Dl.get_all_drivers_who_drove_a_specific_van(van_id)



