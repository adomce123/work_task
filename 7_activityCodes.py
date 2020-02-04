import re
codes = []
path = "C:\\Users\\bd6612\\Downloads\\Task\\logs\\"
with open("C:\\Users\\bd6612\\Downloads\\Task\\LogsToSplit.txt") as openfileobject:
    for line in openfileobject:
        if("] info:" in line):
            pattern=" \[(.*)] info"
            result=re.search(pattern,line)
            if result:
                activityCode = result.group(1)
                
            if(activityCode in codes):
                f = open(path+activityCode+".txt", "a")
                f.write(line)
                f.close()
            else:
                codes.append(activityCode)
                f = open(path+activityCode+".txt", "w")
                f.write(line)
                f.close()
        else:
            f = open(path+activityCode+".txt", "a")
            f.write(line)
            f.close()

codes = list(map(int, codes))
codes.sort()

f = open(path+"AllLogsSorted"+".txt", "w")
f.close()

for x in codes:
    f = open(path+str(x)+".txt", "r")
    f1 = open(path+"AllLogsSorted"+".txt", "a")
    f1.write(f.read())
    f.close()
    f1.close()

