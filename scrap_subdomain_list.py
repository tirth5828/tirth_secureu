import requests
from bs4 import BeautifulSoup

URL = "https://bitquark.co.uk/blog/2016/02/29/the_most_popular_subdomains_on_the_internet"
r = requests.get(URL)  
soup = BeautifulSoup(r.content, 'html.parser')

table = soup.find("table")
title = table.find_all("tr")

subdomain_list = []

for i in title[1:]:
    subdomain_list.append(i.find_all("td")[1].text + "\n")

file= open('subdomain_names.txt', 'a')
file.writelines(subdomain_list)
file.close()