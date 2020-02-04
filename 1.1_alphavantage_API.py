import requests
import datetime
from datetime import timedelta

def comparePrices(crypto):
	today = datetime.date.today()
	yesterday = today - datetime.timedelta(days = 1)
	crypto = str(crypto);

	data = requests.get('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol='+crypto+'&market=EUR&apikey=59I9SXKLV9VG9XO6');
	data = data.json();
	today = data["Time Series (Digital Currency Daily)"][str(today)]["4a. close (EUR)"];
	yesterday = data["Time Series (Digital Currency Daily)"][str(yesterday)]["4a. close (EUR)"];
	gains = float(today) - float(yesterday);

	f = open("positive.txt", "a")
	f1 = open("negative.txt", "a")
	if(gains > 0):
		f.write(crypto + " ")
		f.write(str(gains)+'\n')
	elif(gains < 0):
		f1.write(crypto + " ")
		f1.write(str(gains)+'\n')
	f.close()
	f1.close()

#erase
open('positive.txt', 'w').close()
open('negative.txt', 'w').close()

comparePrices("BCH");
comparePrices("ETH");
comparePrices("LTC");
comparePrices("BTC");
comparePrices("TRX");
