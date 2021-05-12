from RPA.Browser.Selenium import Selenium
from RPA.Browser import Browser
from RPA.Robocloud import Items
import time, re, os, datetime

browser = Selenium()

def config_browser(path_to_save):
    browser.set_download_directory(path_to_save)

#open browser
def open_browser(url: str):
    browser.open_available_browser(url)
    time.sleep(2)

#close popup
def close_popup():
    try:
        yep_btn = browser.find_element('//*[@id="root"]/div/div[2]/div/div/div/div/div/button[1]')
        yep_btn.click()
    except:
        pass

#choose head
def choose_head(head_model):
    head_model_el = browser.find_element(f'//*[@id="head"]/option[{head_model}]')
    head_model_el.click()
    
#choose body
def choose_body(body_model):
    body_model_el = browser.find_element(f'//*[@id="id-body-{body_model}"]')
    body_model_el.click()

#choose_legs
def choose_legs(legs_model):
    #legs_model_text = extract_table(legs_model)
    legs_model_input = browser.driver.find_element_by_xpath("//input[@placeholder='Enter the part number for the legs']")
    browser.input_text(legs_model_input, legs_model)

#set address
def set_shipping_address(shipping_address):
    browser.input_text('//*[@id="address"]', shipping_address)

#show table
def show_table():
    show_table_btn = browser.find_element('//*[text() = "Show model info"]')
    show_table_btn.click()

#extract table
def extract_table(legs_model):
    show_table()
    table_el = browser.find_element(f'//*[@id="model-info"]/tbody/tr[{legs_model}]')
    legs_model_text = (table_el.text)[:-1]
    return legs_model