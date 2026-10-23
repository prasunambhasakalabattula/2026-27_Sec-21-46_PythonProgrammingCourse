marks = int(input("Enter the marks out of 100: "))

if marks >= 90:
    print(f"Grade: A(marks={marks})")
elif marks >= 80:
    print(f"Grade: B(marks={marks})")
elif marks >= 70:
    print(f"Grade: C(marks={marks})")
else:
    print(f"Grade: D(marks={marks})")