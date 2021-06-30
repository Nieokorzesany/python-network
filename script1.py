
import csv

with open('configuration.txt') as file:
    my_list = file.read().splitlines()
print(my_list)

with open('passwd.csv','r') as file:
    reader = csv.reader(file, delimiter=':', lineterminator='\n')
    for row in reader:
        print(row)