import requests
import schedule
import time

def job1():
	url1 = "http://127.0.0.1:8000/wsapi/humidity/humidity"
	r1 = requests.get(url = url1)
	r1 = r1.json()
	print("Request 1 ",r1)

def job2():
	url2= "http://127.0.0.1:8001/api/dev301/ON"
	r2 = requests.get(url = url2)
	r2 = r2.json()
	print("Request 2 ",r2)

while True:
	job1()
	job2()
	time.sleep(5)