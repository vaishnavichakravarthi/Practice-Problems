a=input("enter the numbers to be sorted")
a= [int(n) for n in a.split()]
end=len(a)-1
while end!=0: 
    for i in range(end):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    end=end-1
print(a)
        
          
