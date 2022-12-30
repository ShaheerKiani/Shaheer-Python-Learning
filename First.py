#Q2
Length = int(input("Enter length of rectangle: "))
Width = int(input("Enter width of rectangle: "))

Area = Length * Width
Perimeter = Length + Length + Width + Width

print("The area is", Area)
print("The perimeter is", Perimeter)

#Q3
Num = int(input("Enter a number: "))

if Num % 2 == 0:
    print("Your number is even")
elif Num % 2 == 1:
    print("Your number is odd")

#Q4
Length = int(input("Enter length: "))

Volume = Length**3
SurfaceArea = (6*Length)**2

print("The volume is", Volume)
print("The Surface Area is", SurfaceArea)