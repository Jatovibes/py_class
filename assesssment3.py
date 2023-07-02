def calculate_grades(grades):
    grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades:
        if grade >= 90:
            grade_count["A"] += 1
        elif grade >= 80:
            grade_count["B"] += 1
        elif grade >= 70:
            grade_count["C"] += 1
        elif grade >= 60:
            grade_count["D"] += 1
        else:
            grade_count["F"] += 1
    return grade_count