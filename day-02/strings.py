import sys

text = "Python is awesome"
length = len(text)
print("Length of the string:", length)

text = "vinay"
upper = text.upper()
print("upper is:", upper)

text = "VINAY"
lower = text.lower()
print("upper is:", lower)


text = "gowtham raju"
lower = text.replace("raju", "tarak")
print("upper is:", lower)

text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")

num1 = 3
num2 = 5

def add():
    num = num1+num2
    print(num)

add()

num1 = 3
num2 = 5

def mul(num1,num2):
    num = num1*num2
    print(num)

mul(6,3)


def mul(num1,num2):
    num = num1*num2
    return num

print(mul(7,3))

def mul(num1,num2):
    num = num1*num2
    return num
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print(mul(num1,num2))