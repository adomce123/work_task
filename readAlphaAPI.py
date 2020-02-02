import os

path = 'C:\\Users\\Adam\\source\\repos\\alphavantage API\\alphavantage API\\negative.txt'
if(os.path.getsize(path) > 0):
    with open(path) as openfileobject:
        min = 0;
        for line in openfileobject:
            words = line.split();
            if(float(words[1]) < float(min)):
                min = words[1];
                lossTicker = words[0];
    print("Biggest loss from prev day: " + lossTicker + " " + min);
else:
    print("File is empty")

path = 'C:\\Users\\Adam\\source\\repos\\alphavantage API\\alphavantage API\\positive.txt'
if(os.path.getsize(path) > 0):
    with open(path) as openfileobject:
        max = 0;
        for line in openfileobject:
            words = line.split();
            if(float(words[1]) > float(max)):
                max = words[1];
                gainTicker = words[0];
    print("Biggest gain from prev day: " + gainTicker + " " + max);
else:
    print("File is empty")
