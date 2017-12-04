import string, random
from pprint import pprint
import config
import utilities as utils

def decision(probability):
    return random.random() < probability

def add_syllable(race_name, race_tuple_list_var, predetermined = False):
    if not predetermined:
        return_name = decision(race_tuple_list_var[1])
    else:
        return_name = predetermined
    if return_name:
        name_list = config.file_text_dict.get(race_name + race_tuple_list_var[0])
        if name_list:
            name = random.choice(name_list)
            return name
        else:
            return ""
    else:
        return ""

def standard_gendered(race_name, similar_names = False):
    male_name = ""
    female_name = ""
    first_char = None
    race_tuple_list = utils.return_race_tuple_list(race_name)
    for tuple_var in race_tuple_list:
        if first_char != tuple_var[0][0]:
            first_char = tuple_var[0][0]
            male_name += " "
            female_name += " "
        if tuple_var[0] and not tuple_var[0][-1].isdigit():
            if tuple_var[0][-1] == "M":
                male_name += add_syllable(race_name, tuple_var)
            elif tuple_var[0][-1] == "F":
                female_name += add_syllable(race_name, tuple_var)
        else:
            if similar_names: # gen similar names
                syllable = add_syllable(race_name, tuple_var)
                male_name += syllable
                female_name += syllable
            else: # or different names
                male_name += add_syllable(race_name, tuple_var)
                female_name += add_syllable(race_name, tuple_var)
    return [race_name, male_name, female_name]

def standard_nongendered(race_name, similar_names = False):
    name = ""
    first_char = None
    race_tuple_list = utils.return_race_tuple_list(race_name)
    for tuple_var in race_tuple_list:
        if first_char != tuple_var[0][0]:
            first_char = tuple_var[0][0]
            name += " "
        name += add_syllable(race_name, tuple_var)
    return [race_name, name, name]

def standard_single_name(race_name, similar_names = False):
    name = ""
    first_char = None
    race_tuple_list = utils.return_race_tuple_list(race_name)
    for tuple_var in race_tuple_list:

        name += add_syllable(race_name, tuple_var)
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
        add_next_syllable = decision(tuple_var[1])
        if first_char != tuple_var[0][0]:
            first_char = tuple_var[0][0]
            name += " "
        if leading_orc_L2_space and tuple_var[0] == "L2":
            if add_next_syllable:
                name += " "
                leading_orc_L2_space = False
                trailing_orc_L2_space = True
        if trailing_orc_L2_space and tuple_var[0] == "L3":
            name += " "
            trailing_orc_L2_space = False
        name += add_syllable(race_name, tuple_var, predetermined=add_next_syllable)
    return [race_name, name, name]


def hillgiant(race_name, similar_names = False):
    return standard_single_name(race_name, similar_names)

def halfling(race_name, similar_names = False):
    return (standard_gendered(race_name, similar_names))

def tavern(race_name, similar_names = False):
    name = "the"
    first_char = None
    race_tuple_list = utils.return_race_tuple_list(race_name)
    print(race_tuple_list)
    for tuple_var in race_tuple_list:
        name += " "
        name += add_syllable(race_name, tuple_var)
    return [race_name, name, name]

def newtavern(race_name, similar_names = False):
    name = ""
    first_char = None
    race_tuple_list = utils.return_race_tuple_list(race_name)

    human_race_name, human_male_name, human_female_name = gen_race_name(random.choice(config.human_races))
    first_name = random.choice([human_male_name, human_female_name]).strip().split(" ")[0]

    first_name_probability = 0.2
    s_vs_and_probability = 0.8

    f1 = [first_name, first_name_probability]
    name1s_likely = race_tuple_list[0]
    name1and_likely = race_tuple_list[1]
    n2 =  race_tuple_list[2]
    n3 =  race_tuple_list[3]

    if decision(f1[1]):
        name += f1[0] + "'s"
        name += " "
        name += add_syllable(race_name, n2)
    elif decision(name1s_likely[1]):

        name += add_syllable(race_name, name1s_likely, predetermined=True)
        if decision(s_vs_and_probability):
            name = "The " + name + "'s "
        else:
            name = "The " + name + " and "
        name += add_syllable(race_name, n2)
    elif decision(name1and_likely[1]):
        name += add_syllable(race_name, name1and_likely, predetermined=True)
        if decision(s_vs_and_probability):
            name = "The " + name + " and "
        else:
            name = "The " + name + "'s "
        name += add_syllable(race_name, n2)

    else:
        name += add_syllable(race_name, n2, predetermined=True)
        name = "The " + name

    name += " "
    name += add_syllable(race_name, n3)
    print(name)

    return [race_name, name, name]

def elf(race_name, similar_names = False):
    male_name = ""
    female_name = ""
    first_char = None
    race_tuple_list = utils.return_race_tuple_list(race_name)
    for tuple_var in race_tuple_list:
        if first_char != tuple_var[0][0]:
            first_char = tuple_var[0][0]
            if first_char == "T":
                male_name += ")"
                female_name += ")"
            male_name += " "
            female_name += " "
            if first_char == "L":
                male_name += "("
                female_name += "("
        if tuple_var[0] and not tuple_var[0][-1].isdigit():
            if tuple_var[0][-1] == "M":
                male_name += add_syllable(race_name, tuple_var)
            elif tuple_var[0][-1] == "F":
                female_name += add_syllable(race_name, tuple_var)
        else:
            if similar_names: # gen similar names
                syllable = add_syllable(race_name, tuple_var)
                male_name += syllable
                female_name += syllable
            else: # or different names
                male_name += add_syllable(race_name, tuple_var)
                female_name += add_syllable(race_name, tuple_var)
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
    "newtavern": newtavern,
}

def gen_race_name(race_name, similar_names = False):
    triple = None
    race_name_function = race_functions.get(race_name)
    if race_name_function:
        triple = race_functions.get(race_name)(race_name, similar_names)
    if triple: #[race_name, male_name, female_name]
        return triple





















