#Name: Tran Bao Vu      ID: 2489003
#Step1: Write named constant for 4 prices of coffee and MIN_PRICE for free ship
#Step2: get the customer's coffee quantities
#Step3: Write a program to calculate the price of coffee for each category
#Step4: Write a program to calculate tax and shipping cost
#Step5: Write a program to calculate total cost
#Step6: Display cost of coffee, tax, shipping fee and total cost by using f-string


#Write named constant for 4 prices of coffee and MIN_PRICE for free ship
PRICE_1 = 7.50
PRICE_2 = 8.75
PRICE_3 = 10.00
PRICE_4 = 12.00
MIN_PRICE = 150.00
#Prompt customer for typing the quantity:
Pounds = int(input('How many pounds are you ordering: '))
#This program is to know the price for each category
if Pounds >= 40:
    PRICE = PRICE_1 * Pounds
elif Pounds >= 20:
    PRICE = PRICE_2 * Pounds
elif Pounds >= 10:
    PRICE = PRICE_3 * Pounds
elif Pounds >= 1 and Pounds <= 9:
    PRICE = PRICE_4 * Pounds
#This program is to calculate the tax.
TAX = PRICE * 0.07
#This program is to calculate the shipping
if PRICE > MIN_PRICE:
   SHIPPING = 0.0
else:
   SHIPPING = 1 * Pounds
#This program is to calculate the total cost
TOTAL = PRICE + TAX + SHIPPING

# Display 4 variables:

print(f'Cost of coffee ${PRICE:,.2f}')
print(f'7% sales tax ${TAX:,.2f}')
print(f'Shipping fee ${SHIPPING:,.2f}')
print(f'Total payable ${TOTAL:,.2f}')