import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import sys


def page_size(the_page):
    return len(the_page)


def links_to_the_same_domain(the_page, domain):
    soup = BeautifulSoup(the_page, 'html.parser')
    counter = 0

    for a in soup.find_all('a', href=True):
        if domain in a['href']:
            counter += 1
        elif "https:" in a['href'] or "http:" in a['href']:
            pass
        else:
            counter += 1

    return counter

url = sys.argv[1]

if "https" in url:
    domain = url[12:]
else:
    domain = url[11:]

try:
    req = urllib.request.Request(url)


    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print("The html web page has", page_size(the_page), "bytes.")
        print("There are", links_to_the_same_domain(the_page, domain), "links to the same domain.")

except ValueError:
    print("Ups you put an wrong URL!")

except urllib.error.HTTPError:
    print("We don't have access to your site")

except:
    print("Unkown Error")