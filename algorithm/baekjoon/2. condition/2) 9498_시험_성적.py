import sys

score = int(sys.stdin.readline())
grade = "F"

if score >= 90:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"

sys.stdout.writelines(grade)
