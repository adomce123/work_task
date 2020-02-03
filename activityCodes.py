import re
# with open("C:\\Users\\bd6612\\Downloads\\Task\\LogsToSplit.txt") as openfileobject:
#     for line in openfileobject:
#         pattern="2018-06-11(.*)info"
#         result=re.search(pattern,line)
#         if result:
#             print(result.group(1))

value = "name"
f = open("C:\\Users\\bd6612\\Scripts\\"+value+".txt", "w")
f.write("Now the file has more content!")
f.close()

log = open("C:\\Users\\bd6612\\Downloads\\Task\\LogsToSplit.txt").read()
num = 1
codes = []
while(1==1):
    x = log.split('2018-06-11')[num]
    num=num+1
    #print('2018-06-11'+x)
    pattern="02:00 (.*) info"
    result=re.search(pattern,x)
    if result:
        activityCode = result.group(1)
        if(activityCode in codes):
            f = open("C:\\Users\\bd6612\\Downloads\\Task\\logs\\"+activityCode+".txt", "a")
            f.write('2018-06-11'+x)
            f.close()
        else:
            codes.append(activityCode)
            f = open("C:\\Users\\bd6612\\Downloads\\Task\\logs\\"+activityCode+".txt", "w")
            f.write('2018-06-11'+x)
            f.close()
            
        #print(result.group(1))

