print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Based on a user's order, work out their final bill.
# Use the input() function to get a user's preferences and then
# add up the total for their order and tell them how much they have to pay.

bill = 0

# quanto pagar pelo tamanho

# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25

if size == "S":
    bill =+ 15
elif size == "M":
    bill =+ 20
elif size == "L":
    bill =+ 25
else:
    print("You typed the wrong inputs.")

# quanto adicionar à conta pelo extra de pepperoni
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3

if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or size == "L":
        bill += 3

# quanto adicionar à conta pelo extra de queijo
# Add extra cheese for any size pizza (Y or N): +$1

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")