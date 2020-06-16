import threading
import time
'''
Es decir, si tienes un archivo llamado mi_modulo.py, si lo ejecutamos como
 programa principal el atributo __name__ será '__main__', 
 si lo usamos importandolo desde otro modulo (import mi_modulo) 
 el atributo __name__ será igual a 'mi_modulo'.
'''
class MiHilo(threading.Thread):
    def run(self):
        print("{} inicio".format(self.getName()))
        time.sleep(1)
        print("{} terminado".format(self.getName()))

if __name__ == "__main__":
    for x in range(4):
        hilo = MiHilo(name="Thread - {}".format(x+1))
        hilo.start()
        time.sleep(.5)