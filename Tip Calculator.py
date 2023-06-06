print('****** WELCOME TO ANSANKA HOTEL ******')
food_charge = int(input('Enter the amount of meal purchased: '))
percent_tip = 18/food_charge * 100 
sales_tax = 7/food_charge * 100
print('Percent tip amount: ', percent_tip)
print('Sales tax amount: ', sales_tax)
total_charge = food_charge + percent_tip + sales_tax
print('Total amount of food charge is = ', int(total_charge))