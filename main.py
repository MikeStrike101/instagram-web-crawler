import requests
from bs4 import BeautifulSoup
import json

username = input("Enter Instagram username: ")

r = requests.get("http://instagram.com/" + username)
soup = BeautifulSoup(r.text,'html.parser')

userInfo = soup.find("meta",property = 'og:description')
userDesc = json.loads(soup.find('script', type='application/ld+json').string)

print("Here are " + username + "'s stats: " + "\n")
print(userInfo.attrs["content"][:40])
print("                 ")
print("Here is " + username + "'s description: \n")
print(userDesc['description'])