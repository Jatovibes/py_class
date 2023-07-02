def convertkelvin_to_fahrenheit(value):
    assert value >= 0, 'Colder than zero'
    result= ((value - 273.15) * (9/5)) + 32
    return result

k_temp = [273,12.5, 33.3, 7.9, 22.89]

f_temp = [convertkelvin_to_fahrenheit(temp) for temp in k_temp]

print(f_temp)

    
    
