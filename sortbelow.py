a=(input("Enter the elements in the list"))
a=[int(n) for n in a.split()]
a.sort()
b=int(input("enter the value below which you want the list"))
a=[i for i in a if i<= b]
print(a)
