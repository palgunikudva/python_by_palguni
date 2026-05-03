print("sending a message")
for i in range(1, 4):
    print("Attempt", i, (i)*"*")
    print("I love you so much python")
    # range() function is used to generate a sequence of numbers. It takes three arguments: start, stop, and step. The start argument is the number to start the sequence from, the stop argument is the number to stop the sequence at (exclusive), and the step argument is the number to increment the sequence by. If the step argument is not provided, it defaults to 1.
    # in the above example, the range function generates a sequence of numbers from 1 to 3 (inclusive) and the loop iterates over each number in the sequence. The loop will execute the block of code inside it for each number in the sequence, which will print the attempt number and a message.
    # range(1,4) generates a sequence of numbers from 1 to 3 (inclusive) and the loop iterates over each number in the sequence. The loop will execute the block of code inside it for each number in the sequence, which will print the attempt number and a message.
    # range(1,10,2) generates a sequence of numbers from 1 to 9 (inclusive) with a step of 2, which will be 1, 3, 5, 7, 9.
for i in range(1, 10, 2):
    print("*****"*i)
# For else loop is used to execute a block of code after the loop has finished iterating over all the items in the sequence. The else block will be executed only if the loop was not terminated by a break statement.
successful = False
for i in range(3):
    print("Attempt", i+1)
    if successful:
        print("Attempt", i+1, "successful")
        break
else:
    print("Attempted 3 times,failed")
# nested loop is a loop inside another loop. The inner loop will be executed for each iteration of the outer loop.
for x in range(5):  # outer loop
    for y in range(3):  # inner loop
        print(f"({x},{y})")
# f strings are a way to format strings in python. They are denoted by an f before the opening quotation mark and allow you to embed expressions inside string literals using curly braces {}. The expressions inside the curly braces will be evaluated at runtime and their values will be inserted into the string.
