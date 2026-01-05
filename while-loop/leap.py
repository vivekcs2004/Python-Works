year = 1800

while(year<=2025):

    if (year%100==0 and year%400==0) or (year%4==0 and year%100!=0):
         print(year)
    
    year+=1