from flask import Flask, request, render_template
import dnd_name_gen, config
import random
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def index():
    name_list = dnd_name_gen.return_name_list(app)
    return render_template("frontpage.html", name_list=name_list)

@app.route("/<race_name>")
def race(race_name):
    random_race = race_name == "random"
    if race_name.lower() not in config.races:
        if random_race:
            race_name = random.choice(config.races)
        elif race_name in [x.replace(" ","") for x in config.formatted_race_name_dict_reverse.keys()]:
            for key, value in config.formatted_race_name_dict_reverse.items():
                if race_name == key.replace(" ",""):
                    race_name = value
                    break
    race_name = race_name.lower()
    name_list = dnd_name_gen.return_name_list(app, race_name=race_name)
    if not name_list:
        return render_template("errorpage.html", race_name=race_name)
    list_of_name_lists =[]
    list_of_name_lists.append(name_list[0])
    for i in range(4):
        name_list = dnd_name_gen.return_name_list(app, race_name=race_name)
        list_of_name_lists.append(name_list[0])
    formatted_race_name = [name_list[0] for name_list in list_of_name_lists][0][0]

    primary_list_of_names = None
    secondary_list_of_names = None

    if race_name in config.non_gendered_races:
        primary_list_of_names = [None, [list_item[1][0] for list_item in list_of_name_lists]]
        secondary_list_of_names = None
    else:
        list_without_race_name = [list_item[1:] for list_item in list_of_name_lists]
        male_names = []
        female_names = []
        for sub_list in list_without_race_name:
            for list_item in sub_list:
                if list_item[0] in ["Male"]:
                    male_names.append(list_item[1])
                elif list_item[0] in ["Female"]:
                    female_names.append(list_item[1])
        primary_list_of_names = []
        secondary_list_of_names = []

        first = random.choice(["males first", "females first"])
        if first == "males first":
            primary_list_of_names = ["Male names:", male_names]
            secondary_list_of_names = ["Female names:", female_names]
        elif first == "females first":
            primary_list_of_names = ["Female names:", female_names]
            secondary_list_of_names = ["Male names:", male_names]

    name_list = [[formatted_race_name, race_name], primary_list_of_names, secondary_list_of_names]
    return render_template("namepage.html", name_list=name_list, random_race=random_race)





























if __name__ == "__main__":
    app.run(debug=True)

