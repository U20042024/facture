e = 0
c = 0
q = 0
for i in range(3) :
    print("entrer le nom du client No ",i+1,":")
    o=input()
    n=int(input("entrer le nombre des articles : "))
    for j in range(n) :
        print("donner le prix de l'article No ",j+1,":")
        a = float(input())
        if i==0 :
            x=o
            c=a+a*0.15-a*0.02
            e+=c
        if i==1 :
            d=a+a*0.15-a*0.02
            c+=d
            y=o
        if i==2 :
            e=a+a*0.15-a*0.02
            q+=e
            z=o
print("le total payée par le client ",x,":",e,"DH")
print("le total payée par le client ",y,":",c,"DH")
print("le total payée par le client ",z,":",q,"DH")