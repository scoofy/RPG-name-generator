import sys, random
from pprint import pprint
import config

race_vars = config.race_vars
filename_template = config.filename_template
non_gendered_races = config.non_gendered_races


races = sorted(race_vars.keys())
race_names_with_spaces = sorted(config.race_name_spaces_dict.keys())


def decision(probability):
    return random.random() < probability

def name_files_to_dict(app, race, filename_vars):
    name_dict = {}
    for filename_var in filename_vars:
        file_text = app.open_resource(filename_template.format(race, filename_var), "r").read()
        name_list = file_text.split("\n")
        name_dict[filename_var] = name_list
    return name_dict


def add_syllable(name_probablitity_tuple, name_dict):
    return_name = decision(name_probablitity_tuple[1])
    if return_name:
        name_list = name_dict.get(name_probablitity_tuple[0])
        name = random.choice(name_list)
        return name
    else:
        return ""

def gen_name(app, race_name, similar_names=False):

    race_tuple_list = race_vars.get(race_name)

    filename_vars = [x[0] for x in race_tuple_list]
    filenames = [filename_template.format(race_name, x) for x in filename_vars]

    name_dict = name_files_to_dict(app, race_name, filename_vars)


    male_name = ""
    female_name = ""
    add_space = True
    second_space = False
    second_last_name = False
    leading_orc_L2_space = False
    trailing_orc_L2_space = False
    parentheses = False
    gendered = True
    if race_name in non_gendered_races:
        gendered = False
    if race_name in ["tavern"]:
        male_name += "the "
        female_name += "the "
    if race_name in ["elf", "gnome", "tavern"]:
        second_space = True
        second_last_name = True
        if race_name in ["elf"]:
            parentheses = True
    if race_name in ["orc"]:
        leading_orc_L2_space = True
        trailing_orc_L2_space = False
    for tuple_var in race_tuple_list:
        tuple_name = tuple_var[0]
        tuple_probability = tuple_var[1]

        if add_space:
            if tuple_name.startswith("L"):
                male_name += " "
                female_name += " "
                add_space = False
                if parentheses:
                    male_name += "("
                    female_name += "("

        if second_space:
            if race_name in ["elf"]:
                if tuple_name.startswith("T"):
                    male_name += ") "
                    female_name += ") "
                    second_space = False
            if race_name in ["gnome", "tavern"]:
                if tuple_name == "L1":
                    if second_last_name == True:
                        second_last_name = False
                    else:
                        male_name += " "
                        female_name += " "

        if leading_orc_L2_space and tuple_name == "L2":
            male_name += " "
            female_name += " "
            leading_orc_L2_space = False
            trailing_orc_L2_space = True
        if trailing_orc_L2_space and tuple_name == "L3":
            male_name += " "
            female_name += " "
            trailing_orc_L2_space = False


        ###
        if tuple_name and not tuple_name[-1].isdigit():
            if tuple_name[-1] == "M":
                male_name += add_syllable(tuple_var, name_dict)
            elif tuple_name[-1] == "F":
                female_name += add_syllable(tuple_var, name_dict)
        else:
            if similar_names: # gen similar names
                syllable = add_syllable(tuple_var, name_dict)
                male_name += syllable
                female_name += syllable


            else: # or different names
                male_name += add_syllable(tuple_var, name_dict)
                female_name += add_syllable(tuple_var, name_dict)

    return [race_name, male_name, female_name]

def format_name(name):
    if name in race_names_with_spaces:
        name = config.race_name_spaces_dict.get(name)
    name = name.title()
    name = name.replace("  ", " ")
    name = name.replace("'S", "'s")
    for substring in ["Mc", "Mac"]:
        if name.find(substring) != -1:
            split_var = substring
            split_name = name.split(split_var)
            if len(split_name) == 2:
                first_half = split_name[0]
                last_half = split_name[1]
                name = split_var.join([first_half, last_half.title()])
    return name


def return_name_list(app, race_name = None):
    if not race_name:
        names = [name for name in sorted(race_vars.keys())]
    else:
        names = [race_name]
    name_list_to_return = []
    for name in names:
        race_name, male_name, female_name = gen_name(app, name)
        gendered = race_name not in non_gendered_races
        race_name = format_name(race_name)
        male_name = format_name(male_name)
        female_name = format_name(female_name)
        randomness = random.choice([True, False])
        these_names = []
        if gendered:
            if randomness:
                these_names = [[race_name], ["Male", male_name], ["Female", female_name]]
            else:
                these_names = [[race_name], ["Female", female_name], ["Male", male_name]]
        else:
            if randomness:
                these_names = [[race_name], [male_name]]
            else:
                these_names = [[race_name], [female_name]]
        name_list_to_return.append(these_names)
    return name_list_to_return

















