while True:
    num=input("Ingrese un numero de 3 digitos: ")
    print(len(num))
    dig1=int(num[0])
    dig2=int(num[1])
    dig3=int(num[2])
    num2=[0,0,0]
    #Caso 1: Todos los numeros son iguales
    if dig1==dig2 and dig1==dig3 and dig2==dig3:
        print("Caso 1.0")
        print(num)
        
    #Caso 2: Dos de los numeros son iguales  
    elif dig1==dig2 or dig1==dig3 or dig2==dig3:
        if dig1==dig2:#1=2
            if dig1>dig3:#1>3
                num2[0]=dig1
                num2[1]=dig1
                num2[2]=dig3
                print("Caso 2.1")
                print(num2[0]*100+num2[1]*10+num2[2]*1)
            elif dig3>dig1:#3>1
                num2[0]=dig3
                num2[1]=dig1
                num2[2]=dig1
                print("Caso 2.2")
                print(num2[0]*100+num2[1]*10+num2[2]*1)
            
        elif dig1==dig3:#1==3
            if dig1>dig2:#1>2
                num2[0]=dig1
                num2[1]=dig1
                num2[2]=dig2
                print("Caso 2.3")
                print(num2[0]*100+num2[1]*10+num2[2]*1)
            elif dig2>dig1:#2>1
                num2[0]=dig2
                num2[1]=dig1
                num2[2]=dig1
                print("Caso 2.4")
                print(num2[0]*100+num2[1]*10+num2[2]*1)

        elif dig2==dig3:#2=3
            if dig2>dig1:#2>1
                num2[0]=dig2
                num2[1]=dig2
                num2[2]=dig1
                print("Caso 2.5")
                print(num2[0]*100+num2[1]*10+num2[2]*1)
            elif dig1>dig2:#1>2
                num2[0]=dig1
                num2[1]=dig2
                num2[2]=dig2
                print("Caso 2.6")
                print(num2[0]*100+num2[1]*10+num2[2]*1)

    #Caso 3: Los 3 numeros son diferentes
    elif dig1>dig2 and dig1>dig3:#Mayor 1
        if dig2>dig3:#Mayor 2 que el 3
            num2[0]=dig1
            num2[1]=dig2
            num2[2]=dig3
            print("Caso 3.1")
            print(num2[0]*100+num2[1]*10+num2[2]*1)
        elif dig3>dig2:#Mayor 3 que el 2
            num2[0]=dig1
            num2[1]=dig3
            num2[2]=dig2
            print("Caso 3.2")
            print(num2[0]*100+num2[1]*10+num2[2]*1)
            
    elif dig2>dig1 and dig2>dig3:#Mayor 2
        if dig1>dig3:#Mayor 1 que el 3
            num2[0]=dig2
            num2[1]=dig1
            num2[2]=dig3
            print("Caso 3.3")
            print(num2[0]*100+num2[1]*10+num2[2]*1)
        elif dig3>dig1:#Mayor 3 que el 1
            num2[0]=dig2
            num2[1]=dig3
            num2[2]=dig1
            print("Caso 3.4")
            print(num2[0]*100+num2[1]*10+num2[2]*1)

    elif dig3>dig1 and dig3>dig2:#Mayor 3
        if dig1>dig2:#Mayor 1 que el 2
            num2[0]=dig3
            num2[1]=dig1
            num2[2]=dig2
            print("Caso 3.5")
            print(num2[0]*100+num2[1]*10+num2[2]*1)
        elif dig2>dig1:#Mayor 2 que el 1
            num2[0]=dig3
            num2[1]=dig2
            num2[2]=dig1
            print("Caso 3.6")
            print(num2[0]*100+num2[1]*10+num2[2]*1)
    







