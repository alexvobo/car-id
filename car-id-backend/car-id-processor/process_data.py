import json
import requests

# ! returns keys in list of dictionaries


def all_keys(list_of_dicts):
    return set().union(*(d.keys() for d in list_of_dicts))
# ! returns index of the requested model


def search(list_of_dicts, make, model):
    return list_of_dicts[make][next((i for i, item in enumerate(list_of_dicts[make]) if item.get(model)), -1)]


with open("../car-id-scraper/cardib.json") as f:
    car_db = json.load(f)
    make = 'bmw'
    model = '4-series'
    models = all_keys(car_db[make])
    print(search(car_db, make, model))

#? The goal is to download all of the images, either as bytes or jpg/png and 