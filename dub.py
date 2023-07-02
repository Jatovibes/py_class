def grade_average(grades):
    average = sum(grades) / len(grades)
    rounded_average = round(average)
    if rounded_average >= 90:
        return "A"
    elif rounded_average >= 80:
        return "B"
    elif rounded_average >= 70:
        return "C"
    elif rounded_average >= 60:
        return "D"
    else:
        return "F"