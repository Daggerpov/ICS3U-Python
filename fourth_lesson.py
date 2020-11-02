'''1
print(f"{'x':>7} {'y':>10}")
for x in range(10):
      y = 3 * x + (5/4)
      print(f"{x:>7} {y:>10}")
'''
'''2
start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))
increment = int(input("Enter the increment: "))
print(f"{'List value':>14} {'Square':>14}")
for i in range(start, end, increment):
      print(f"{i:>14} {i**2:>14}")
'''
'''3
def getBiggerNumber(x, y):
      if (x - y) >= 0:
            return x 
      else:
            return y 
'''
'''4
def histogram(list):
      for i in range(list):
            print(f"{i * '*'}")
print(histogram(4))'''
'''5
def Cel2Fah(deg_cel):
      return round(deg_cel * 9 / 5 + 32, 1)
'''
'''6
def useFunction(func, num):
      return func(num) ** 2
def addOne(x):
      return x + 1 
'''
'''7
values = tuple(['x', 'y', 'z'])
values.append('asdl;fj')
'''
'''8
numbers = []
num_count = int(input("How many numbers do you want to add to an empty list? "))
for i in range(num_count):
      numbers.append(float(input("Enter a number: ")))
      print(numbers)
print(f"Here is the sorted list: {sorted(numbers)}")
print(f"Here is the sum of that list: {sum(numbers)}")
'''
'''10
list_in_tuple = (['a', 'b', 'c'],)
'''
'''11
def real_number(num):
      try:
            return float(num)
      except ValueError:
            return "You must've made an oopsie"

num = input("Enter a real number: ")
print(real_number(num))
'''
'''12
class Error(Exception):
      #base for other Custom Error classes
      pass

class NegativeValueError(Error):
      #raised when value entered for a mark is under 0.
      pass

class ValueRangeError(Error):
      #raised when value entered for a mark is above the limit (100)
      pass

while True:
      try: 
            mark = int(input("Enter your letter/number mark: "))
            if mark < 0:
                  raise NegativeValueError
            elif mark > 100:
                  raise ValueRangeError
            break
      except NegativeValueError:
            print("This value cannot be negative, try again.")
      except ValueRangeError:
            print("This value exceeds the limit of 100, try again")

print(f"Your mark is: {mark}")
'''