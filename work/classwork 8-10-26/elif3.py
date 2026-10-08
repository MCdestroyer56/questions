tot_sales= float(input('Enter you total sales for the month:'))

if tot_sales > 40000:
   tot_sales = tot_sales/100*15
   print('Bonus earned is:',tot_sales)
   
else:
    tot_sales = tot_sales/100*5
    print('bonus earned is:',tot_sales)
