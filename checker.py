import requests, os
from random import randint
from colorama import Fore

os.system("cls")
p = input(Fore.BLUE + "Proxies: " + Fore.CYAN)
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
proxfile = open(p, 'r')
for prox in proxfile:
	proxies = {'http': prox}
	username = letters[randint(0, 25)] + letters[randint(0, 25)] + letters[randint(0, 25)] + letters[randint(0, 25)]
	r = requests.get("https://github.com/" + username, headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36 Edg/88.0.705.63'}, proxies=proxies)
	if  "not" in r.text:
		print(Fore.RED + "[TAKEN] " + username)
	else:
		print(Fore.GREEN + "[AVAILABLE] " + username)
		