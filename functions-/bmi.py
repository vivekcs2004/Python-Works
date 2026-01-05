def bmi(weight_in_kg,height_in_cm):
    result = round(weight_in_kg/((height_in_cm/100)**2),2)

    return(result)

print(bmi(72,179))