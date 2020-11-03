import json
import time
import downloader
import os


SAVE_PATH = "D:/Machine Learning/cardata"


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
        start = time.perf_counter()
        # loop through makes
        time.sleep(0.5)
        models = all_keys(car_db[make])
        for model in models:
            # loop through models for each make
            try:
                generations = search(car_db, make, model)[model]
                # loop through all the years of each model0
                for gen in generations:
                    images = gen['images']
                    year = gen['year']
                    # Let's create the directories if they don't exist
                    gen_name = "-".join(g.strip() for g in year.split("-"))
                    folder_name = make+"_"+model+"_"+gen_name
                    folder_dir = os.path.join(SAVE_PATH, folder_name)
                    if not os.path.exists(folder_dir):
                        # create directories if they dont exist
                        os.makedirs(folder_dir)

                    if len(os.listdir(folder_dir)) == 0:
                        downloader.batch_download(
                            folder_name, images, folder_dir)
                        time.sleep(0.5)
                        #print(folder_name + " EXISTS ALREADY!")
                    else:
                        print("already visisted {}, {}, {} ".format(
                            make, model, year))
            except Exception:
                print("catastrophic error {}, {}".format(make, model))
        end = time.perf_counter()
        print(f"{make} done in {end - start:0.4f} seconds")

# ? The goal is to download all of the images, either as bytes or jpg/png and
