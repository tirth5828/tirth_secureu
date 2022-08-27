import ssl, socket, requests

def ssl_details(url):
    print('---------------------------------')
    print('[+] SSL Details :')
    try:
        req = requests.get("https://www." + url, verify=True) # verify=True will check the SSL certificate
        print("- SSL : Enabled") 
        get_ssl_details(url) # get the SSL details
    except requests.exceptions.SSLError:
        print("- SSL : Disabled")

def get_ssl_details(hostname):
    ctx = ssl.create_default_context()  # create a context object
    with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s: # create a socket object
        s.connect((hostname, 443))  # connect to the hostname on port 443
        cert = s.getpeercert() # get the certificate from the socket
    subject = dict(x[0] for x in cert['subject']) # get the subject from the certificate
    issued_to = subject['commonName'] # get the common name from the subject
    print(f'- issued_to : {issued_to}') # print the common name

