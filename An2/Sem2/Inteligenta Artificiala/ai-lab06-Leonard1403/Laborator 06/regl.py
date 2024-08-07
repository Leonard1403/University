import csv

with open('data/v2_world-happiness-report-2017.csv', newline='') as input_file, open('output.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file, quoting=csv.QUOTE_ALL)

    # scrie header-ul
    writer.writerow(next(reader))

    # scrie rândurile, filtrând rândurile care conțin valori nule
    for row in reader:
        if any(not x for x in row):
            continue  # treci peste rândurile care conțin valori nule
        writer.writerow(row)
