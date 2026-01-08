import csv

def calculate_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Student Result Analysis\n")

    for row in reader:
        name = row["Name"]
        maths = int(row["Maths"])
        physics = int(row["Physics"])
        chemistry = int(row["Chemistry"])

        total = maths + physics + chemistry
        average = total / 3
        grade = calculate_grade(average)

        print(f"Name: {name}")
        print(f"Total Marks: {total}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
        print("----------------------")
