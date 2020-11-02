'''for i in range(1, 11):
    print(i)

print("\n")

x = 1
while x <= 10:
    print(x)
    x += 1
'''

'''import random
num = random.randrange(45, 50, 5)
print(num)'''

'''num = 2
print(num < 10)
num *= 3
print(num)
print(num > 10)
num //= 4
print(num)'''

'''def doThis(w1, w2):
    w3 = w1 + w2 
    w4 = w2 + w1 
    if w3 == w4:
        print(w3 + w4)
    else:
        print(w4 * 2)

doThis("123", "321")'''

'''myList = (78, 54, 34, 87, 76, 55)
print(myList[0])
print(min(myList))
print(len(myList))'''

'''num = int(input("Enter a number: "))
print("the answer is:", num*3-7)'''

'''choices = [1, 2, 3, 4, 5]
choice = 1
x = 0
while choice in choices:
    choice = int(input("Enter one of the choices: "))
    x += choice
print(x - choice)'''

'''percent = 105
if percent < 0 or percent > 100:
    print("Not a valid mark.")
else:
    print("This is a valid mark.")'''

'''for x in range(1, 3):
    for y in range(10, 2, -2):
        print(y ** x, end=", ")
    print()'''

'''myList = [78, 54, 34, 87, 76, 55]
print(myList[2:5])
myList.sort()
print(myList)'''

'''response = 'yes'
while response == 'yes':
    def drawTree(height):
        startSpaces = height
        for i in range(height + 1):
            print(f"{startSpaces * ' '}{'*' * (i * 2 - 1)}")
            startSpaces -= 1
        print()
    height = int(input("What is the height of a tree, and I will 'draw' it for you? "))

    drawTree(height)

    response = input("Try again? ")

print("Merry Christmas!")'''

'''response = 'yes'
while response == 'yes':
    def drawTree(height):
        startSpaces = height
        for i in range(height + 1):
            print(f"{startSpaces * ' '}{'*' * (i * 2 - 1)}")
            startSpaces -= 1
        print()
    height = int(input("What is the height of a tree, and I will 'draw' it for you? "))

    drawTree(height)

    response = input("Try again? ")

print("Merry Christmas!")'''