from RPA.Browser.Selenium import Selenium
from RPA.Browser import Browser
import time, re, os, datetime

browser = Selenium()
#init path to save and check if it not exists->create
path_to_save = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output')
if not os.path.exists(path_to_save):
    os.makedirs(path_to_save)

browser.set_download_directory(path_to_save)
