import selenium.webdriver as webdriver
from time import sleep

if __name__ == "__main__":
    urls = ['http://google.com', 'http://facebook.com','http;//colorado.edu']

b = webdriver.Firefox()

while True:
    for idx, url in enumerate(urls):
        b.maximize_window()
        b.get('http://google.com')
        sleep(20)