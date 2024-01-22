from os import system
system("cls")

print("Digite un valor mayor a 20: ")
n=int(input())
a=0
for i in range(20,n+1):
    if(a==0):
        print(f"par {i}")
        a=1
    elif(a==1):
        print(f"impar {i}")
        a=0
    
    
        
    
    
    
