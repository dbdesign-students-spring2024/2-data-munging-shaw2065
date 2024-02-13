# Place code below to do the analysis part of the assignment.
import csv

def compute_decade(annmean):
    return (sum(annmean)/len(annmean))

f = open('./data/clean_data.csv', 'r')
csv_reader = csv.DictReader(f)

i = 0
annmean = []
month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

for line in csv_reader:
    if i == 10:
        i = 0
    if i < 10:
        for m in month:
            try:
                annmean.append(float(line[m]))
            except:
                continue
        if i == 0:
            starting = line["Year"]
        elif i == 9:
            ending = line["Year"]
            print(starting+" to "+ending+": "+ format(compute_decade(annmean),'.2f')+"°F")
            annmean = []
    i += 1
ending = line["Year"]
print(starting+" to "+ending+": "+ format(compute_decade(annmean),'.2f')+"°F")