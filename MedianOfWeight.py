import csv

with open('HeightWeight.csv',newline='') as l:
    read= csv.reader(l)
    list= list(read)

list.pop(0)

file=[]

for i in range(len(list)):
    height=list[i][2]
    file.append(float(height))

lenght=len(file)

file.sort()

if lenght%2==0:
    median1=float(file[lenght//2])
    median2=float(file[lenght//2-1])
    median= (median1+median2)/2

else:
    median= file[lenght//2]

print('The Mode Of The Weight(Pounds) : ' +str(median))