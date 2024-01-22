#Reto 1, Autor: Brian Sebastian Caceres Pinzon
#print("Por favor ingrese su valor de hemoglobina en g/dL con punto (.) decimal: ")#Mensaje en pantalla
hemoglobina=float(input())#Lee hemoglobina y lo comvierte a tipo de dato float

#print("Por favor ingrese su genero 1-> Femenino o 2-> Hombre: ")#Mensaje en pantalla
genero=int(input())#Lee el numero indicador de genero y lo conierte a entero

if genero==1:#Caso si es mujer
    #print("Usted es mujer")
 
    if hemoglobina<13.2:                          #Caso 1 para mujer
        print("Alerta 1")
    if 13.2<=hemoglobina and hemoglobina<=16.6:   #Caso 2 para mujer
        print("Sin alerta")
    if hemoglobina>16.6:                          #Caso 3 para mujer
        print("Alerta 2")

if genero==2:#Caso si es hombre
    #print("Usted es hombre")

    if hemoglobina<11.6:                          #Caso 1 para hombre
        print("Alerta 1")
    if 11.6<=hemoglobina and hemoglobina<=15:     #Caso 2 para hombre
        print("Sin alerta")
    if hemoglobina>15:                            #Caso 3 para hombre
        print("Alerta 2")

if genero <1 or genero >2:#Caso no es hombre ni mujer
    print("No es posible generar la alerta")




