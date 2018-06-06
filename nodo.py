import sys
from Ciudad import *
import random
import math
import time
import copy
file = open("solucion.txt","w")
gen=0

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

    def mutacion(self,num1,num2):
        aux=self.acomodo[num1]
        self.acomodo[num1]=self.acomodo[num2]
        self.acomodo[num2]=aux

    
            
#se crean los primeros 100          
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
#acomodo de los 100 primeros
lista = sorted(lista, key=lambda nodo: nodo.distancia)
i=0
lista2=[]
nuevaGen=[]
print("----------------ordenados")
file.write("\n")
#imprime los primeros 50
while(i<50):
    file.write("{:<15} {:<15} {:<100} {:<150}".format(str(lista[i].generacion),str(lista[i].cromosoma),str(lista[i].printOrden(1)),str(lista[i].getDist())))
    file.write("\n")
    #print(str(lista[i].printOrden())+" "+str(lista[i].getDist()))
    i+=1
print('--------------------------------')
i=0
#copiamos los 50 mejores
while (i<50):
    lista2.append(lista[i])
    i+=1
#nuevaGen=lista
#lista2=copy.deepcopy(lista)
nuevaGen=copy.deepcopy(lista)
#empieza el cruce
r=0
cont=0
for i in range(0,50,2):
    nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(i+1)].getAcomodo()),nodos)
    r+=1
i=0
k=0
cont=0
while cont<25:
    for n in range (0,2):
        if (i<=47):
            nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(i+2)].getAcomodo()),nodos)
            r+=1
            cont+=1
            if cont>=25:
                break
        else:
            nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(k)].getAcomodo()),nodos)
            k+=1
            r+=1
            cont+=1
            if cont>=25:
                break
        i+=1
    i+=2
    #i+=2
    
k=0
i=0
cont=0
while cont<25:
    for n in range (0,3):
        if (i<=46):
            nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(i+3)].getAcomodo()),nodos)
            r+=1
            cont+=1
            if cont>=25:
                break
        else:
            nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(k)].getAcomodo()),nodos)
            k+=1
            r+=1
            cont+=1
            if cont>=25:
                break
        i+=1
    i+=3
    
k=0
i=0
cont=0
while cont<25:
    for n in range (0,4):
        if (i<=45):
            nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(i+4)].getAcomodo()),nodos)
            r+=1
            cont+=1
            if cont>=25:
                break
        else:
            nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(k)].getAcomodo()),nodos)
            k+=1
            r+=1
            cont+=1
            if cont>=25:
                break
        i+=1
    i+=4

    

file.write("\n")
#nuevaGen = sorted(nuevaGen, key=lambda nodo: nodo.distancia)
i=0
file.write("sin ordenar-----------------------------------------\n")
while (i<100):
    nuevaGen[i].cromosoma=i+1
    nuevaGen[i].generacion=nuevaGen[i].generacion+1
    #print(str(nuevaGen[i].printOrden(1))+" "+str(nuevaGen[i].getDist()))
    file.write("{:<15} {:<15} {:<100} {:<150}".format(str(nuevaGen[i].generacion),str(nuevaGen[i].cromosoma),str(nuevaGen[i].printOrden(1)),str(nuevaGen[i].getDist())))
    file.write("\n")
    #nuevaGen[i].cambioAcomodo(lista2[uno[i]].cruce(lista2[dos[i]].getAcomodo()),nodos)
    #print(str(i)+" orden: "+str(nuevaGen[i].printOrden(1))+" --distancia-- "+str(nuevaGen[i].getDist()))
    i+=1

file.write("\n")
#ordenacion de nueva generacion
nuevaGen = sorted(nuevaGen, key=lambda nodo: nodo.distancia)
i=0
file.write("ordenados-----------------------------------------\n")
while (i<100):
    #print(str(nuevaGen[i].printOrden(1))+" "+str(nuevaGen[i].getDist()))
    file.write("{:<15} {:<15} {:<100} {:<150}".format(str(nuevaGen[i].generacion),str(nuevaGen[i].cromosoma),str(nuevaGen[i].printOrden(1)),str(nuevaGen[i].getDist())))
    file.write("\n")
    i+=1

#comienzan las mutacuones
aux=nuevaGen[0].mutacion(4,9)
#masNodos=deepcopy(lista)
lista2=[]
i=0
while (i<50):
    lista2.append(nuevaGen[i])
    i+=1
w=0
while w<99:

    r=0
    cont=0
    i=0
    for j in range(0,50,2):
        nuevaGen[r].cambioAcomodo(lista2[j].cruce(lista2[(j+1)].getAcomodo()),nodos)
        r+=1
    i=0
    k=0
    cont=0
    while cont<25:
        for n in range (0,2):
            if (i<=47):
                nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(i+2)].getAcomodo()),nodos)
                r+=1
                cont+=1
                if cont>=25:
                    break
            else:
                nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(k)].getAcomodo()),nodos)
                k+=1
                r+=1
                cont+=1
                if cont>=25:
                    break
            i+=1
        i+=2
        #i+=2
    
    k=0
    i=0
    cont=0
    while cont<25:
        for n in range (0,3):
            if (i<=46):
                nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(i+3)].getAcomodo()),nodos)
                r+=1
                cont+=1
                if cont>=25:
                    break
            else:
                nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(k)].getAcomodo()),nodos)
                k+=1
                r+=1
                cont+=1
                if cont>=25:
                    break
            i+=1
        i+=3
    
    k=0
    i=0
    cont=0
    while cont<25:
        for n in range (0,4):
            if (i<=45):
                nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(i+4)].getAcomodo()),nodos)
                r+=1
                cont+=1
                if cont>=25:
                    break
            else:
                nuevaGen[r].cambioAcomodo(lista2[i].cruce(lista2[(k)].getAcomodo()),nodos)
                k+=1
                r+=1
                cont+=1
                if cont>=25:
                    break
            i+=1
        i+=4

    

    file.write("\n")
    #nuevaGen = sorted(nuevaGen, key=lambda nodo: nodo.distancia)
    i=0
    file.write("sin ordenar-----------------------------------------\n")
    while (i<100):
        nuevaGen[i].cromosoma=i+1
        nuevaGen[i].generacion=nuevaGen[i].generacion+1
        #print(str(nuevaGen[i].printOrden(1))+" "+str(nuevaGen[i].getDist()))
        file.write("{:<15} {:<15} {:<100} {:<150}".format(str(nuevaGen[i].generacion),str(nuevaGen[i].cromosoma),str(nuevaGen[i].printOrden(1)),str(nuevaGen[i].getDist())))
        file.write("\n")
        #nuevaGen[i].cambioAcomodo(lista2[uno[i]].cruce(lista2[dos[i]].getAcomodo()),nodos)
        #print(str(i)+" orden: "+str(nuevaGen[i].printOrden(1))+" --distancia-- "+str(nuevaGen[i].getDist()))
        i+=1

    file.write("\n")
    #ordenacion de nueva generacion
    nuevaGen = sorted(nuevaGen, key=lambda nodo: nodo.distancia)
    i=0
    file.write("ordenados-----------------------------------------\n")
    while (i<100):
        #print(str(nuevaGen[i].printOrden(1))+" "+str(nuevaGen[i].getDist()))
        file.write("{:<15} {:<15} {:<100} {:<150}".format(str(nuevaGen[i].generacion),str(nuevaGen[i].cromosoma),str(nuevaGen[i].printOrden(1)),str(nuevaGen[i].getDist())))
        file.write("\n")
        i+=1
    nuevaGen[0].mutacion(4,9)
    lista2=[]
    i=0
    while (i<50):
        lista2.append(nuevaGen[i])
        i+=1
    w+=1



#print(uno)
#print(dos)
file.close();
