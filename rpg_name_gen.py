import sys, random, string
from pprint import pprint
import config
import create_names

def gen_name(race_name, similar_names=False):
    triple = create_names.gen_race_name(race_name, similar_names)
    if triple: # [race_name, male_name, female_name]
        return triple

def check_for_triples(string):
    single = None
    double = None
    triple = None
    replace = None
    for char in string:
        if single != char:
            single = char
            double = None
            continue
        elif not double:
            double = char
            continue
        elif double != char:
            single = char
            double = None
            continue
        else: # three letters in a row
            replace = string.replace(char*3, char*2)
            break
    if replace:
        string = check_for_triples(replace)
    return string

def format_name(name):
    if name in config.races:
        race_name = name
    else:
        race_name = None
    if name in race_names_with_spaces:
        name = config.race_name_spaces_dict.get(name)

    if not race_name:
        # check for triple letters:
        name = name.lower()
        name = check_for_triples(name)

    name = string.capwords(name)
    if race_name:
        if race_name in config.human_races:
            if race_name != "human":
                name = "Human (" + string.capwords(name) + ")"
    else:
        if "(" in name:
            name_split = name.split("(")
            if len(name_split) == 2:
                first, last = name_split
                name = "(".join([first, string.capwords(last)])
    shorts = ["a", "an", "the", "at", "by", "for", "in", "of", "on", "to", "up", "and", "as", "but", "or", "and" "nor"]
    shorts_with_spaces = [" " + x + " " for x in shorts]
    if any(word.title() in name for word in shorts_with_spaces):
        for space_word_space in shorts_with_spaces:
            if space_word_space.title() in name:
                name = name.replace(space_word_space.title(), space_word_space)
    name = " ".join(name.split())
    name = name.replace("' ", " ")
    if name.endswith("'"):
        name = name[:-1]
    if not name.startswith("The "): # Taverns
        for substring in config.surname_affixes:
            if name.split(" ")[-1].startswith(substring) != -1: # Last names only
                split_var = substring
                split_name = name.split(split_var)
                if len(split_name) == 2:
                    first_half = split_name[0]
                    last_half = split_name[1]
                    name = split_var.join([first_half, string.capwords(last_half)])
    return name

def return_name_list(race_name=None, similar_names=False):
    if not race_name:
        names = [name for name in sorted(config.race_vars.keys())]
    else:
        names = [race_name]

    formatted_name_list = []
    for name in names:
        name_list = gen_name(name, similar_names)
        if not name_list:
            continue
        race_name, male_name, female_name = name_list
        formatted_race_name = format_name(race_name)
        male_name = format_name(male_name)
        female_name = format_name(female_name)
        formatted_name_list.append([[formatted_race_name, race_name], male_name, female_name])
    formatted_name_list = sorted(formatted_name_list)
    if not formatted_name_list:
        return

    name_list_to_return = []
    for name_list in formatted_name_list:
        race_name_tuple, male_name, female_name = name_list
        formatted_race_name, race_name = race_name_tuple
        gendered = race_name not in config.non_gendered_races
        randomness = random.choice([True, False])
        these_names = []
        if gendered:
            if randomness:
                these_names = [[formatted_race_name, race_name], ["Male", male_name], ["Female", female_name]]
            else:
                these_names = [[formatted_race_name, race_name], ["Female", female_name], ["Male", male_name]]
        else:
            if randomness:
                these_names = [[formatted_race_name, race_name], [male_name]]
            else:
                these_names = [[formatted_race_name, race_name], [female_name]]
        name_list_to_return.append(these_names)
    return name_list_to_return


race_names_with_spaces = config.race_name_spaces_dict.keys()












