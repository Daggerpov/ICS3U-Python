'''2
while True:
      print("Have a good day")
"""to stop execution of a python file, all you have to do 
is press Ctrl+C in the terminal you're running it on. 
This creates a "KeyboardInterrupt"."""
'''
'''3
print("Please type 'quit' to stop entering words. ")
words = 0
while True:
      word = input("Enter a word: ")
      if word == 'quit':
            break
      words += 1
print(f"You entered {words} words.")
'''
'''4
num_marks = int(input("How many marks do you have? "))
sum = 0
for i in range(num_marks):
      sum += int(input("Enter a mark: "))
print(f"The average is: {round(sum / num_marks, 1)}")
'''
'''5
print(f'{"Number":>10} {"Square":>14}')
for i in range(1, 1001):
      print(f"{i:>10} {i**2:>14}")
'''
'''6
endpoint = int(input("What number do I stop at? "))
print(f"Stop when count is less than {endpoint}")
for i in range(100, endpoint-1, -5):
      print(i)
'''
'''7
number = input("What is your number? ")
sum, digits = 0, 0
for i in number:
      sum += int(i)
      digits += 1
print(f"Your number has {digits} digits and their sum is {sum}. ")
'''
'''8 a)
import random 
random_integers = []
for i in range(10):
      random_integers.append(random.randint(5, 25))
print(random_integers)
'''
'''8 b)
import random 
random_integers = []
x = int(input("What is your first value? "))
y = int(input("What is your second value? "))
for i in range(10):
      random_integers.append(random.randint(x, y))
print(random_integers)
'''
'''9
import random 

while True:
      point = random.randint(1, 6)
      print(f"Your first roll and point value is: {point}")
      tries = 0

      while True: 
            your_point = random.randint(1, 6)
            print(f"Next roll is: {your_point}")
            tries += 1
            if point == your_point:
                  break 

      print(f"It took {tries} times to get your point again.")

      repeat = input("Do you want to play again? (yes/no) ")

      if repeat.lower() != 'yes':
            break
'''

