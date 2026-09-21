# Create a list named products containing at least 6 products names (strings)
products=["Smartphone","Laptop","Washing Machine","Television","Air Conditioner","Bottle"]
print(products)

# create a tuple named sample_prodcut that stores (product_name,price,category)
sample_product=("Apple Macbook Pro M5 chip",227900,"Laptop")
print(sample_product)

# print the 2nd and last product from the products list
print(products[1]) # this will print the second prodct in the list 
print(products[-1]) # this will print the last product in the list 

# 4 Append two new product names to products and then print the updated list
print("Previously Products list",products)
print("Going to add 2 new products through append function ")
products.append("Cup")
print(products)
products.append("Microwave")
print(products)

#Extra :Convert sample prodct into a list , change its price and convert it back to tuple
print("Printing before changing the type to list")
print(type(sample_product))
sample_product=list(sample_product)
print("Printing after changing the type to list")
print(type(sample_product))
print("Before changin price ",sample_product)
sample_product[1]=289000
print("Printing after changing the price")
print(sample_product)

sample_product=tuple(sample_product)
print("printing after changing the type from list to tuple ")
print(type(sample_product))