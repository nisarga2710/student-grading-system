
name=input("Enter student name:")
marks=[]
for i in range(5):
    score = float(input(f"Enter marks for subject{i+1}:"))
    marks.append(score)
total=sum(marks)
average=total/5
if average>=90:
    grade = 'A'
elif average>=75:
    grade = 'B'
elif average >=50:
    grade = 'C'
else:
    grade='Fail'
print("\n---Result---")
print(f"Name:{name}")
print(f"Total:{total}")
print(f"Average:{average}")
print(f"Grade:{grade}")

