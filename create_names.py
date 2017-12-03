import string, random
from pprint import pprint
import config
import utilities as utils

def decision(probability):
    return random.random() < probability

def add_syllable(name_probability_tuple, predetermined = False):
    if not predetermined:
        return_name = decision(name_probability_tuple[1])
    else:
        return_name = predetermined
    if return_name:
        name_list = config.file_text_dict.get(name_probability_tuple[0])
        if name_list:
            name = random.choice(name_list)
            return name
        else:
            return ""
    else:
        return ""

def race_tuple_contents(race_tuple_var):
    tuple_name = race_tuple_var[0]
    tuple_probability = race_tuple_var[1]
    return tuple_name, tuple_probability

def standard_gendered(race_name, similar_names = False):
    male_name = ""
    female_name = ""
    first_char = None
    race_tuple_list = utils.return_race_tuple_list(race_name)
    for tuple_var in race_tuple_list:
        tuple_name, tuple_probability = race_tuple_contents(tuple_var)
        file_name_dict_var = race_name + tuple_name
        name_probability_tuple = [file_name_dict_var, tuple_probability]
        if first_char != tuple_name[0]:
            first_char = tuple_name[0]
            male_name += " "
            female_name += " "
        if tuple_name and not tuple_name[-1].isdigit():
            if tuple_name[-1] == "M":
                male_name += add_syllable(name_probability_tuple)
            elif tuple_name[-1] == "F":
                female_name += add_syllable(name_probability_tuple)
        else:
            if similar_names: # gen similar names
                syllable = add_syllable(name_probability_tuple)
                male_name += syllable
                female_name += syllable
            else: # or different names
                male_name += add_syllable(name_probability_tuple)
                female_name += add_syllable(name_probability_tuple)
    return [race_name, male_name, female_name]

def standard_nongendered(race_name, similar_names = False):
    name = ""
    first_char = None
    race_tuple_list = utils.return_race_tuple_list(race_name)
    for tuple_var in race_tuple_list:
        tuple_name, tuple_probability = race_tuple_contents(tuple_var)
        file_name_dict_var = race_name + tuple_name
        name_probability_tuple = [file_name_dict_var, tuple_probability]
        if first_char != tuple_name[0]:
            first_char = tuple_name[0]
            name += " "
        name += add_syllable(name_probability_tuple)
    return [race_name, name, name]

def standard_single_name(race_name, similar_names = False):
    name = ""
    first_char = None
    race_tuple_list = utils.return_race_tuple_list(race_name)
    for tuple_var in race_tuple_list:
        tuple_name, tuple_probability = race_tuple_contents(tuple_var)
        file_name_dict_var = race_name + tuple_name
        name_probability_tuple = [file_name_dict_var, tuple_probability]
        name += add_syllable(name_probability_tuple)
    return [race_name, name, name]

def tiefling(race_name, similar_names = False):
    race_name, male_name, female_name = standard_gendered(race_name, similar_names)
    return_list = [race_name]

    human_races = config.human_races
    human_surnames = []
    for i in range(2):
        human_race_for_tiefling_surname = random.choice(human_races)
        ignore, random_human_name, ignore = human(human_race_for_tiefling_surname)
        random_human_surname = random_human_name.strip().split(" ")[-1]
        human_surnames.append(random_human_surname)

    for i in range(2):
        name = [male_name, female_name][i]
        name_list = name.strip().split(" ")
        standard = name_list[0]
        virtue = name_list[1]
        first = random.choice([standard, virtue])
        surname = human_surnames[i]
        full = first + " " + surname
        return_list.append(full)
    return return_list

def dwarf(race_name, similar_names = False):
    return standard_gendered(race_name, similar_names)

def human(race_name, similar_names = False):
    return standard_gendered(race_name, similar_names)

def gnome(race_name, similar_names = False):
    race_name, male_first, female_first = standard_gendered(race_name, similar_names)
    race_name, male_second, female_second = standard_gendered(race_name, similar_names)
    male_last = male_second.split(" ")[-1]
    male_full = male_first + " " + male_last
    female_last = female_second.split(" ")[-1]
    female_full = female_first + " " + female_last
    return [race_name, male_full, female_full]

def goblin(race_name, similar_names = False):
    return standard_nongendered(race_name, similar_names)

def orc(race_name, similar_names = False):
    leading_orc_L2_space = True
    trailing_orc_L2_space = False
    name = ""
    first_char = None
    race_tuple_list = utils.return_race_tuple_list(race_name)
    for tuple_var in race_tuple_list:
        tuple_name, tuple_probability = race_tuple_contents(tuple_var)
        file_name_dict_var = race_name + tuple_name
        name_probability_tuple = [file_name_dict_var, tuple_probability]
        add_next_syllable = decision(tuple_probability)
        if first_char != tuple_name[0]:
            first_char = tuple_name[0]
            name += " "
        if leading_orc_L2_space and tuple_name == "L2":
            if add_next_syllable:
                name += " "
                leading_orc_L2_space = False
                trailing_orc_L2_space = True
        if trailing_orc_L2_space and tuple_name == "L3":
            name += " "
            trailing_orc_L2_space = False
        name += add_syllable(name_probability_tuple, predetermined=add_next_syllable)
    return [race_name, name, name]


def hillgiant(race_name, similar_names = False):
    return standard_single_name(race_name, similar_names)

def halfling(race_name, similar_names = False):
    return (standard_gendered(race_name, similar_names))

def tavern(race_name, similar_names = False):
    race_name, name, ignore = standard_single_name(race_name, similar_names)
    name = "the"
    first_char = None
    race_tuple_list = utils.return_race_tuple_list(race_name)
    for tuple_var in race_tuple_list:
        tuple_name, tuple_probability = race_tuple_contents(tuple_var)
        file_name_dict_var = race_name + tuple_name
        name_probability_tuple = [file_name_dict_var, tuple_probability]
        name += " "
        name += add_syllable(name_probability_tuple)
    return [race_name, name, name]

def elf(race_name, similar_names = False):
    male_name = ""
    female_name = ""
    first_char = None
    race_tuple_list = utils.return_race_tuple_list(race_name)
    for tuple_var in race_tuple_list:
        tuple_name, tuple_probability = race_tuple_contents(tuple_var)
        file_name_dict_var = race_name + tuple_name
        name_probability_tuple = [file_name_dict_var, tuple_probability]
        if first_char != tuple_name[0]:
            first_char = tuple_name[0]
            if first_char == "T":
                male_name += ")"
                female_name += ")"
            male_name += " "
            female_name += " "
            if first_char == "L":
                male_name += "("
                female_name += "("
        if tuple_name and not tuple_name[-1].isdigit():
            if tuple_name[-1] == "M":
                male_name += add_syllable(name_probability_tuple)
            elif tuple_name[-1] == "F":
                female_name += add_syllable(name_probability_tuple)
        else:
            if similar_names: # gen similar names
                syllable = add_syllable(name_probability_tuple)
                male_name += syllable
                female_name += syllable
            else: # or different names
                male_name += add_syllable(name_probability_tuple)
                female_name += add_syllable(name_probability_tuple)
    return [race_name, male_name, female_name]



race_functions = {
    "tavern": tavern,
    "elf": elf,
    "halfling": halfling,
    "hillgiant": hillgiant,
    "orc": orc,
    "goblin": goblin,
    "gnome": gnome,
    "human": human,
    "illuskan": human,
    "chondathan": human,
    "tethyrian": human,
    "damaran": human,
    "turami": human,
    "dwarf": dwarf,
    "tiefling": tiefling,
}

def gen_race_name(race_name, similar_names = False):
    triple = None
    race_name_function = race_functions.get(race_name)
    if race_name_function:
        triple = race_functions.get(race_name)(race_name, similar_names)
    if triple: #[race_name, male_name, female_name]
        return triple





















