#Reto 3 Por Brian Sebastian Caceres Pinzon (o.O)
#------Librerias------#
import os
os.system ("cls")#Limpiamos consola

#Variables
listaMedicamento=[]#la cantidad de existencias actuales del medicamento para cada sucursal
listaMedicamentoInicial=[]#Copia del anterior para hacer el calculo despues
listaSucurs=[]#número de la sucursal donde será atendido cada paciente
listaSistolica=[]
listaDiastolica=[]
dosis=[]
listaEntregado=[]
menorIndice=0
mayorIndice=0


#-------------------PROGRAMA------------------#
nm=input().split(" ")
n=int(nm[0])#cantidad sucursales
m=int(nm[1])#cantidad pacientes
while(n<1 or m<1):
    nm=input().split(" ")
    n=int(nm[0])
    m=int(nm[1])
#print(nm)
#print(n)
#print(m)
    
for i in range(n):#Leemos la cantidad de medicamentos para cada sucursal 
#    print(f"ingrese la cantidad existente de medicamento en la sucursal {i+1}: ")
    CantExistMedic=int(input())
    while(CantExistMedic<1): #Verificamos que esa cantidad sea mayor o igual a 1
#        print(f"ingrese la cantidad existente de medicamento en la sucursal {i+1} again: ")
        CantExistMedic=int(input())
    listaMedicamento.append(int(CantExistMedic))

listaMedicamentoInicial=listaMedicamento.copy()
#print("lista de medicamento")
#print(listaMedicamento)
#print("lista de medicamento inicial")
#print(listaMedicamentoInicial)


for j in range(m):#Leemos para cada paciente el numero de sucursal donde sera atendido
#    print(f"Ingrese el # de sucursal donde será atendido el paciente {j+1}, presion sistolica y diastolica usando punto: ")
    NumSucurAtendi=input().split(" ")
    while(int(NumSucurAtendi[0])<1):#Verificamos que el numero de sucursal sea mayor o igual a 1
#        print(f"Ingrese el # de sucursal donde será atendido el paciente {j+1}, presion sistolica y diastolica usando punto again: ")
        NumSucurAtendi=input().split(" ")
    
    listaSucurs.append(int(NumSucurAtendi[0]))
    listaSistolica.append(int(NumSucurAtendi[1]))
    listaDiastolica.append(int(NumSucurAtendi[2]))

#print("lista de sucursales para cada paciente")
#print(listaSucurs)
#print("lista de diastolica para cada paciente")
#print(listaDiastolica)
#print("lista de sistolica para cada paciente")
#print(listaSistolica)
    
for k in range(m):#Verificamos para cada paciente que dosis es necesaria y lo vamos almacenando en el array
    if(int(listaSistolica[k])<80 and int(listaDiastolica[k])<60):
        dosis.append(5)
    elif(120>int(listaSistolica[k])>=80 and 80>int(listaDiastolica[k])>=60):
        dosis.append(0)
    elif(130>int(listaSistolica[k])>=120 and 85>int(listaDiastolica[k])>=80):
        dosis.append(0)
    elif(140>int(listaSistolica[k])>=130 and 90>int(listaDiastolica[k])>=85):
        dosis.append(2)
    elif(160>int(listaSistolica[k])>=140 and 100>int(listaDiastolica[k])>=90):
        dosis.append(5)
    elif(180>int(listaSistolica[k])>=160 and 110>int(listaDiastolica[k])>=100):
        dosis.append(10)
    elif(int(listaSistolica[k])>=180 and int(listaDiastolica[k])>=110):
        dosis.append(30)
    elif(int(listaSistolica[k])>=140 and 90>int(listaDiastolica[k]) ):
        dosis.append(20)
    else:
        dosis.append(0)#Muy importante el caso donde no entra en los condicionales
#print("dosis")
#print(dosis)


for l in range(m):#El for recorre la cantidad m de pacientes y obtenemos su #ro de sucursal, en funcion a eso restamos la dosis de ese paciente
    listaMedicamento[(listaSucurs[l]-1)]-=int(dosis[l])#Se toma la cantidad existente, en la posicion de la sucursal numSucurs y se resta la dosis

#print("Lista de medicamento inicial")
#print(listaMedicamentoInicial)
#print("Lista de medicamento")
#print(listaMedicamento) 
   
for z in range(n):#Para cada sucursal se calculan los medicamentos entregados
    listaEntregado.append(listaMedicamentoInicial[z]-listaMedicamento[z])
    
#print("Lista de Entregado")
#print(listaEntregado)

#---------Salidas del programa----------------#

menorIndice=listaMedicamento.index(min(listaMedicamento))
print(menorIndice+1,listaMedicamento[menorIndice])

mayorIndice=listaMedicamento.index(max(listaMedicamento))
print(mayorIndice+1,listaMedicamento[mayorIndice])

for f in range(n):#entregadas*100/inicial
    cociente = listaEntregado[f]*100/listaMedicamentoInicial[f]
    prcntg = '{0:.2f}'.format(cociente)
    print(f+1,prcntg+'%')






