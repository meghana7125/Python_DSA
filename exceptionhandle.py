'''x=int(input("enter a number:"))
y=int(input("enter a number:"))
try:
    print(x/y)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
finally:
   print("done")
for i in range(5):
    if i=="meghana":
        break
        print(i)
else:
    print("done")
a=int(input("enter a number:"))
if a<0:
    raise ValueError("number is negative")
while True:
    try:
        num = int(input("Enter a valid integer: "))
        print("You entered:", num)
        break
    except ValueError:
        print("Error: Please enter a valid integer.")'''
l=[1,2,3,4,5,6,7,8,9,10]
try:
    print(l[10])
except IndexError as e:
    print(e)