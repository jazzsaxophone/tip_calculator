# create a tip calulator
# calculator will take customer input and output the price in to a float
# input is saved into a variavle called meal_price
# a statment is printed out confirming the price

# creat a variable that will take the cost of the meal
# cost should be in float form
meal_price = float(input("What was your total bill today? "))
print()

print()

# update total price with tax
tax = 10/100
meal_tax = meal_price + tax
print(f"The total cost of your meal, plus tax is: ${meal_tax}")
print()

# create a variable to take input to see if guest want to leave a tip
# variable should be a string
tip = str(input("Will you be leaving a tip? (Please enter 'yes' or 'no')"))
print(tip)

# use a if, elif, and else statment to determine if guest wants to leave a tip
# print total for guest

if tip == "yes":
    tip_amt = float(input("How much would you like to tip?"))
    print(meal_tax+tip_amt)
elif tip == "no":
    print(f"{meal_tax+tip_amt}")

# input taken from customer on how many ways to split the bill
# use this equation to calulate the meal_price/bill_split
total_paying = int(input("How many ways would you like to split the bill? "))
print()

# meal_price/total_paying will be saved into a variable called bill_split
bill_split = meal_price/total_paying

# have a statment printed out with new price after each person splitting
print(f"Your new total for all {total_paying} of the guest(s) is $ {bill_split} each.")
print("Thank you for shopping with us, please come agian")
