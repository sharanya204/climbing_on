import csv

header = ['date', 'name', 'grade', 'type', 'area', 'crag', 'send', 'length', 'comments']

with open("test.csv", "a", newline='') as f, open("data1.csv", "r") as d:
    writer = csv.writer(f)
    reader = csv.reader(d)
    # writer.writerow(header) # write the header
    # write the actual content line by line
    for line in reader:
        writer.writerow(line)
    # writer.close()
    # reader.close()
