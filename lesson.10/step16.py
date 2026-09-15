import csv


with open('data/user.csv', 'r', newline='', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=',')

    for row in reader:
        print(row)