# create a own function
def greet():
    print("Hello, welcome to Python programming!")


# call the function
greet()
# arguments and parameters


def greet(name):
    print(f"Hello, {name}! Welcome to Python programming!")


greet("Alice")
greet("Bob")
greet("Charlie")
# parameters and arguements are the same thing but parameters are used in function definition and arguments are used in function call
# parameters are the variables that are defined in the function definition and arguments are the values that are passed to the function when it is called
# types of functions
# 1. Built-in functions: These are the functions that are provided by Python and can be used without importing any module. Examples include print(), len(), type(), etc.
# 2. User-defined functions: These are the functions that are created by the user to perform specific tasks. We have already seen an example of a user-defined function in the greet() function above.
# 3. Lambda functions: These are anonymous functions that are defined using the lambda keyword. They are typically used for short, simple functions that are not reused elsewhere in the code. for example lambda x: x**2 is a lambda function that takes a single argument x and returns the square of x.
# 1-functions that perform a task
# 2-functions that return a value


def get_greeting(name):
    return f"Hello, {name}! Welcome to Python programming!"


greeting_message = get_greeting("Alice")
print(greeting_message)
file = open("content.txt", "w")# we can write the greeting message to a file using the open function and the write method of the file object
file.write(greeting_message)# we can also write the greeting message to a file using the print function and redirecting the output to a file
file.close()
# by default all fuctions return None if there is no return statement


def greet(name):
    return f"Hello, {name}! Welcome to Python programming!"


print(greet("Alice"))
# next function


def increment(number, by):
    return number+by


result = increment(number=5, by=3)  # keyword arguments
print(result)

# default arguments


def increment(number, num=1):  # optional parameter should comme after required parameter
    return number+num


print(increment(5, 3))
print(increment(5))  # default value of num is 1

# *args,wait,what?


def multiply(x, y):
    return x*y


print(multiply(2, 3))


def multiply(*numbers):  # *args takes variable number of arguments and returns a tuple and used when we don't know how many arguments will be passed to the function
    # we can pass any number of arguments to the function and it will multiply them all together
    result = 1
    for num in numbers:
        result *= num
    return result


print(multiply(2, 3, 4, 5))
# tuples are immutable and we can not change the values of a tuple once it is created but we can create a new tuple by concatenating two tuples together
# lists are mutable and we can change the values of a list after it is created
