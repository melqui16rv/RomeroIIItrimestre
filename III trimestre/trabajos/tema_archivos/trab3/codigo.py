from classf import *
import csv
listapais=[]
with open('C:\\melqui\\pais.csv',encoding='utf-8') as csvDataFile:

    csvReader=csv.reader(csvDataFile)    
    for row in csvReader:
        ob=pais(row[1],row[3],row[7],row[12])
        listapais.append(ob)

for apr in listapais:
    #print(apr)
    print('\n''pais:',apr.getpais())
    print('poblacion:',apr.getedadMe())
    print('altura:',apr.getpobla())
    print('edad media:',apr.getaltura())