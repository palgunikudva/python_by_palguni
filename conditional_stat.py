temperature = 15
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("done")
# if statement is used to execute a block of code only if a certain condition is true. If the condition is false, the block of code will be skipped.
# elif statement is used to check multiple conditions. If the first condition is false, the next condition will be checked, and so on. If all conditions are false, the else block will be executed.
# ternary operator is a one-line if statement that assigns a value to a variable based on a condition. The syntax is: variable = value_if_true if condition else value_if_false
age = 6
message = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(message)
# logical operators are used to combine multiple conditions. The three logical operators are: and, or, not
# and operator returns true if both conditions are true
# or operator returns true if at least one of the conditions is true
# not operator returns the opposite of the condition
high_income = False
good_credit = True
student = False
# if high_income or good_credit:
#  print("Eligible for loan")
# else:
# print("Not eligible for loan")
# not operator example
# if not student:
# print("eligible")
# else:
# print("not eligible")
if (high_income or good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
# short circuit evaluation is a programming technique where the evaluation of a logical expression is stopped as soon as the result is determined. For example, in the expression "A and B", if A is false, then the entire expression will be false regardless of the value of B, so B will not be evaluated. This can improve performance by avoiding unnecessary calculations.
high_income = False
good_credit = True
student = False
if high_income and good_credit or not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
# chaining comparison operators allows you to compare multiple values in a single expression. For example, you can check if a number is between two values using the syntax: lower_bound < variable < upper_bound
age = 22
# 18<=age<65 is the same as age>=18 and age<65
if 18 <= age < 65:
    print("eligible")
