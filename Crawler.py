

from bs4 import *
from urllib.request import urlopen
from html.parser import HTMLParser
import re
choice=input("Enter choice \n1) indeed.com 2) dice.com \n")
skill=input("Enter skill ")
pincode=input("Enter pincode ")

if(choice==1):
    
    html_page = urlopen("https://www.indeed.com/jobs?q=" +skill+"&l=" +pincode)
    soup = BeautifulSoup(html_page,"html.parser")
    f= open("links_indeed.txt","w+")
    for link in soup.findAll('a', attrs={'href': re.compile("vjs")}):
        f.write("https://www.indeed.com" + link.get('href') + "\n")
    
    f.close()


else:


    html_page = urlopen("https://www.dice.com/jobs?q=" +skill+"&l=" +pincode)
    soup = BeautifulSoup(html_page,"html.parser")
    f= open("links_dice.txt","w+")
    for link in soup.findAll('a', attrs={'href': re.compile("detail/")}):
        f.write("https://www.dice.com" + link.get('href') + "\n")
    
    f.close()
