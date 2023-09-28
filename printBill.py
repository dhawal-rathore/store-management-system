import time

def printBill(l):
    sum=0
    t=time.localtime()
    f=open(f"{t[0]}_{t[1]}_{t[2]}_{t[3]}-{t[4]}-{t[5]}.txt",'w')
    f.write('\t\tShop Name\t\t\n\n')
    f.write(f"{t[3]}:{t[4]}:{t[5]}\t\t\t{t[2]}/{t[1]}/{t[0]}\n\n")
    f.write("Product Name\t\t\tQuantity\t\t\tMRP\t\t\Cost\n")
    for i in range(len(l)):
        f.write(f"{l[i][0]}\t\t\t\t\t\t{l[i][1]}\t\t\t{l[i][2]}\t\t\t{int(l[i][1])*int(l[i][2])}\n")
        sum+=int(l[i][1])*int(l[i][2])
    f.write('\n')
    for j in range(30):
        f.write('-')
    f.write(f"\nTotal Cost :\t{sum}\nThank You for shopping with us.")
    f.close()
