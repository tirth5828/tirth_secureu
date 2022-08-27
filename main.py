import domain_scanner as ds
import ssl_details as ssld
import port_status as ps
import X_XSS_Protection_status as xxss

def get_details(url):
    ds.domain_scanner(url)
    ssld.ssl_details(url)
    ps.port_scanner(url)
    xxss.X_XSS_Protection_status(url)

