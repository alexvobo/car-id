import json
import time
import downloader
import os
# ! returns keys in list of dictionaries


def all_keys(list_of_dicts):
    return set().union(*(d.keys() for d in list_of_dicts))
# ! returns index of the requested model


def search(list_of_dicts, make, model):
    return list_of_dicts[make][next((i for i, item in enumerate(list_of_dicts[make]) if item.get(model)), -1)]


with open("../car-id-scraper/cardib.json") as f:
    car_db = json.load(f)

    makes = car_db.keys()
    for make in makes:
        # loop through makes
        models = all_keys(car_db[make])
        for model in models:
            # loop through models for each make
            try:
                generations = search(car_db, make, model)[model]
                save_directory_base = "D:/Machine Learning/car-id/"+make+"/"+model + "/"
                # loop through all the years of each model0
                for gen in generations:
                    images = gen['images']
                    year = gen['year']
                    save_directory = save_directory_base + year
                    if not os.path.exists(save_directory):
                        # create directories if they dont exist
                        os.makedirs(save_directory)

                    if len(os.listdir(save_directory)) == 0:
                        file_prefix = "{}-{}-{}".format(make, model, year)
                        downloader.batch_download(
                            file_prefix, images, save_directory)
                        time.sleep(1)
                        #print(save_directory + " EXISTS ALREADY!")
                    else:
                        print("skipping {}, {}, {}".format(make, model, year))
            except Exception:
                print("skipping {}, {}".format(make, model))

# ? The goal is to download all of the images, either as bytes or jpg/png and
