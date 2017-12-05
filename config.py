import importlib, sys
from pprint import pprint

import_template = "names.{}{}"

non_gendered_races = ["goblin", "orc", "hillgiant", "tavern", "newtavern", "party"]
human_races = ["human", "illuskan", "chondathan", "tethyrian", "damaran", "turami"]
race_vars={ # [text,  probablity]
            "elf":      [["F1", 1.],
                        ["F2M", 1.],
                        ["F2F", 1.],
                        ["L2",  1.],
                        ["L3",  1.],
                        ["T5",  1.],
                        ["T6",  1.]],
            "halfling": [["F1", 1.],
                        ["F2M", 0.5],
                        ["F2F", 1.],
                        ["F3",  0.25],
                        ["L1",  0.15],
                        ["L2",  1.],
                        ["L3",  0.85]],
            "hillgiant":[["F1", 1.],
                        ["F2",  1.],
                        ["F3",  0.2]],
            "orc":      [["F1", 1.],
                        ["L1",  1.],
                        ["L2",  0.25],
                        ["L3",  1.]],
            "goblin":   [["F1", 1.],
                        ["F2",  0.75],
                        ["L1",  0.1]],
            "gnome":    [["F1", 1.],
                        ["F2M",0.25],
                        ["F2F",0.25],
                        ["L1",1.],
                        ["L2",1.]],
            "human":    [["F1", 1.],
                        ["F2M", 0.75],
                        ["F2F", 0.95],
                        ["L2", 1.],
                        ["L3", 0.95]],
            "illuskan": [["F1", 1.],
                        ["F2M", 0.75],
                        ["F2F", 0.75],
                        ["L2", 1.],
                        ["L3", 0.95]],
            "chondathan":[["F1", 1.],
                        ["F2M", 0.75],
                        ["F2F", 0.75],
                        ["L2", 1.],
                        ["L3", 0.95]],
            "tethyrian":[["F1", 1.],
                        ["F2M", 0.75],
                        ["F2F", 0.75],
                        ["L2", 1.],
                        ["L3", 0.95]],
            "damaran":  [["F1", 1.],
                        ["F2M", 0.75],
                        ["F2F", 0.75],
                        ["L2", 1.],
                        ["L3", 0.95]],
            "turami":   [["F1", 1.],
                        ["F2M", 0.75],
                        ["F2F", 0.75],
                        ["L2", 1.],
                        ["L3", 0.95]],
            "dwarf":    [["F1", 1.],
                        ["F2M", 0.9],
                        ["F2F", 0.95],
                        ["L2", 1.],
                        ["L3", 0.95]],
            "tiefling": [["F1", 1.],
                        ["F2M", 1.],
                        ["F2F", 1.],
                        ["L2", 1.]],
            "tavern":   [["F1", 1.],
                        ["F2", 1.]],
            "newtavern":[# First name probability (0.2), found in create names
                        ["N1S", 0.4],
                        ["N1A", 0.75],
                        ["N2", 0.2],
                        ["N3", 1.]],
            "party":    [["P1", 0.45],
                        ["A1", 0.55],
                        ["N1", 0.35],
                        ["A1", 0.35],
                        ["N1", 0.35],
                        ["A1", 0.35],
                        ["C1", 0.45],],
}

race_name_spaces_dict = {"hillgiant": "hill giant",
                         "newtavern": "tavern (new)"}

races = sorted(race_vars.keys())

surname_affix_list = ["Mac", "Mc", "Van", "Von", "O'"]
surname_affixes = [" {}".format(x) for x in surname_affix_list]



















file_text_dict = {}
def name_files_to_dict():
      for race_name in race_vars.keys():
            race_tuple_list = race_vars.get(race_name)
            filename_vars = [x[0] for x in race_tuple_list]
            # filenames = [filename_template.format(race_name, x) for x in filename_vars]
            for filename_var in filename_vars:
                  try:
                        name_py_file = importlib.import_module(import_template.format(race_name, filename_var))
                        syllable_text_list = name_py_file.text.split("\n")
                        syllable_text_list = list(filter(None, syllable_text_list))
                        if syllable_text_list:
                              file_text_dict[race_name + filename_var] = syllable_text_list
                  except:
                        pass
name_files_to_dict()
