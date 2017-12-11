import requests
import sys
from control_lib import *
from word2number import w2n
import selenium.webdriver as webdriver

state = None

print sys.path

url_base = 'http://ec2-184-72-98-174.compute-1.amazonaws.com/'

login = {
	'postUser':'prithvi3141',
	'postPass':'boulder123',
}
request_parameters = {
	's':'1',
}

def main():
    
    default_browser = webbrowser.get()
    state = 1
    request_parameters = {
	's':'1',
    }
    
    session = requests.session()
    r = session.request('POST', url_base + 'index.php', json=None, data=login, headers=None, params=request_parameters)

    with open("results.html", "w") as f:
        f.write(r.content)
    default_browser.open("results.html", new=0)

    while 1:
        
        data = recordAudio()
        lower_data = data.lower()
        if lower_data.startswith('google'):
            command = lower_data.split(' ', 1)
            if len(command) == 1:
                continue
            if state == 1:
                if command[1].startswith('movies in'):
                    theatreName = command[1].split('in ', 1)
                    if len(theatreName) == 2:
                        stringName = theatreName[1] 
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            print "India"
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)
                            state = 2
                            print "India"
                    
            elif state == 2:
                if command[1].startswith('go to'):
                    theatreName = command[1].split('to ', 1)
                    if len(theatreName) == 2:                    
                        stringName = theatreName[1] 
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)
                            state = 3
                elif command[1].startswith('add to'):
                    words = command[1].split(' ')
                    length = len(words)
                    if words[length-1] == 'favorites':
                        stringName = 'add to favorites'
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)

                elif command[1].startswith('remove from'):
                    words = command[1].split(' ')
                    length = len(words)
                    if words[length-1] == 'favorites':
                        stringName = 'remove from favorites'
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)
            elif state == 3:
                if command[1].startswith('book tickets'):
                    speak('Which Show')
                    while 1:
                        data = recordAudio()
                        lower_data = data.lower()
                        words = lower_data.split(' ')
                        if len(words)==2:
                            if words[0] == 'show':
                                if words[1].isdigit():
                                    #number = int(words[1])
                                    className = 'show'+str(words[1])
                                    print className
                                    url = fetchPostLinkFromClassName(r.content, className)
                                    if url == 'Link Not Found':
                                        speak('There is no such show')
                                        continue
                                    print 'India'
                                    print url
                                    
                                    while 1:
                                        speak('How many tickets')
                                        data = recordAudio()
                                        lower_data = data.lower()
                                        words = lower_data.split(' ')
                                        if len(words)==2:
                                            if words[1] == 'tickets' or words[1] == 'ticket':
                                                if words[0].isdigit():
                                                    numberOfTickets = int(words[0])
                                                    print numberOfTickets
                                                    body = {
                                                        'numberofseats':numberOfTickets,
                                                    }
                                                    r = session.request('POST', url_base + url, json=None, data=None, headers=None, params=None)
                                                    url = fetchPostLinkFromClassName(r.content, 'Show')
                                                    r = session.request('POST', url_base + url, json=None, data=body, headers=None, params=None)
                                                    print r.content
                                                    with open("results.html", "w") as f:
                                                        f.write(r.content)
                                                    default_browser.open("results.html", new=0)
                                                    
                                                    
                                                    
                                                    break
                                                else:
                                                    continue
                                        else:
                                            continue
                                else:
                                    continue
                            else:
                                continue
                        elif len(words)==1:
                            if words[0].isdigit():
                                
                                className = 'show'+str(words[0])
                                print className
                                url = fetchPostLinkFromClassName(r.content, className)
                                if url == 'Link Not Found':
                                    speak('There is no such show')
                                    continue
                                print 'India'
                                print url
                                while 1:
                                    speak('How many tickets')
                                    data = recordAudio()
                                    lower_data = data.lower()
                                    words = lower_data.split(' ')
                                    print words[1]
                                    if len(words)==2:
                                        if words[1] == 'tickets' or words[1] == 'ticket':
                                            if words[0].isdigit():
                                                numberOfTickets = int(words[0])
                                                print numberOfTickets
                                                body = {
                                                    'numberofseats':numberOfTickets,
                                                }
                                                r = session.request('POST', url_base + url, json=None, data=None, headers=None, params=None)
                                                url = fetchPostLinkFromClassName(r.content, 'Show')
                                                r = session.request('POST', url_base + url, json=None, data=body, headers=None, params=None)
                                                print r.content
                                                with open("results.html", "w") as f:
                                                    f.write(r.content)
                                                default_browser.open("results.html", new=0)

                                                break
                            else:
                                continue
                        else:
                            continue
                        break

            elif state == 4:
                if command[1].startswith('theaters in'):
                    theatreName = command[1].split('in ', 1)
                    if len(theatreName)==2:
                        stringName = theatreName[1] 
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)
                            state = 1



            elif state == 5:
                if command[1].startswith('movies in'):
                    theatreName = command[1].split('in ', 1)
                    if len(theatreName)==2:
                        stringName = theatreName[1]
                        print stringName
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)
                            state = 2

                elif command[1].startswith('go to'):
                    theatreName = command[1].split('to ', 1)
                    if len(theatreName)==2:
                        stringName = theatreName[1] 
                        url = fetchRequestLinkFromStringName(r.content, stringName)
                        if url == "Link Not Found":
                            print url
                        else:
                            print url
                            r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                            print r.content
                            with open("results.html", "w") as f:
                                f.write(r.content)
                            default_browser.open("results.html", new=0)
                            state = 3

                    
            if command[1] == 'go home':
                    theatreName = command[1].split(' ')
                    stringName = theatreName[1] 
                    url = fetchRequestLinkFromStringName(r.content, stringName)
                    if url == "Link Not Found":
                        print url
                    else:
                        print url
                        r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                        print r.content
                        with open("results.html", "w") as f:
                            f.write(r.content)
                        default_browser.open("results.html", new=0)
                        state = 1
            elif command[1] == 'show me cities':
                    stringName = 'view theaters by location' 
                    url = fetchRequestLinkFromStringName(r.content, stringName)
                    if url == "Link Not Found":
                        print url
                    else:
                        print url
                        r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                        print r.content
                        with open("results.html", "w") as f:
                            f.write(r.content)
                        default_browser.open("results.html", new=0)
                        state = 4
            elif command[1] == 'show me favorite theaters':
                    stringName = 'favorite theatres' 
                    url = fetchRequestLinkFromStringName(r.content, stringName)
                    if url == "Link Not Found":
                        print url
                    else:
                        print url
                        r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                        print r.content
                        with open("results.html", "w") as f:
                            f.write(r.content)
                        default_browser.open("results.html", new=0)
                        state = 1
            elif command[1] == 'show me booked movie shows' or command[1] == 'show me book movie shows':
                    stringName = 'booked movie shows' 
                    url = fetchRequestLinkFromStringName(r.content, stringName)
                    if url == "Link Not Found":
                        print url
                    else:
                        print url
                        r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                        print r.content
                        with open("results.html", "w") as f:
                            f.write(r.content)
                        default_browser.open("results.html", new=0)
                        state = 5
            elif command[1] == 'logout':
                    stringName = command[1] 
                    url = fetchRequestLinkFromStringName(r.content, stringName)
                    if url == "Link Not Found":
                        print url
                    else:
                        print url
                        r = session.request('GET', url_base + url, json=None, data=None, headers=None, params=None)
                        print r.content
                        with open("results.html", "w") as f:
                            f.write(r.content)
                        default_browser.open("results.html", new=0)
                        exit;

                    
            


if __name__ == "__main__":
        main() 

