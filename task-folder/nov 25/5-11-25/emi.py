# create a function emi with parameters

def emi(a,t,r):#amount,tenure,rate
    r = r / (12 * 100) 
    result = round((a*r*(1+r)**t)/((1+r)**t-1),2)

    return(result)
print(emi(2000,10,2))
