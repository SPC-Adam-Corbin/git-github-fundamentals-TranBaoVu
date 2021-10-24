#Name: Tran Bao Vu          ID: 2489003
# Step1:Write named constants for Discount level
# Step2:prompts shoppers for entering the price of a purchase and assign it to RETAIL_PRICE variable
# Step3:prompts shoppers for entering accumulated loyalty points and assign it to LOYALTY_PTS variable
# Step4:Write a program to calculate the discount amount and the reduced prices before taxes
# Step5:Write a program to calculate the taxes and assign it to TAX variable
# Step6:Write a program to calculate total cost of the purchase, assign it to TOTAL variable
# Step7:Display purchase prices, loyalty points, discount amount, reduced price, tax, and total cost,
# reduced price, tax, and total cost Using f-string


# Write named constants for Discount level
DISCOUNT_25 = 0.25
DISCOUNT_20 = 0.20
DISCOUNT_15 = 0.15
DISCOUNT_10 = 0.10
# prompts shoppers for entering the price of a purchase.
RETAIL_PRICE = float(input('Enter price of purchase: '))
# prompts shoppers for entering accumulated loyalty points
LOYALTY_PTS = int(input('Enter number of loyalty points: '))
# Write a program to calculate the discount amount:
if LOYALTY_PTS >= 100:
    DISCOUNT = RETAIL_PRICE * DISCOUNT_25
elif LOYALTY_PTS >= 80 and LOYALTY_PTS <= 99:
    DISCOUNT = RETAIL_PRICE * DISCOUNT_20
elif LOYALTY_PTS >= 60 and LOYALTY_PTS <= 79:
    DISCOUNT = RETAIL_PRICE * DISCOUNT_15
elif LOYALTY_PTS >= 40 and LOYALTY_PTS <= 59:
    DISCOUNT = RETAIL_PRICE * DISCOUNT_10
else:
    DISCOUNT = RETAIL_PRICE * 0.0

#Write a program to calculate the reduced prices before taxes:
REDUCED_PRICE = RETAIL_PRICE - DISCOUNT
# Write a program to calculate the taxes:
TAX = REDUCED_PRICE * 0.07
# Write a program to calculate total cost of the purchase:
TOTAL = REDUCED_PRICE + TAX
#Display variables with f-string:
print(f'Discount amount: ${DISCOUNT:,.2f}')
print(f'Reduced price before sales tax: ${REDUCED_PRICE:,.2f}')
print(f'Sales tax: ${TAX:,.2f}')
print(f'Total cost: ${TOTAL:,.2f}')
