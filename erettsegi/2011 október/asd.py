def honap2(a):
    lista=[31,59,90,120,151,181,212,243,273,304,334,365]
    db=0
    for i in lista:
        db+=1
        if a<=i:
            return db
print(honap2(364))
