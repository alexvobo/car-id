from copy import Error
from json.decoder import JSONDecodeError
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import base64
import requests
import json

import codecs
import os
import time


def getSoup(url):
    driver = webdriver.Firefox()
    driver.get(url)

    # save_path = os.getcwd()
    # file_name = 'index.html'
    # complete_name = os.path.join(save_path, file_name)

    # file_object = codecs.open(complete_name, "w", "utf-8")
    # html = driver.page_source

    # file_object.write(html)
    driver.close()


def readSoup():
    file_object = codecs.open("index.html", "r", "utf-8")
    return BeautifulSoup(file_object.read(), "html.parser")


def get_as_base64(url):

    return base64.b64encode(requests.get(url).content).decode("utf-8")


def clickMake(make):

    pass


def parse_style_attribute(style_string):
    if 'background-image' in style_string:
        style_string = style_string.split(' url("')[1].replace('");', '')
        return style_string
    return None


def all_keys(list_of_dicts):
    return set().union(*(d.keys() for d in list_of_dicts))

# getSoup(url)
# soup = readSoup()


url = "https://www.autoevolution.com/cars/"

driver = webdriver.Firefox()
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")

listMakes = soup.select("div[itemtype='https://schema.org/Brand']")
list_make_urls = []
for i in listMakes:
    hrf = i.find("a").get("href")
    list_make_urls.append(hrf)
# car_database = {}
# driver.find_element_by_css_selector("button.sc-bwzfXH:nth-child(2)").click()

""" Try to load json we already have. If it's not there, create file """
car_database = {}
with open("cardib.json", "a+") as f:
    f.seek(0)
    car_database = json.load(f)


""" For each make, find the models and find all the generations for every model and get the images"""
for count, make in enumerate(list_make_urls):
    make_name = make[make[:len(make)-1].rfind("/")+1:len(make)-1]

    # & TESTING PUPOSES ONLY!!
    # """ If we have logged the model, skip """
    # existing_makes = car_database.keys()

    # if make_name in existing_makes:
    #     print('exists {}'.format(make_name))
    #     continue
    # & TESTING PUPOSES ONLY!!
    driver.get(make)

    model_soup = BeautifulSoup(driver.page_source, "html.parser")
    # find each make url
    listModels = model_soup.select("div.carmod")
    list_model_urls = []
    for i in listModels:
        hrf = i.find("a").get("href")
        list_model_urls.append(hrf)
    # We have all the models for each brand. Prepare to append dictionaries of models to list

    if not car_database.get(make_name):
        print('{} does not exist in db'.format(make_name))
        car_database[make_name] = []

    for model in list_model_urls:

        driver.get(model)
        model_details = {}
        model_name = model[model[:len(
            model)-1].rfind("/")+1:len(model)-1]
        print("Looking at  {}".format(model_name))

        """ If we have logged the model, skip """
        # * WE NEED TO MOVE THIS INTO GEN FOR LOOP
        existing_models = all_keys(car_database[make_name])
        if model_name in existing_models:
            print('exists {}'.format(model_name))
            time.sleep(2)
            continue
        # * SO THAT WE CAN CHECK TO SEE IF THE YEAR
        # * IS IN OUR JSON ALREADY

        model_details[model_name] = []
        sub_model_soup = BeautifulSoup(
            driver.page_source, "html.parser")

        # & go through the models and locate each generation
        submodels = sub_model_soup.select("div.container.carmodel")

        if not submodels:
            print("No submodels found for {}".format(model_name))
            continue

        # & Go through each generation
        for gen in submodels:
            gen_details = {}
            year = gen.select_one(
                'p:nth-child(1) > a:nth-child(1)').string

            gen_details["year"] = year
            print("{}, {}, {}".format(make_name, model_name, year))
            # & click into details -> pics then append to db
            details_url = gen.select_one("a:nth-child(4)").get("href")
            driver.get(details_url)
            time.sleep(1)
            # & click on img so we can load the gallery
            driver.execute_script("$('#aegal_0').click();")
            time.sleep(1)
            sub_model_gallery = BeautifulSoup(
                driver.page_source, "html.parser")

            images = sub_model_gallery.select(
                "div.vslide > a")
            if not images:
                print("No images found for {} {}".format(model_name, year))
                continue
            gen_details['images'] = []

            for img in images:
                # *model_details['images'].append(get_as_base64(img.get("href")))
                gen_details['images'].append(img.get("href"))

            # & Append a model generation to the model list
            model_details[model_name].append(gen_details)

            time.sleep(5)

        # & Append model + all generations to the make
        car_database[make_name].append(model_details)
        with open("cardib.json", "r+") as f:
            json.dump(car_database, f, indent=4)

    time.sleep(5)
driver.close()
