from sys import path
from order_robots import *
from utils import *


download_link = 'https://robotsparebinindustries.com/orders.csv'
url = 'https://robotsparebinindustries.com/#/robot-order'

def minimal_task():
    path_to_save = init_output()
    input_file = download_orders_csv(download_link, path_to_save)
    input_list = read_input(input_file)
    open_browser(url)
    close_popup()
    for order in input_list:
        print(order)
        fill_form(order[0], int(order[1]), str(order[2]), order[3], order[4], path_to_save)
        close_popup()



    #print(input_list)
    print("Done.")


if __name__ == "__main__":
    minimal_task()
