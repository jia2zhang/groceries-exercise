# groceries.py
import operator
#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output
### Checkpoint 1 - Printing Products ###
## Print the number of products.
products_count = len(products)

print("--------------")
print("THERE ARE "+str(products_count)+" PRODUCTS")
print("--------------")

## Print the first product.
# print("This is the first product: ", products[0])

## Print the name of the first product.
# prod1 = products[0].get("name")
# print("Name of the first product: ", prod1)

## Print the name of each product.
# for p in products:
#     print(p["name"])

## Print in alphabetical order the name of each product.
# products_sorted = sorted(products, key=operator.itemgetter("name"))
# print("Name of each product by alphabetical order: ")
# for pp in products_sorted:
#     print(pp["name"])

## Print in alphabetical order the name and price of each product.
# products_sorted = sorted(products, key=operator.itemgetter("name"))
# print("Alphabetical order of the name and price of each product: ")
# for np in products_sorted:
#     print("+", np["name"], "("+str(np["price"])+")")

## Print in alphabetical order the name and price of each product, where the price is rounded to two decimal places.
products_sorted = sorted(products, key=operator.itemgetter("name"))
print("Alphabetical order of the name and price of each product rounded to two decimal places: ")
for np in products_sorted:
    print("+", np["name"], "("+str("${0:.2f}".format(np["price"]))+")")


### Checkpoint 2 - Printing Departments ###
## Print the number of unique departments. # Use a "set" because it auto-removes duplicates
unique_dept = set()
for x in products:
    unique_dept.add(x["department"])

print("--------------")
print("THERE ARE", len(unique_dept), "UNIQUE DEPARTMENTS.")
print("--------------")

## Print the name of each unique department in alphabetical order.
# unique_dept = sorted(unique_dept)
# print("The name of each unique department:")
# for ud in unique_dept:
#     print(ud)

## Print in alphabetical order the name of each unique department, as well as the number of products associated with that department, and properly differentiate between "products" plural and "product" singular, depending on how many there are
print("Name of each unique department and number of products in each department:")
unique_dept = sorted(unique_dept)

for ud in unique_dept:
    matched_prods_dept = [p for p in products if p["department"] == ud]
    department_prods_count = len(matched_prods_dept)
    
    if department_prods_count > 1:
        label = "products"
    else:
        label = "product"

    print("+", ud.title(), "("+str(department_prods_count), label+")")

