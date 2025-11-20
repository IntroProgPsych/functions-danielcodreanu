# Write a function describe_number(n) that:

# returns “positive” if n > 0

# returns “zero” if n == 0

# returns “negative” if n < 0

# Ask the user for a number, call the function, and print the message.*

# Write your code here:

n = int(input("type a number:"))

def describe_number(n):
    if n > 0:
        return("positive")
    elif n == 0:
        return("zero")
    elif n < 0:
        return("negative")
    else:
        return("error")
    
print(describe_number(n))
