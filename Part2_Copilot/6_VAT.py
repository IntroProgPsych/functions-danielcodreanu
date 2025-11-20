# Write a function apply_vat(price) that returns the price including 19% VAT.
# Ask the user for a price and print the result.

# Write your code here:

price = int(input())

def apply_vat(price):
    return (price * 19 / 100)

print(apply_vat(price))