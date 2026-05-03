count = 0
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        count += 1
print(f"Total even numbers are {count}")
# explanation: This code iterates through the numbers from 1 to 9 and checks if each number is even (i.e., divisible by 2 with no remainder). If a number is even, it prints the number and increments the count of even numbers. Finally, it prints the total count of even numbers found in the range.
