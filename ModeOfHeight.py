import csv
from collections import Counter

with open('HeightWeight.csv',newline='') as l:
    read= csv.reader(l)
    list= list(read)

list.pop(0)

file=[]

for i in range(len(list)):
    height=list[i][1]
    file.append(float(height))

counting=Counter(file)

range={
    '50-60':0,
    '60-70':0,
    '70-80':0
}

for i,occurence in counting.items():
    if 50<float(i)<60:
        range['50-60']+= occurence
    elif 60<float(i)<70:
         range['60-70']+= occurence
    elif 70<float(i)<80:
        range['70-80']+= occurence


crange,coccurence=0,0

for i,occurence in range.items():

    if occurence>coccurence:
        crange,coccurence=[int(i.split('-')[0]),int(i.split('-')[1])],occurence

    
mode= float((crange[0]+crange[1])/2)
print(f"The Mode Of The Height(Inches) -> {mode:2f} ")


