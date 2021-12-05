import csv

with open('HeightWeight.csv',newline='') as l:
    read= csv.reader(l)
    list= list(read)

list.pop(0)

file=[]

for i in range(len(list)):
    height=list[i][1]
    file.append(float(height))

lenght=len(file)

total=0

for i in file:
    total= total+i

mean= total/lenght

print('The Mean Of The Height(Inches): '+ str(mean))

