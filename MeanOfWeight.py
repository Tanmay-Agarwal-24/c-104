import csv

with open('HeightWeight.csv',newline='') as l:
    read= csv.reader(l)
    list= list(read)

list.pop(0)

file=[]

for i in range(len(list)):
    weight=list[i][2]
    file.append(float(weight))

lenght=len(file)

total=0

for i in file:
    total= total+i

mean= total/lenght

print('The Mean Of The Weight(Pounds): '+ str(mean))

