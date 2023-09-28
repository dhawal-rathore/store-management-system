import csv
def dataWrite(obj):
    file=open('productdata.csv','w',newline='')
    writer=csv.writer(file)
    writer.writerows(obj)
    file.close()
def dataRead():
    file=open('productdata.csv','r',newline='')
    obj=[]
    for i in csv.reader(file):
        obj.append(i)
    file.close()
    return obj

