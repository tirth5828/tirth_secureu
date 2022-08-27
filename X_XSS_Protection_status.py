import requests

class ScanHeaders: # class to scan the headers
	def __init__(self, url):
		self.url = url # url to scan
		response = requests.get(self.url) # get the response from the url
		self.headers = response.headers # get the headers from the response

	def scan_xxss(self): # scan the X-XSS-Protection header
		return self.headers["X-XSS-Protection"]

def X_XSS_Protection_status(url): # function to scan the X-XSS-Protection header
    url = "https://www." + url
    print('---------------------------------')
    print('[+] Header :')
    target = ScanHeaders(url) # create a ScanHeaders object
    if target.scan_xxss() == 1: # if the X-XSS-Protection header is 1 (Enabled)
        print("X-XSS-Protection : Enabled")
    else: # if the X-XSS-Protection header is 0 (Disabled)
        print("X-XSS-Protection : Disabled")

    
