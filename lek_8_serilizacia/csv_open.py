import csv

with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)  # quoting=csv.QUOTE_NONNUMERIC числа в числа
    for line in csv_file:
        print(line)
    print(type(line))
