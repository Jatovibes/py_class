def grade_average(grades):
    average=sum(grades)/len(grades)
    if average >=90:
        return "A"
    elif average >=80:
        return "B"
    elif average >=70:
        return "C"
    elif average >=60:
        return "D"
    else:
        return "F"
    
 
    





