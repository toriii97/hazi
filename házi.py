
import csv

xList = []
yList = []
file = open(r"C:\Users\user\Desktop\Fire.txt")
reader = csv.reader(file)
for row in reader:
    xList.append(float(row[0]))
    yList.append(float(row[1]))
file.close()

xMin = xMax = xList[0]
yMin = yMax = yList[0]
tSum = 0

def method_name():
    return xMax

for val in xList:
    if val > yMin:
        yMin = val
        tSum += val
print("Minimuma:" + str(+xMin))
print("Maximuma:" + str(+xMax))
