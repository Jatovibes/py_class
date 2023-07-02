def convert_to_f(value):
    result= (value * (9/5)) + 32
    return result

c_temp = [12.5, 33.3, 7.9, 22.89]

f_temp = [convert_to_f(temp) for temp in c_temp]

print(f_temp)