
## Deployment

To deploy this project run

```bash
  pip install requirements.txt 
  python main.py
```


## Scrapper

**BeautifulSoup** is used to scrap the sub domain list.  
Code to scrap the sub domain - [scrap_subdomain_list.py](scrap_subdomain_list.py)  
List of subdomian - [subdomain_name.txt](subdomain_name.txt)  
Get all subdomian from text file in from of array - [get_domain_list.py](get_domain_list.py)  
## Output
```bash
---------------------------------
[+] Subdomains :
- [301 OK] https://mail.google.com
- [200 OK] https://www.google.com
- [301 OK] https://blog.google.com
- [302 OK] https://m.google.com
- [200 OK] https://mobile.google.com
- [301 OK] https://search.google.com
- [404 Not OK] https://api.google.com
- [302 OK] https://admin.google.com
- [302 OK] https://news.google.com
- [404 Not OK] https://sms.google.com
- [200 OK] https://video.google.com
- [302 OK] https://ads.google.com
- [404 Not OK] https://wap.google.com
- [404 Not OK] https://download.google.com
- [302 OK] https://chat.google.com
- [404 Not OK] https://web.google.com
- [404 Not OK] https://email.google.com
- [200 OK] https://cloud.google.com
- [301 OK] https://1.google.com
- [302 OK] https://admin.google.com
- [302 OK] https://store.google.com
- [404 Not OK] https://api.google.com
- [302 OK] https://news.google.com


[+] Total Subdomains Found : 34
---------------------------------
[+] SSL Details :
- SSL : Enabled
- issued_to : *.google.com
---------------------------------
[+] Ports :
[OPEN] Port open : 135
[OPEN] Port open : 139
---------------------------------
[+] Header :
X-XSS-Protection : Disabled
```