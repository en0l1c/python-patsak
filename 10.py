
#Author: Konstantinos Gialantzis
#Last update: 17/02/2019

from bs4 import BeautifulSoup
import requests

#TODO:
#1)the raw_input is too dangerous for security reasons. Gonna change it

url = raw_input('Type the link of the website:')

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")


count_url = 0
count_blnk_br = 0
count_blnk_p = 0

for link in soup.find_all('a'):
    count_url += 1

for link in soup.find_all('br'):
	count_blnk_br += 1

for link in soup.find_all('p'):
	count_blnk_p += 1

print "The links on this website are: "
print count_url

print "The <br> and <p> on this website are: "
print count_blnk_br + count_blnk_p


#this exercises tested on www.cs.unipi.gr,  www.google.gr
