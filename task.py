from order_robots import *
from utils import *


download_link = 'https://robotsparebinindustries.com/orders.csv'
url = 'https://robotsparebinindustries.com/#/robot-order'

def minimal_task():
    open_browser(url)
    close_popup()
    # choose_head(2)
    # choose_body(4)
    #set_shipping_address('test shipping addr')
    #extract_table(2)
    choose_legs(6)

    # path_to_save = init_output()
    # input_file = download_orders_csv(download_link, path_to_save)
    # input_list = read_input(input_file)
    #print(input_list)
    print("Done.")


if __name__ == "__main__":
    minimal_task()
