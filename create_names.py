import config
import string, random

def decision(probability):
    return random.random() < probability

def name_files_to_dict(app, race, filename_vars):
    name_dict = {}
    for filename_var in filename_vars:
        file_text = app.open_resource(config.filename_template.format(race, filename_var), "r").read()
        name_list = file_text.split("\n")
        name_dict[filename_var] = name_list
    return name_dict

def add_syllable(name_probablitity_tuple, name_dict, predetermined = False):
    if not predetermined:
        return_name = decision(name_probablitity_tuple[1])
    else:
        return_name = predetermined
    if return_name:
        name_list = name_dict.get(name_probablitity_tuple[0])
        name = random.choice(name_list)
        return name
    else:
        return ""
'''
if race_name in ["elf", "gnome", "tavern"]:
    second_space = True
    second_last_name = True

if race_name in ["orc"]:
    leading_orc_L2_space = True
    trailing_orc_L2_space = False

for tuple_var in race_tuple_list:
    tuple_name = tuple_var[0]
    tuple_probability = tuple_var[1]

    if second_space:
        if race_name in ["gnome"]:
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
'''

def race_tuple_contents(race_tuple_var):
    tuple_name = race_tuple_var[0]
    tuple_probability = race_tuple_var[1]
    return tuple_name, tuple_probability

def standard_gendered(race_name, race_tuple_list, name_dict, similar_names = False):
    male_name = ""
    female_name = ""
    first_char = None
    for tuple_var in race_tuple_list:
        tuple_name, tuple_probability = race_tuple_contents(tuple_var)
        if first_char != tuple_name[0]:
            first_char = tuple_name[0]
            male_name += " "
            female_name += " "
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

def standard_nongendered(race_name, race_tuple_list, name_dict, similar_names = False):
    name = ""
    first_char = None
    for tuple_var in race_tuple_list:
        tuple_name, tuple_probability = race_tuple_contents(tuple_var)
        if first_char != tuple_name[0]:
            first_char = tuple_name[0]
            name += " "
        name += add_syllable(tuple_var, name_dict)
    return [race_name, name, name]

def standard_single_name(race_name, race_tuple_list, name_dict, similar_names = False):
    name = ""
    first_char = None
    for tuple_var in race_tuple_list:
        tuple_name, tuple_probability = race_tuple_contents(tuple_var)
        name += add_syllable(tuple_var, name_dict)
    return [race_name, name, name]

def tiefling(race_name, race_tuple_list, name_dict, similar_names = False):
    race_name, male_name, female_name = standard_gendered(race_name, race_tuple_list, name_dict, similar_names)
    return_list = [race_name]
    for name in [male_name, female_name]:
        name_list = name.strip().split(" ")
        standard = name_list[0]
        virtue = name_list[1]
        full = standard + " (" + virtue + ")"
        return_list.append(full)
    return return_list

def dwarf(race_name, race_tuple_list, name_dict, similar_names = False):
    return standard_gendered(race_name, race_tuple_list, name_dict, similar_names)

def human(race_name, race_tuple_list, name_dict, similar_names = False):
    return standard_gendered(race_name, race_tuple_list, name_dict, similar_names)

def gnome(race_name, race_tuple_list, name_dict, similar_names = False):
    race_name, male_first, female_first = standard_gendered(race_name, race_tuple_list, name_dict, similar_names)
    race_name, male_second, female_second = standard_gendered(race_name, race_tuple_list, name_dict, similar_names)
    male_last = male_second.split(" ")[-1]
    male_full = male_first + " " + male_last
    female_last = female_second.split(" ")[-1]
    female_full = female_first + " " + female_last
    return [race_name, male_full, female_full]

def goblin(race_name, race_tuple_list, name_dict, similar_names = False):
    return standard_nongendered(race_name, race_tuple_list, name_dict, similar_names)

def orc(race_name, race_tuple_list, name_dict, similar_names = False):
    leading_orc_L2_space = True
    trailing_orc_L2_space = False
    name = ""
    first_char = None
    for tuple_var in race_tuple_list:
        tuple_name, tuple_probability = race_tuple_contents(tuple_var)
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
        name += add_syllable(tuple_var, name_dict, predetermined=add_next_syllable)
    return [race_name, name, name]


def hillgiant(race_name, race_tuple_list, name_dict, similar_names = False):
    return standard_single_name(race_name, race_tuple_list, name_dict, similar_names)

def halfling(race_name, race_tuple_list, name_dict, similar_names = False):
    return (standard_gendered(race_name, race_tuple_list, name_dict, similar_names))

def tavern(race_name, race_tuple_list, name_dict, similar_names = False):
    race_name, name, ignore = standard_single_name(race_name, race_tuple_list, name_dict, similar_names)
    name = "the "
    first_char = None
    for tuple_var in race_tuple_list:
        tuple_name, tuple_probability = race_tuple_contents(tuple_var)
        name += " "
        name += add_syllable(tuple_var, name_dict)
    return [race_name, name, name]

def elf(race_name, race_tuple_list, name_dict, similar_names = False):
    male_name = ""
    female_name = ""
    first_char = None
    for tuple_var in race_tuple_list:
        tuple_name, tuple_probability = race_tuple_contents(tuple_var)
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

def gen_race_name(app, race_name, race_tuple_list, filename_vars, similar_names = False):
    name_dict = name_files_to_dict(app, race_name, filename_vars)
    triple = None
    race_name_function = race_functions.get(race_name)
    if race_name_function:
        triple = race_functions.get(race_name)(race_name, race_tuple_list, name_dict, similar_names)
    if triple:
        race_name, male_name, female_name = triple
        return [race_name, male_name, female_name]





















