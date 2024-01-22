#Reto 1, Autor: Brian Sebastian Caceres Pinzon
MA1=0
MA2=0
MSA=0
HA1=0
HA2=0
HSA=0


#print("Por favor ingrese numero de personas")#Mensaje en pantalla
numPersonas=int(input())

while(numPersonas>0):
    #print("Por favor ingrese su valor de hemoglobina en g/dL con punto (.) decimal: ")#Mensaje en pantalla
    hemoglobina=float(input())#Lee hemoglobina y lo comvierte a tipo de dato float
    #print("Por favor ingrese su genero 1-> Femenino o 2-> Hombre: ")#Mensaje en pantalla
    genero=int(input())
    
    while (genero!=1 and genero!=2):
        #print("Por favor ingrese su genero 1-> Femenino o 2-> Hombre: ")#Mensaje en pantalla
        genero=int(input())

        
    if  genero==1:#Caso si es mujer
        numPersonas-=1
        
        #print("Usted es mujer")
     
        if hemoglobina<13.2:                          #Caso 1 para mujer
            #print("Alerta 1")
            MA1+=1
        elif 13.2<=hemoglobina and hemoglobina<=16.6:   #Caso 2 para mujer
            #print("Sin alerta")
            MSA+=1
        elif hemoglobina>16.6:                          #Caso 3 para mujer
            #print("Alerta 2")
            MA2+=1

    elif  genero==2:#Caso si es hombre
        numPersonas-=1
         
        #print("Usted es hombre")

        if hemoglobina<11.6:                          #Caso 1 para hombre
            #print("Alerta 1")
            HA1+=1
        elif 11.6<=hemoglobina and hemoglobina<=15:     #Caso 2 para hombre
            #print("Sin alerta")
            HSA+=1
        elif hemoglobina>15:                            #Caso 3 para hombre
            #print("Alerta 2")
            HA2+=1


print(MA1,MA2,MSA,HA1,HA2,HSA)



