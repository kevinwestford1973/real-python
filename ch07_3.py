import csv
import os


# 7.3) Read and write CSV data

my_path = "/Users/leo/Dropbox/projects/real-python"
input_file = os.path.join(my_path, "pastimes.csv")
output_file = os.path.join(my_path, "categorized pastimes.csv")

with open(input_file, "r") as read_file, open(output_file, "w") as write_file:
    reader = csv.reader(read_file)
    writer = csv.writer(write_file)

    next(reader)
    writer.writerow(["Name", "Favorite Pastime", "Type of Pastime"])

    for row in reader:
        if row[1].lower().find("fighting") >= 0:
            row.append("Combat")
        else:
            row.append("Other")
        writer.writerow(row)

