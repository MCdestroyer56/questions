tot_sales= int(input('Enter you total sales for the month:'))

if tot_sales > 40000:
   tot_sales = tot_sales/100*15
   print('Bonus earned is:',tot_sales)
