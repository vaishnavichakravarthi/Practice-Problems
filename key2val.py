dict={'a':"Speckbit", 'b':"World", 'c':"Quiet"}
a=dict.items()
str=input("input the the value you want to search")
for i in a:
    if str==i[1]:
        print(i[0])
        
        
