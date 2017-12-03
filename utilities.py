import config

def return_race_tuple_list(race_name):
    return [x for x in config.race_vars.get(race_name)]
