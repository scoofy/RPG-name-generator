execute = True
test = False
if execute and not test:
    print("Start!")

import xlrd, string, sys, os
from pprint import pprint
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
current_path = os.getcwd()
if test:
    xls_path = "/Users/mschoolfield/Documents/d&d/Matts Name Generator dissection .xlsx"
else:
    xls_path = filedialog.askopenfilename()
#pprint(xls_path)

filename_text_tuple_list = []

sheet_name_list = [
            "Elf",
            "Halfling",
            "Hill Giant",
            "Orc",
            "Goblin",
            "Gnome",
            "Human",
            "Illuskan",
            "Chondathan",
            "Tethyrian",
            "Damaran",
            "Turami",
            "Dwarf",
            "Taverns",
            "Tiefling",
]
sheet_names_replace_dict = {"Taverns":"Tavern",
                            "Hill Giant":"Hillgiant",
                            }
sheet_names_replace_dict_keys = sheet_names_replace_dict.keys()
filename_suffixes = [
            "F1", "F2", "F2Male", "F2Female", "F3", "F4",
            "L1", "L2", "L3", "L4",
            "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T2/4",
]
filename_dict = {
            "F2Male":"F2M",
            "F2Female":"F2F",
            "T2/4":"T234"
}
filename_dict_keys = filename_dict.keys()

if test:
    export_path_suffix = "/testnames/here"
else:
    export_path_suffix = "/names/here"
export_path = current_path + export_path_suffix
str_file_path_list = export_path.split("/")
# print(str_file_path_list)

book = xlrd.open_workbook(xls_path)
text_row_start = None
for sheet in book.sheets():
    #pprint(sheet.name)
    if sheet.name in sheet_name_list:
        for r in range(sheet.nrows):
            if r < 3:
                pass
            else:
                try:
                    text = sheet.cell(rowx=r, colx=0).value
                    if text.replace(" ","").replace("'","").replace("-","").isalpha():
                        # print(text)
                        text_row_start = r
                        break
                except:
                    pass
        for c in range(sheet.ncols):
            col_str = ""
            try:
                potential_file_suffix = sheet.cell(rowx=text_row_start-1, colx=c).value
                #print(potential_file_suffix)
                #print("-")
                if potential_file_suffix in filename_suffixes:
                    filename_suffix = potential_file_suffix
                else:
                    filename_suffix = filename_suffixes[c]
            except:
                filename_suffix = filename_suffixes[c]
            #print(filename_suffix)
            #print("----")
            if filename_suffix in filename_dict_keys:
                filename_suffix = filename_dict.get(filename_suffix)
            for r in range(sheet.nrows):
                if r < text_row_start:
                    continue
                text = sheet.cell(rowx=r, colx=c).value
                try:
                    text.isalpha()
                    if text:
                        col_str += text + "\n"
                except:
                    '''print(text)'''
            if col_str:
                if col_str.endswith("\n"):
                    col_str = col_str[:-1]
                str_file_path_list.pop(-1)
                sheet_name = sheet.name
                if sheet_name in sheet_names_replace_dict_keys:
                    sheet_name = sheet_names_replace_dict.get(sheet_name)
                full_sheet_name = sheet_name.lower()+str(filename_suffix)+".txt"
                str_file_path_list.append(full_sheet_name)
                str_file_path = "/".join(str_file_path_list)
                name_text_tuple = [str_file_path, col_str]
                filename_text_tuple_list.append(name_text_tuple)
                #print(str_file_path)
                #pprint(col_str)
                print(full_sheet_name)

if execute:
    for name_text_tuple in filename_text_tuple_list:
        path, text = name_text_tuple
        file = open(path, "w")
        file.write(text)
        file.close()
    if not test:
        print("Finished!")















