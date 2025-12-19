def calculate_grade(marks):
    if marks >=90:
        return "A"
    elif marks >=75:
        return "B"
    elif marks >=50:
        return "c"
    else:
        return "fail"
print("student grade management system")
name = input ("enter student name:")
marks = float(input("enter marks(out of 100):"))
grade = calculate_grade(marks)
print("\nStudent Name:" , name)
print("marks:" , marks)
print("grade:" , grade)