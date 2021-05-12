import requests
import csv
import time, re, os, datetime

#init path to save and check if it not exists->create
def init_output():
    path_to_save = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output')
    if not os.path.exists(path_to_save):
        os.makedirs(path_to_save)
    return path_to_save

#download input csv file
def download_orders_csv(download_link, path_to_download):
    try:
        input_file_path = f'{path_to_download}/orders.csv'
        req = requests.get(download_link)
        content = req.content
        csv_file = open(input_file_path, 'wb')
        csv_file.write(content)
        csv_file.close()
        return input_file_path
    except Exception as e:
        return f'Unexpected error occured when trying to download input file. Exception: {e}'

#read input
def read_input(path_to_file):
    with open(path_to_file, newline='') as f:
        reader = csv.reader(f)
        input_data = list(reader)
    return(input_data)