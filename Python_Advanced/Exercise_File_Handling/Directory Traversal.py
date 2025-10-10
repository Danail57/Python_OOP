import os
from collections import defaultdict

files = defaultdict(list)
directory = "."  

for element in os.listdir(directory):
    path = os.path.join(directory, element)
    if os.path.isfile(path):
        ext = os.path.splitext(element)[1]
        files[ext].append(element)
    elif os.path.isdir(path):
        for sub_el in os.listdir(path):
            sub_path = os.path.join(path, sub_el)
            if os.path.isfile(sub_path):
                ext = os.path.splitext(sub_el)[1]
                files[ext].append(sub_el)

with open("dir_traversal.txt", "w") as report:
    for ext, filenames in sorted(files.items()):
        report.write(f"{ext}\n")
        for name in sorted(filenames):
            report.write(f"- - - {name}\n")

