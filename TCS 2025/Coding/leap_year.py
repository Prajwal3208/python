"""there are 3 conditions for the leap year 
1. year should be divisible by 4
2.yaer should be divisible by 400
3. year should not be divisible by 100
     """

year = 1996

if (year%4 == 0 and year%100 !=0) or (year%400 == 0):
    print(True)
else:
    print(False)