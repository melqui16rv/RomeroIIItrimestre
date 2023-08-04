from classf import *
import csv
listapais=[]
with open('C:\\Users\\SENA\Music\\pais.csv') as csvDataFile:

    csvReader=csv.reader(csvDataFile)    
    for row in csvReader:
        ob=pais(row[0],row[1],row[2],row[3])
        listapais.append(ob)
        print(ob)