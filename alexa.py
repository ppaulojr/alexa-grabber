from BeautifulSoup import BeautifulSoup
import urllib2, re
import pickle

def Alexa_top_links (country,pagina=None):
    if pagina:
        page = urllib2.urlopen("http://www.alexa.com/topsites/countries;%d/%s"%(pagina,country))
    else:
        page = urllib2.urlopen("http://www.alexa.com/topsites/countries/%s"%country)
    soup = BeautifulSoup(page)
    links = soup.findAll("a",href=re.compile("http://*"))
    lista = []
    for link in links:
        href = link.get('href', None)
        if href and href.find('alexashopping')<0:
            lista.append(href)
    return lista

def Alexa_Country (country):
    lista = Alexa_top_links(country)
    for i in range(1,5):
        lista = lista+Alexa_top_links(country,i)
    return lista

def Alexa_Fetch_countries ():
    lista = []
    page = urllib2.urlopen("http://www.alexa.com/topsites/countries")
    soup = BeautifulSoup(page)
    links = soup.findAll("a",href=re.compile("/topsites/countries/*"))
    lista = []
    for link in links:
        href = link.get('href', None)
        if href:
            lista.append(href[20:])
    return [i for i in lista if i!='']

def Alexa_Fetch_Cat (cat,pagina=None):
    if pagina:
        page = urllib2.urlopen("http://www.alexa.com/topsites/category;%d/Top/%s"%(pagina,cat))
    else:
        page = urllib2.urlopen("http://www.alexa.com/topsites/category/Top/%s"%cat)
    soup = BeautifulSoup(page)
    links = soup.findAll("a",href=re.compile("http://*"))
    lista = []
    for link in links:
        href = link.get('href', None)
        if href and href.find('alexashopping')<0:
            lista.append(href)
    return lista

def Alexa_Category (cat):
    lista = Alexa_Fetch_Cat(cat)
    for i in range(1,25):
        lista = lista+Alexa_Fetch_Cat(cat,i)
    return lista

def Alexa_Fetch_cats ():
    lista = []
    page = urllib2.urlopen("http://www.alexa.com/topsites/category")
    soup = BeautifulSoup(page)
    links = soup.findAll("a",href=re.compile("/topsites/category/Top/*"))
    lista = []
    for link in links:
        href = link.get('href', None)
        if href:
            lista.append(href[23:])
    return [i for i in lista if i!='']

def TopCountries2Disk ():
    countries = Alexa_Fetch_countries()
    CountryRank = dict()
    for country in countries:
        CountryRank[country] = Alexa_Country(country)
            lista = Alexa_Fetch_Cat(cat)
    for i in range(1,25):
        lista = lista+Alexa_Fetch_Cat(cat,i)
    return lista

def Alexa_Fetch_cats ():
    lista = []
    page = urllib2.urlopen("http://www.alexa.com/topsites/category")
    soup = BeautifulSoup(page)
    links = soup.findAll("a",href=re.compile("/topsites/category/Top/*"))
    lista = []
    for link in links:
        href = link.get('href', None)
        if href:
            lista.append(href[23:])
    return [i for i in lista if i!='']

def TopCountries2Disk ():
    countries = Alexa_Fetch_countries()
    CountryRank = dict()
    for country in countries:
        CountryRank[country] = Alexa_Country(country)
    print CountryRank
    file = open("CountryRank.pck", "w")
    pickle.dump(CountryRank, file)

def TopCats2Disk():
    cats = Alexa_Fetch_cats()
    catsRank = dict()
    for cat in cats:
        print cat
        catsRank[cat] = Alexa_Category(cat)
    print catsRank
    file = open("topcats.pck", "w")
    pickle.dump(catsRank, file)
