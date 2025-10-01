import pandas as pd


students = {
    "Name": ["Danyal", "Arham", "Moosa", "Haseeb", "Hanzla"],
    "Age": [22, 25, 28, 23, 26],
    "Marks": [85, 90, 95, 88, 92]
}

df = pd.DataFrame(students)


print("Full Data:")
print(df)


print("\nStudents with Marks > 90:")
print(df[df["Marks"] > 90])


grades = []
for marks in df["Marks"]:
    if marks > 90:
        grades.append("A")
    elif marks >= 80:
        grades.append("B")
    else:
        grades.append("C")

df["Grade"] = grades

print("\nWith Grade Column:")
print(df)