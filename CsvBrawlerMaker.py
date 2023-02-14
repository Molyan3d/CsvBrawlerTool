import csv

print("Ultimate CSV Tool - 1.0")
print("-> Implemented by @molyan_")
print("-> github.com/Molyan3d/CsvbrawlerMaker")
print("-> (c) Molyan Stars Team, 2023")
input_file_name = input("Enter the name of the input.csv file to open: ")
charname = input("Enter the desired TID Name: ")

tid_dict = {}

with open(input_file_name, 'r') as input_file:
    reader = csv.reader(input_file)
    headers = next(reader) 
    tid_index = headers.index("TID")  
    en_index = headers.index("EN")  
    for row in reader:
        tid = row[tid_index]
        en = row[en_index]
        tid_dict[tid] = en

new_tids = []

brawler_name = f"TID_{charname}"
brawler_desc = f"TID_{charname}_DESC"
brawler_tp = f"TID_{charname}_SHORT_DESC"
brawler_weapon = f"TID_{charname}_WEAPON"
brawler_weapon_desc = f"TID_{charname}_WEAPON_DESC"
brawler_ulti = f"TID_{charname}_ULTI"
brawler_ulti_desc = f"TID_{charname}_ULTI_DESC"
brawler_gadget = f"TID_ACCESSORY_{charname}_GADGET"
brawler_gadget_desc = f"TID_ACCESSORY_{charname}_GADGET_DESC"
brawler_sp_1= f"TID_{charname}_SP_1"
brawler_sp_1_desc = f"TID_{charname}_SP_1_DESC"
brawler_sp_2 = f"TID_{charname}_SP_2"
brawler_sp_2_desc = f"TID_{charname}_SP_2_DESC"

new_tids.extend([
    brawler_name,
    brawler_desc,
    brawler_tp,
    brawler_weapon,
    brawler_weapon_desc,
    brawler_ulti,
    brawler_ulti_desc,
    brawler_gadget,
    brawler_gadget_desc,
    brawler_sp_1,
    brawler_sp_1_desc,
    brawler_sp_2,
    brawler_sp_2_desc
])

new_en_values = []
for tid in new_tids:
    new_en = input(f"Enter the {tid}: ")
    new_en_values.append(new_en)

for i in range(len(new_tids)):
    tid_dict[new_tids[i]] = new_en_values[i]

new_rows = []
for tid, en in tid_dict.items():
    new_row = {headers[tid_index]: tid, headers[en_index]: en}
    for i in range(len(headers)):
        if i not in (tid_index, en_index):
            new_row[headers[i]] = en
    new_rows.append(new_row)

output_file_name = f"{input_file_name[:-4]}_tid_edited.csv"
with open(output_file_name, 'w', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(new_rows)

print(f"{charname} added successfully to {output_file_name}!")