greatest = 0
for num1 in range(100,1000):           #finds product of all 3 digits numbers
    for num2 in range(100,1000):
        product = num1*num2
        if str(product) == str(product)[::-1] and product>greatest:  #checks if product is palindrome
            greatest = product
        
    

print(greatest)
#ans 906609
