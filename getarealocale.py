import netifaces
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import numpy as np
dump = str(netifaces.interfaces())




#Funzione per rimuovere i caratteri di troppo
def replace22(char):
    my_new_string = char.replace("]","").replace("[","").replace("'","")
    return my_new_string

dump2= replace22(dump)
#Converto in lista array
arr = dump2.split(',')
#grandezza array
size = len(arr)
#arr.remove('Killer E2600 Gigabit Ethernet Controller')

#Utilizzo il for per visualizzare tutti gli ip delle interfacce
for x in range(size):
  print(arr[x] + ': ', netifaces.ifaddresses(arr[x].lstrip().rstrip()))
  #print(arr[x])

