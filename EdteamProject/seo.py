#Auditoria SEO

import urllib.request as request

from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import re;

############Contar los h1########
from lxml.html._diffcommand import description

site =  request.urlopen("http://python.org")
soup = BeautifulSoup(site)
for h1 in soup.find_all('h1'):
    print('este es un h1:',h1)
print("En total son: ", len(soup.find_all('h1')))


#######check links ################
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
links = []
elements = soup.select('a')

for element in elements:
    link = element.get('href')
    if link.startswith('http'):
        links.append(link)

print(links)

for link in links[:10]:
    petition = urlopen(link)
    print("Enlace;  ", link, " Respuesta: ", petition.code)

###############ANALYTICS###############

for file in os.listdir('/Users/jose/PycharmProjects/EdteamProject/public_html'):
    if(file.endswith(".txt")):
        print("Se encontro el archivo robots.txt en: ", os.path.join('/Users/jose/PycharmProjects/EdteamProject/public_html',file))

for file in os.listdir('/Users/jose/PycharmProjects/EdteamProject/public_html'):
    if(file.endswith(".xml")):
        print("Se encontro el archivo  ", os.path.join('/Users/jose/PycharmProjects/EdteamProject/public_html',file))

url = "http://python.org"
page = request.urlopen(url)
soup = BeautifulSoup(page)
icon_link = soup.find('link',rel="icon")
icon = request.urlopen(url+icon_link['href'])
with open("test.ico","wb") as f:
    try:
        f.write(icon.read())
        print("Succes!")
    except:
        print("No hay Icono")

##### ANALYTICS #########
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
if(soup.findAll(text=re.compile(".google-analytics"))):
    print("contiene google analytics")
else:
    print("No tiene analytics")



#######Idioma ###########
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site,'html.parser')
lang  = soup.find('html')['lang']
print('El idioma del sitio web es, lang = ',lang)

#########CHARSET ########
site = "https://python.org"
print("pagina:",site)
peticion = request.urlopen(site)
meta = petition.info()
print(meta)


#########VIEWPORT########
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
print(soup.find('meta',attrs={'name':'viewport'}))
