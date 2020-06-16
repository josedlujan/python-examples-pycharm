#Peso
import os
import requests
import re
import urllib.request as request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import html5lib
from lxml import etree
####HTTPS######
req = request.Request('http://python.org')
res = request.urlopen(req)
print("HTTP or HTTPS: ", res.geturl())


##########################TAMAÑO DE PAGINA ###########################
link = "https://python.org"
print ("url:", link)
site = request.urlopen(link)
meta = site.info()
print ("Content-Length:", site.headers['content-length'])

#Create the file out.txt before script execute
f = open("out.txt", "r")
print ("File on disk:",len(f.read()))
f.close()

f = open("out.txt", "wb")
f.write(site.read())
site.close()
f.close()

f = open("out.txt", "r")
print ("File on disk after download:",len(f.read()))
f.close()

print ("os.stat().st_size returns:", os.stat("out.txt").st_size)

###############################TITLE###############################
html = urlopen("http://edteam.com")
soup = BeautifulSoup(html.read())
print(len(soup.html.head.title.string))
print(soup.html.head.title.string)
###############################TITLE###############################

###############################DESCRIPTION########################
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
description = soup.find('meta',attrs={'name':'description'})
print(len(description.get('content')))
if(len(description.get('content')))<154:
    print("La descripción es menor a 154")
print("description:",description.get('content'))
##############################DESCRIPTION###########################

#############################IMG ALT################################
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
count = 1
for image in soup.findAll("img"):
    print("Imagen #",count,":",image["src"])
    print("Alt de imagen #",count,":",image.get('alt','None'))
    count += 1




#############################IMG ALT################################

############################REPEAT KEYWORD##########################
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
keywords = soup.find('meta',attrs={'name':'keywords'})
print("Keywords:",keywords.get('content'))
words=keywords.get('content').split()
print(words)
for word in words:
    print(word,len(soup.findAll(text=re.compile(word))))
    #print(word,soup.find(text=re.compile(word)))

####################################################################



###########################WWW##########################
req = request.Request('http://python.org')
res = request.urlopen(req)
print(res.geturl())


###########################WWW##########################

####DIA 2 ####DIA 2 ####DIA 2 ####DIA 2 ####DIA 2 ####DIA 2

############################h1##########################
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
print(soup.find_all('h1'))
for h1 in soup.find_all('h1'):
    print('Este es un h1:',h1)
print("En total son: ",len(soup.find_all('h1')))

############################h1##########################



###################check links###########################
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
links = []
elements = soup.select('a')
#Nos trae todos los enlaces
# for element in elements:
#    link = element.get('href')
#    links.append(link)
#

#queremos los enlaces http
for element in elements:
    link = element.get('href')
    if link.startswith('http'):
        links.append(link)

print(links)

for link in links[:10]:
    petition = urlopen(link)
    print("Enlace: ", link, " Respuesta: ", petition.code)


###################check links###########################



#######################FAV ICON###########################
url = "http://python.org"
page = request.urlopen(url)
soup = BeautifulSoup(page)
icon_link = soup.find("link", rel="icon")
icon = request.urlopen(url+icon_link['href'])
with open("test.ico", "wb") as f:
    try:
        f.write(icon.read())
        print ("Success!")
    except:
        print("No fav icon")
#######################FAV ICON###########################


######################LANG ###############################

site = request.urlopen("http://python.org")
soup = BeautifulSoup(site,'html.parser')
#html = soup.find('html')
lang = soup.find('html')['lang']
#lang = soup.find('html',attrs={'lang'})
print('idioma : "lang = ',lang,'"')


######################LANG ###############################


#################Buscar archivo robots.txt#########

for file in os.listdir(('/Users/jose/PycharmProjects/PrimerProyecto/public_html')):
    if file.endswith(".txt"):
        print('Se encontro el archivo robots.txt en: ', os.path.join("/Users/jose/PycharmProjects/PrimerProyecto/public_html",file))

for file in os.listdir(('/Users/jose/PycharmProjects/PrimerProyecto/public_html')):
    if file.endswith(".xml"):
        print('Se encontro el archivo: ', os.path.join("/Users/jose/PycharmProjects/PrimerProyecto/public_html", file))
########################ANALYTICS##################ç

site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
if(soup.findAll(text=re.compile(".google-analytics"))):
    print('Contiene google analytics')
else:
    print('No contiene google analytics')

########################CHARSET#####################
link = "https://python.org"
print ("url:", link)
site = request.urlopen(link)
meta = site.info()
print ("Content Type:", site.headers['content-type'])

######View port######
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
if(soup.find('meta',attrs={'name':'viewport'})):
    print('Viewport: ',description.get('content'))
else:
    print('Cuenta con Viewport')







#keywords = soup.find('meta',attrs={'name':'keywords'})
#print("Keywords:",keywords.get('content'))
#words=keywords.get('content').split()
#print(words)
#for word in words:
#    print(word,len(soup.findAll(text=re.compile(word))))
    #print(word,soup.find(text=re.compile(word)))






#metas = soup.find(attrs={"name":"description"})

#print(metas)
'''
f = urlopen( "http://python.org" ).read()
tree = etree.HTML( f )
#m = tree.xpath( "//meta" )
m = tree.xpath("//meta[@name='description']/@content")
print(len(m))
#for i in m:
 #   print (etree.tostring( i ))
    #print(etree._Attrib['property'],etree._Attrib['content'])
'''
