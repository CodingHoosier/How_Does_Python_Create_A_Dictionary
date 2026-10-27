# https://www.youtube.com/watch?v=YXuRcQntpbw
# How Does Python Create A Dictionary?
# Let's use a dictionary to store 
#  car brands and models.
# The keys are the car models, 
#  and the values are the brands.
# The dictionary is created 
#  using curly braces.
# The key and value pairs 
# are separated by a colon.
car = {"Camaro":"Chevrolet",
       "Mustang":"Ford",
       "Civic":"Honda"}
print(f"The car dictionary is of type: {type(car)}")
# Perform a lookup using the key
myCar = car["Civic"]
print(f"My car is made by {myCar}")
# What if the key doesn't exist?
#  Let's try it.
try:
    myCar = car["Corvette"]
    print(f"My car is made by {myCar}")
except KeyError as ex:
    # We end up here 
    #  because the key doesn't exist
    print(f"KeyError: {ex}")    
# Create a dictionary using the dict() constructor
food = dict(fruit="apple", 
            vegetable="carrot", 
            grain="rice")
print(f"The food dictionary is of type: {type(food)}")
print(f"The food dictionary is: {food}")
# Add a key/value pair
#  to the dictionary
food["protein"] = "chicken"
print(f"The food dictionary after addition is: {food}") 
