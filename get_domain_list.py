# opening the subdomain text file in the read mode
subdomain = []

with open('C:\\Users\\TIRTH JOSHI\\Desktop\\SECUREU Python\\subdomain_name.txt','r') as file:
	name = file.read()
	subdomain = name.splitlines()
    
def get_subdomain_list():
    return subdomain

# print(subdomain)
    
