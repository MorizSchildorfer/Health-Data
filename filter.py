import csv

data = []
row_index = []
with open('weirds.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            row_index = row
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            data.append(row)
            line_count += 1
    print(f'Processed {line_count} lines.')

count = 0
status_counts = {}
status_index = row_index.index("Status")
con_index = row_index.index("Conditions")
hep_set = set()
fail_count = 0
fail_set = set()
print("S", status_index, "\nC", con_index)
# keywords = ["hepatitis a", "hepatitis-a", "hepatitis b", "hepatitis-b", "hepatitis c", "hepatitis-c"]
keywords = ["hepatitis a"]
count_full = 0
weirdos = []
for row in data:
    full_text = ", ".join(row)
    a = False
    if any([x in full_text.lower() for x in keywords]):
        count_full += 1
        a = True
    if not any([x in row[con_index].lower() for x in keywords]):
        if a:
            weirdos.append(full_text)
        fail_count += 1
        fail_set.add(row[con_index].lower())
        if " a" in row[con_index].lower():
            hep_set.add(row[con_index].lower())
        continue
    if row[status_index] not in status_counts:
        status_counts[row[status_index]] = 1
    else:
        status_counts[row[status_index]] += 1
    count += 1

print("Fail Set", fail_set)  
for x in hep_set:
    print(x) 
for x in weirdos:
    print(x) 
print("Status", status_counts)
print("Fails", fail_count)   
print("Full", count_full) 
