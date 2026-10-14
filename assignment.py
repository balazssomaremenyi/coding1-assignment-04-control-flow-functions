def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: For loop is looking over the list, goes through all elements it contains, while the if command only allows to work on the numbers which are meeting it's condition, and are strictly bigger than 1. In this case these are two numbers, 2, and 3. These two are the ones passed to add_value. It is important that the for loop does not stop on a value it cannot add through its condition but iteratively looks over the whole list until every condition is met. Whihc would mean it would print 3,4.

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: It would return 3, because the it adds 1 to the defined value, in this case 2 + 1. The most important difference between pring and return is that when the condition of the fuction is met return stops, shots down the fuciton, while a print is a display, it does not stop the loop, it runs iteratively until the defined end conditions ar met or we even could have an infinite loop,
