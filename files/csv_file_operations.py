import csv

def read_csv(fn, delimiter):
    with open(fn, 'r') as csv_f:
        cnt = -1
        rows = csv.reader(csv_f, delimiter=delimiter)
        for row in rows:
            if cnt == -1:
                print(f"{"|".join(row)}")
            else:
                print(f"{row[0]}|{row[1]}|{row[2]}|{row[3]}")
            cnt += 1
    print(f"Total rows: {cnt}")

def write_csv(fn, header, row):
    with open(fn, 'w', newline='') as csv_f:
        writer = csv.writer(csv_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(row)
    
# read_csv('names.csv', ',')
write_csv('output.csv', ['Name', 'Age', 'City', 'Occupation'], ['Alice', '30', 'New York', 'Engineer'])
