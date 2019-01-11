input_number = input("Enter a list element separated by space ")
list  = input_number.split()
print("Calculating product of element of input list")
product = 1
for num in list:
    product *= int (num)
print("Product = ",product)
