# Q1
for o in range(100):
    output: str = 'o' * 2
    print(output)
# Using a for loop with range in this case means we are multiplying the action 'o' in range of 100,
# so the higher the multiplier the more 'o' characters will output

# Q2
def calculate_vat(amount):
    return amount * 1.2
total = calculate_vat(100)
print(total)
# added 'return' to fix the problem - sends the function result back to caller

#Q1 part 2
for number in range(100):
    output = 'o' * number
    print(output)
