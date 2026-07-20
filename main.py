'''print("Meghana\nMeghana1")
print(r"\tcurent\new\folder")
# / is escape character
#write a program to find odd and even with function:
n=int(input())
for i in range(1,n+1):
    if n/2==0:
        print("odd")
    else:
        print("even")
# dict
student = {
    "name": "Meghana",
    "gender": "Female",
    "Age": 21,
    "courses": ["python", "java", "Datascience"]
}
print(student)
def count(*args):
    print(type(args))
#count(1,2,3,4,5)
def dicts(**Kwargs):
    print(type(Kwargs))
#dicts(name="Meghana",age=20,gender="female")
def default(gender="female")
x="Meghana"
x=x[1:-1]
x=x[::-1]
print(x)
while True:
    print("h1")'''
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num + 1):
    sum += i
print("Sum =", sum)