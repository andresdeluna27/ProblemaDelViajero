import sys
from Ciudad import *
import random
import math
import time
import copy
file = open("solucion.txt","w")
gen=1

class Nodo(object):
    
    def __init__(self,lista):
        global gen
        self.distancia=0
        self.ciudades=[]
        self.acomodo=[]
        self.generacion=None
        self.cromosoma=0
        i=1
        while (i<26):
            self.acomodo.append(i)
            i+=1
        random.shuffle(self.acomodo)
        ind=self.acomodo.index(1)
        aux=self.acomodo[0]
        self.acomodo[0]=1
        self.acomodo[ind]=aux
        #print(self.acomodo)
        #print(len(lista))
        i=0
        while (i<25):
            #print(i)
            self.ciudades.append(lista[(self.acomodo[i])-1])
            self.generacion=gen
            i+=1
        self.longitud()
    
    def longitud(self):
        i=0
        while (i<24):
            self.distancia+=self.ciudades[i].distancia(self.ciudades[(i+1)])
            i+=1
        self.distancia+=self.ciudades[24].distancia(self.ciudades[0])
        return self.distancia

    def getDist(self):
        return str(self.distancia)

    def getList(self):
        i=0
        cad="coordenadas"
        while i<25:
            cad+=str(str(i)+" "+self.ciudades[i].impr()+" ")
            i+=1
        print(cad)

    def printOrden(self,num):
        aux=self.acomodo
        if num==0:
            aux.append(1)
        return aux
        #file.write(""+str(aux))
        #file.write("\n")
        #print('distancia:  '+self.getDist())
        #file.write('distancia:  '+lista.getDist())   
        #file.write("\n")
        #self.getList()

    def cruce(self,lista):#funcion que hace los cruzamientos de los nodos
        i=1
        segAcomodo=[]
        k=0
        while k<26:
            segAcomodo.append(int(1))
            k+=1
        segAcomodo[1]=self.acomodo[1]
        paro=True
        aux=self.acomodo[1]
        aux2=lista[1]
        ind=0
        while (paro):#primera parte del ciclo
            ind=self.acomodo.index(aux2)
            segAcomodo[ind]=self.acomodo[ind]
            aux2=lista[ind]
            if ind==24 or aux==aux2:
                paro=False
        i=0
        while i<25:#el relleno con los faltantes
            if segAcomodo[i]==1:
                if lista[i]==aux:
                    segAcomodo[i]=aux2
                else:
                    segAcomodo[i]=lista[i]
            i+=1
        return segAcomodo

    def cambioAcomodo(self,lista,city): #cambia el orden de las ciudades despues del cruce
        self.acomodo=copy.deepcopy(lista)
        i=0
        while i<25:
            self.ciudades[i]=(city[(self.acomodo[i])-1])
            i+=1
        self.distancia=0#se setea la longitud en cero 
        self.longitud()#se vuelve a calcular con el nuevo acomodo
        

    def getAcomodo(self): #sirve para pasar como argumento a la funcion cruce
        return self.acomodo
            
            
nodos=[]
i=1
while (i<26):
    nodos.append(Ciudad(i))
    i+=1
lista=[]
i=0
file.write("{:<12} {:<65} {:<57} {:<150}".format('Generacion','Cromosoma','Lista','Distancia'))
file.write("\n")
while (i<100):
    lista.append(Nodo(nodos))
    lista[i].cromosoma=i+1
    #time.sleep(0.03)
    file.write("{:<15} {:<15} {:<100} {:<150}".format(str(lista[i].generacion),str(lista[i].cromosoma),str(lista[i].printOrden(0)),str(lista[i].getDist())))
    file.write("\n")
    #print('distancia:  '+lista[i].getDist())
    i+=1

lista = sorted(lista, key=lambda nodo: nodo.distancia)
i=0
lista2=[]
nuevaGen=[]
print("----------------ordenados")
file.write("\n")
while(i<50):
    file.write("{:<15} {:<15} {:<100} {:<150}".format(str(lista[i].generacion),str(lista[i].cromosoma),str(lista[i].printOrden(1)),str(lista[i].getDist())))
    file.write("\n")
    #print(str(lista[i].printOrden())+" "+str(lista[i].getDist()))
    i+=1
print('--------------------------------')
i=0
while (i<50):
    lista2.append(lista[i])
    i+=1
#nuevaGen=lista
#lista2=copy.deepcopy(lista)
nuevaGen=copy.deepcopy(lista)

r=0
cont=0
#print('--------------------------------')
#print(lista2[0].getAcomodo())
#print(lista2[0].getDist())
#print(lista2[1].getAcomodo())
#print(lista2[1].getDist())
#print(lista2[0].cruce(lista2[1].getAcomodo()))
#aux=lista2[0]
#aux.cambioAcomodo(lista2[0].cruce(lista2[1].getAcomodo()),nodos)
#print(aux.getAcomodo())
#print(aux.getDist())
#print('--------------------------------')

for i in range(50):
    for k in range(2):
        if i==48:
            if k!=1:
                nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[49].getAcomodo()),nodos)
            else:
                nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[0].getAcomodo()),nodos)
        elif i==49:
            if k!=1:
                nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[0].getAcomodo()),nodos)
            else:
                nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[1].getAcomodo()),nodos)
        else:
            nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(i+k+1)].getAcomodo()),nodos)
        r+=1


nuevaGen = sorted(nuevaGen, key=lambda nodo: nodo.distancia)
i=0
while (i<100):
    print(str(i)+" "+str(nuevaGen[i].printOrden(1))+" "+str(nuevaGen[i].getDist()))
    #nuevaGen[i].cambioAcomodo(lista2[uno[i]].cruce(lista2[dos[i]].getAcomodo()),nodos)
    #print(str(i)+" orden: "+str(nuevaGen[i].printOrden(1))+" --distancia-- "+str(nuevaGen[i].getDist()))
    i+=1


#print(uno)
#print(dos)
file.close();
