import requests
from bs4 import BeautifulSoup

def fetchRequestLinkFromStringName(page, stringName):
    try:
        url = "Link Not Found"
        soup = BeautifulSoup(page, 'html.parser')
        for link in soup.find_all('a', href=True):
            #print link.string
            #print link.get("href")
            if link.string.lower() == stringName.lower():
                url = link.get("href")
                print link.get("href")
                

    except Exception as e:
        print('Error:')
        print(e)
    return url


login = {
	'postUser':'prithvi3141',
	'postPass':'boulder123',
}
request_parameters = {
	's':'1',
}
session = requests.session()

r = session.request('POST', 'http://ec2-184-72-98-174.compute-1.amazonaws.com/index.php', json=None, data=login, headers=None, params=request_parameters)
request_parameters = {
	's':'4',
	'theatreid':'2',
}
r = session.request('GET', 'http://ec2-184-72-98-174.compute-1.amazonaws.com/customer.php', json=None, data=None, headers=None, params=request_parameters)
print r.content
stringName = "home"
url = fetchRequestLinkFromStringName(r.content, stringName)
if url == "Link Not Found":
    print url
else:
    print url
    print "India"
