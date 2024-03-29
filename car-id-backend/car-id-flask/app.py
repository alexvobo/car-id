from flask import Flask, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def search(list_of_dicts, make, model):
    # ! returns keys in list of dictionaries
    return list_of_dicts[make][next((i for i, item in enumerate(list_of_dicts[make]) if item.get(model)), -1)]


def find_years(yearString):
    # Parses year string with the format "2010 - 2019" and returns list of all the years i.e. 2010, 2011, ... 2019
    start, end = yearString.split("-")
    return [str(year) for year in range(int(start), int(end)+1)]


def all_keys(list_of_dicts):
    return set().union(*(d.keys() for d in list_of_dicts))


def filter_text(items, models=False):

    filt_items = []
    for item in items:
        word_list = item.split("-")
        if models:
            # Filtering Models
            if len(word_list) > 1:
                filt_items.append(
                    " ".join(subword.title()
                             for subword in word_list))
            else:
                if len(word_list[0]) <= 3:
                    filt_items.append(" ".join(subword.upper()
                                               for subword in word_list))
                else:
                    filt_items.append(" ".join(subword.title()
                                               for subword in word_list))

        else:
            # Fitlering Makes (default)
            filt_items.append(" ".join(subword.title()
                                       for subword in word_list))

    return filt_items


# This is our main file
with open("cardb.json", "r") as f:
    db = json.load(f)


@ app.route('/', methods=['GET'])
# * Get list of makes
def get_makes():
    if db:
        return jsonify(sorted(filter_text(list(db.keys()))))


@ app.route('/<make>', methods=['GET'])
# * Get list of models for the make
def get_model_list(make):
    if db:
        return jsonify(sorted(filter_text(list(all_keys(db[make])), models=True)))


@ app.route('/<make>/all', methods=['GET'])
# * Get entire list of models with their images
def get_models(make):
    if db:
        return jsonify(db[make])


@ app.route('/<make>/<model>', methods=['GET'])
# * Get specific make/model list
def get_make_model(make, model):
    if db:
        return jsonify(search(db, make, model))


@ app.route('/<make>/<model>/years', methods=['GET'])
# * Get specific make/model list
def get_make_model_years(make, model):
    if db:
        data = search(db, make, model)[model]
        years = []
        for d in data:
            years.append(d['year'])
        return jsonify(years)


@ app.route('/<make>/<model>/<year>', methods=['GET'])
# * Get specific make/model/year list, if year is found returns that specific generation otherwise returns the entire list of generations
def get_make_model_year(make, model, year):
    #! Need to make this work for ex. 2003-2015 give all models up to the end date
    if db:
        data = search(db, make, model)
        for d in data[model]:
            print("here" + make)
            formatted_year = "-".join([x.strip()
                                       for x in d['year'].split('-')])
            print(formatted_year)
            if year == formatted_year:
                return(jsonify(({model: d})))
            elif "-" not in year:
                print("here2" + make)
                year_range = find_years(d['year'])
                if year.strip() in year_range:
                    return(jsonify(({model: d})))
        return(jsonify(data))


if __name__ == '__main__':
    app.run(debug=True)
