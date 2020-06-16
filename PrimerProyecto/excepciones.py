lista = [1,2]

#error
#print(lista[4])

#excepciones

try:
    print(lista[5])
except IndexError:
    print("error en el indice")
else:
    print("Sin errores")
finally:
    print("Finalmente")

try:
    raise  TypeError
except:
    print("Lanzamos error")

class Er(Exception):
    def __init__(self,valor):
        print("Este fue el valor: ", valor)

try:
    raise Er(1)
except Er:
    print("Error tipo Er")

#the 'r' means the the following is a "raw string", ie. backslash characters are treated literally instead of signifying special treatment of the following character.
#literals
#so '\n' is a single newline
#and r'\n' is two characters - a backslash and the letter 'n'


#exp regulares
import  re
print(re.search(r"p","parangatirimicuaro"))
print(re.search(r"\d\d","parangatiri11micuaro"))


#mejoras patrons
patron = re.compile("\d\d")
print(patron.search("sdsdsds89dsdsdsdfdf99d").group())

if(re.search("[a-z][0-9].*$"," fff dddd pa1jose")):
    print("Lo encontramos")

print(re.sub(r"\d","-","holajose123@gmail.com"))








