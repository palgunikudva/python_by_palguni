# while loop
number = 100
while number > 0:
    print(number)
    number //= 2
# while loop is used when we don't know how many times we want to execute a block of code. It will continue to execute as long as the condition is true. In this example, the loop will continue to execute until the number becomes 0 or negative.
#command = ""
# command.lower() != "quit":
    #command = input(">")
    #print("ECHO", command) # echo is a command that repeats what you say. In this example, the loop will continue to execute until the user types "quit". The input function is used to get user input, and the loop will print "ECHO" followed by the user's input until they type "quit".
# In this example, the loop will continue to execute until the user types "quit". The input function is used to get user input, and the loop will print "ECHO" followed by the user's input until they type "quit".
# while loop can also be used with else statement. The else block will be executed when the condition becomes false.
# infine loop
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
