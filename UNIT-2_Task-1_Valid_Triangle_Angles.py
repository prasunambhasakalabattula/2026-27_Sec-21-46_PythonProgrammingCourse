# Check triangle validity from three angles.
a=int(input("Enter first angle: "))
b=int(input("Enter second angle: "))
c=int(input("Enter third angle: "))

if a>0 and b>0 and c>0 and a+b+c==180:
    print(f"valid triangle(angles={a},{b},{c})")
else:
    print(f"Not a valid triangle(angles={a},{b},{c})")   
