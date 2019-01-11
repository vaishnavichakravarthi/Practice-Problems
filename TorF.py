a=input("Enter the list A")
b=input("enter the list B")
a=[int(n) for n in a.split()]
b=[int(n) for n in b.split()]

for x in a:
    if x in b:
        vij+=1
    else:
        vij=0
        
if vij>=1:
    print('True')
else :
    print('FAlse')


        
        
