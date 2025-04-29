import urllib.request
url = "https://ilmurrillo.it/"
risultato = urllib.request.urlopen(url)
theBytes = risultato.read()
text = theBytes.decode()
import bs4
doc  = bs4.BeautifulSoup(text)
print(doc.prettify())

"""root = doc.contents[0]
print(type(root))
print(root.name.upper())

def naviga(tag) :
    print(tag.name.upper())
    for stag in tag.contents:
        if type(stag) == bs4.element.Tag :
            naviga(stag)

def naviga2(tag, indent) :
    print(indent + tag.name.upper())
    for stag in tag.contests :
        if type(stag)  == bs4.element.Tag :
            naviga2(stag, indent + "  ")

naviga2(root, "") """