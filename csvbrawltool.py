import csv
import os
import sys

debug = "--debug" in sys.argv

PACKAGE_VERSION = "\033[32m2.0\033[0m"
AUTHOR = "\033[32m@molyan_\033[0m"
GITHUB_LINK = "\033[32mgithub.com/Molyan3d/CsvbrawlerMaker\033[0m"
COPYRIGHT_DESC = "\033[32m(c) Molyan Stars Team, 2023\033[0m"
def info(msg: str):
    print(f"\033[32m-> {msg}\033[0m")

def raise_exception(err, msg: str) -> None:
    info(f"Error: {msg}")
    raise err

def read_csv(filepath: str) -> list:  
    try:
        rows = [row for row in csv.reader(open(filepath, 'r', encoding="UTF-8"))]
    except FileNotFoundError as err:
        raise_exception(err, "CSV file not found!")
        return []

    return rows

def write_csv(csv_rows: list, filepath: str) -> None:
    with open(filepath, "w", encoding="UTF-8") as f:
        writer = csv.writer(f, delimiter=',')
        for row in csv_rows:
            writer.writerow(row)

def print_credits() -> None:
    print(f'\033[32mUltimate CSV Tool - {PACKAGE_VERSION}\033[0m')
    info(f'\033[32mImplemented by {AUTHOR}\033[0m')
    info(GITHUB_LINK)
    info(COPYRIGHT_DESC)

def create_character_localization(csv_rows: list, character_name: str) -> None: 

    if len(csv_rows) <= 2:  
        raise_exception(Exception("Wrong csv file"), "CSV file is too small!")

    header = csv_rows[0]
    if "EN" not in header:  
        raise_exception(Exception("Wrong header in csv file"),
                        "Сsv file does not contain necessary strings for localization")

    tids = [
        f"TID_{character_name}",
        f"TID_{character_name}_DESC",
        f"TID_{character_name}_SHORT_DESC",
        f"TID_{character_name}_WEAPON",
        f"TID_{character_name}_WEAPON_DESC",
        f"TID_{character_name}_ULTI",
        f"TID_{character_name}_ULTI_DESC",
        f"TID_ACCESSORY_{character_name}_GADGET",
        f"TID_ACCESSORY_{character_name}_GADGET_DESC",
        f"TID_{character_name}_SP_1",
        f"TID_{character_name}_SP_1_DESC",
        f"TID_{character_name}_SP_2",
        f"TID_{character_name}_SP_2_DESC"
    ]

    tids_values = ['' for _ in tids]

    if not debug:
        tids_values[0] = str(input("Enter the Brawler Name: "))
        tids_values[1] = str(input("Enter the Brawler Description: "))
        tids_values[2] = str(input("Enter the Brawler Tipology: "))
        tids_values[3] = str(input("Enter the Attack Name: "))
        tids_values[4] = str(input("Enter the Attack Description: "))
        tids_values[5] = str(input("Enter the Ulti Name: "))
        tids_values[6] = str(input("Enter the Ulti Description: "))
        tids_values[7] = str(input("Enter the Gadget Name: "))
        tids_values[8] = str(input("Enter the Gadget Description: "))
        tids_values[9] = str(input("Enter the 1st Star Power Name: "))
        tids_values[10] = str(input("Enter the 1st Star Power Description: "))
        tids_values[11] = str(input("Enter the 2nd Star Power Name: "))
        tids_values[12] = str(input("Enter the 2nd Star Power Description: "))

    for i in range(len(tids)):
        '''row = []
        for index in range(len(header)): # so we get number of columns and iterate over each
            # If this is first column, then tid should be here
            if index == 0:
                row.append(tids[i])
            else: # else append value
                row.append(tids_values[i])'''
        row = [tids[i] if idx == 0 else tids_values[i] for idx in range(len(header))] 
        csv_rows.append(row)

def create_character_localization_input() -> None:
    input_file_name = input("Enter the name of the input.csv file to open: ")
    if not debug:
        charname = input("Enter the desired TID Name: ")
    else:
        charname = "test"

    if len(input_file_name) <= 0:
        raise_exception(FileExistsError(), "Wrong filename!")
    if len(charname) <= 0:
        raise_exception(Exception(), "Wrong character name!")
    csv_rows = read_csv(input_file_name)

    create_character_localization(csv_rows, charname)  

    name, ext = os.path.splitext(input_file_name)
    output_filepath = f'{name}_tid{ext}'
    write_csv(csv_rows, output_filepath)
    info(f"File written to {output_filepath}")

if __name__ == "__main__":
    print_credits()
    create_character_localization_input()
