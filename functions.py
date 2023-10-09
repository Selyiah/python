# functions
def hello():
    print("hello")
    print("hello")
    print("hello")
    print("hello")


hello()
hello()


# () this means calling the function (calling the function in this case hello) and it will repeat it

def bye(name):
    print("bye,", name)
bye("maria")
bye("kim")
bye("olya")

# functions part 2
def some_function(name, job="developer"):
    print(name, "is a", job)
some_function("Fiona")
some_function("Fiona", "manager")

# return value

# Using return statement
def sum(x, y):
    return x + y
result = sum(10, 15)
print("result is: {}".format(result))

# Without return statement
def sum(x, y):
    print(x + y)
result = sum(10, 15)
print("result is: {}".format(result))

# function to the return the area of a circle
def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return area
area = circle_area(9)
print(area)

def days_in_hours(days):
    hours = days * 24
    return hours
print(days_in_hours(10))

# for loop & function combination
def times_two(num):
    result = num * 2
    return result
for number in range(3): # 0,1,2
    calc_res = times_two(number)
    print(calc_res)
