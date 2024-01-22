
def case1(list,prom):
    i = 0
    major = 0
    while (i < len(list)):
        if list[i] > prom:
            major += 1
        i += 1
    return major

def case2(list,prom):
    i = 0
    minor = 0
    while (i < len(list)):
        if list[i] < prom:
            minor += 1
        i += 1
    return minor

def case3(list,prom):
    i = 0
    equal = 0
    while (i < len(list)):
        if list[i] == prom:
            equal += 1
        i += 1
    return equal
    

def promedio(v:float, p:int):
    return (v / p )

def alert(h:float,s:int):
    if s == 1:
        if h < 13.2:
            return 'Alerta 1'
        elif h > 16.6:
            return 'Alerta 2'
        else:
            return 'Sin alerta'
    elif s == 2:
        if h < 11.6:
            return 'Alerta 1'
        elif h > 15:
            return 'Alerta 2'
        else:
            return 'Sin alerta'

def data(pacients: int):
    i = 0
    m = 0
    f = 0
    fSuma = 0
    mSuma = 0
    fList = []
    mList = []
        
    while (i < pacients):
        sw = True
        hemo = float(input())
        while (sw):
            sex = int(input())
            if sex != 1 and sex != 2:
                sw = True
            else:
                sw = False
        if sex == 1:
            fSuma += hemo
            f +=1
            fList.append(hemo)
        else:
            mSuma += hemo
            m +=1
            mList.append(hemo)
        i += 1
    fProm = promedio(fSuma,f)
    mProm = promedio(mSuma,m)
    fAlert = alert(fProm,1)
    mAlert = alert(mProm,2)
    fMajor = case1(fList,fProm)  
    mMajor = case1(mList,mProm)
    fMinor = case2(fList,fProm) 
    mMinor = case2(mList,mProm)
    fEqual = case3(fList,fProm) 
    mEqual = case3(mList,mProm)
    print(f"{mProm:.2f} {mAlert}")
    print(f"{fProm:.2f} {fAlert}")
    print(f"{mMajor} {fMajor}") 
    print(f"{mMinor} {fMinor}")
    print(f"{mEqual} {fEqual}")
    
    
def main():
    pacients = int(input())
    data(pacients)

if __name__ == "__main__":
    main()