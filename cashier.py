#cashier_task_14

print('=== Album Store Nota ===')

item_name = input('input item name :')
price = float(input('input price item :'))
quantity = float(input('input quantity of the item :'))
total_money = float(input('input total many you pay :'))
re_money = total_money - quantity * price

#Nota

teks =f'''
==========================
    Nota of the shop
==========================
- Your item name        :{item_name}
- Your item price       :{price}
- Your item quantity    :{quantity}
- Your total of money   :{total_money}
- Your total of channge : IDR{re_money}
===========================
'''
#open and make new file txt

file = open('nota.txt','w')

#writing into file
file.write(teks)