import requests
import get_domain_list as gdl

# function for scanning subdomains
def domain_scanner(domain_name,sub_domnames = gdl.get_subdomain_list()):
	print('---------------------------------')
	print('[+] Subdomains :')

	count = 0 # count the number of subdomains
	for subdomain in sub_domnames:
		
		url = f"https://{subdomain}.{domain_name}" # create the url
		try:
			requests.get(url) # try to get the response from the url
			r = requests.head(url) # get the headers from the url
			ok_code = "" # create a variable to store the response code
			if r.ok:
				ok_code = "OK"
			else:
				ok_code = "Not OK"

			print(f'- [{r.status_code} {ok_code}] {url}') # print the status code and the url
			count += 1 # increment the count
		except requests.ConnectionError: # if the url is not reachable skip the url
			pass

	print("\n")
	print(f'[+] Total Subdomains Found : {count}')

