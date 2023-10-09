# for loop
# think of range(5) as a collection of five digits in a box: 0,1,2,3,4 starting from a 0
# the FOR loop would iterate through every digit
for number in range(5):
    print("hello")

# for loop & function
def times_two(num):
    result = num * 2
    return result

for number in range(3): # 0,1,2
    calc_res = times_two(number)
    print(calc_res)

for number in range(5): # 0,1,2,3,4
    print("executing FOR LOOP - run No {}".format(number + 1)) # starting from 1 instead of 0 by adding the +1


total = 0
print("*** This statement is OUTSIDE THE LOOP")
print("Before the loop executes, our TOTAL is equal to = ", total, '\n')
print("--------------------------------------------------------")
for number in range(3): # remember --> 0, 1, 2
    print("This is loop execution for digit: " + str(number) + " inside the loop \n")
    print("Updating total... (+ 1) \n")
    total = total + 1 # every time the loop executes, we add 1 to the total
print("--------------------------------------------------------")
print("***This statementWe is OUTSIDE the loop now")
print("The final TOTAL value is: " + str(total))

# A while loop is used to iterate over a block of code or statements as long as the test expression is true.

# Example INFINITE 'while loop' that runs forever until the memory is 'blown'
store_capacity = 10
while store_capacity > 0:
    print('Please come in. Spaces available: ' + str(store_capacity))
# store_capacity = store_capacity - 1 ---> imagine that we forgot to add this logic!!!
print("\nPlease wait for someone to exit the store.")

capacity = 0
while capacity < 10:
    capacity+= 1
    print(capacity)
    print("hello")
#the capacity+=1 means that instead of 0-9 it will be 1-10 so the count begins from 1
#if you add a second print "hello", then this becomes part of the code and prints 10 times also.

store_capacity = 5
while store_capacity > 0:
    print("please come in. Spaces available: " + str(store_capacity))
    store_capacity -= 1
print("\nPlease wait for someone to exit the store.")

# Rewrite this code to use a for loop and the range() function:
print('~' * 0)
print('~' * 1)
print('~' * 2)
print('~' * 3)
print('~' * 4)
print('~' * 5)
print('~' * 6)
print('~' * 7)
print('~' * 8)

for number in range(9):
    print('~' * number)

