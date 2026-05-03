print("hello")
# **kwargs is used to pass a variable number of keyword arguments to a function and it returns a dictionary of the keyword arguments passed to the function


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# this prints the keyword arguments passed to the function in the form of a dictionary and we can access the values of the dictionary using the keys
print_info(name="palguni", age=25, city="Karkala")
#print(print_info.name)  # this will give an error because print_info is a function and it does not have an attribute called name but we can access the values of the dictionary using the keys
# how to access the values of the dictionary using the keys
info = print_info(name="palguni", age=25, city="Karkala")
print(info)  # this will print None because the function does not return anything and by default all functions return None if there is no return statement but we can access the values of the dictionary using the keys
# this will print the keyword arguments passed to the function in the form of a dictionary and we can access the values of the dictionary using the keys
print_info(name="palguni", age=25, city="Karkala")
# how to access only the name from the dictionary


def print_info(**kwargs):
    # this will get the value of the key "name" from the dictionary and return it
    name = kwargs.get("name")
    print(f"Name: {name}")


# this will print the name from the dictionary
print_info(name="palguni", age=25, city="Karkala")
