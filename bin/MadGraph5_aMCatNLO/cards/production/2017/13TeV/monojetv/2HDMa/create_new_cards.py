import csv

with open('MA-vs-Ma_scan.csv') as f:
    data_old = [tuple(line) for line in csv.reader(f)]

data_new = []
for MA in range(200, 2100,100):
    for Ma in range(100, 1100,100):
        data_new.append((MA,Ma))
print(data_new)
print(len(data_new))
