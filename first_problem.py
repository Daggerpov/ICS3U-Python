import sys

def mean(list):
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)

def median(list):
    length = len(list)
    list.sort()

    if length % 2 == 0:
        #is even 
        first_median = list[length//2]
        second_median = list[length//2 - 1]
        result = (first_median + second_median) / 2
    else:
        #is odd
        result = list[length//2]
    
    return result

def range_function(list):
    list.sort()
    return list[-1] - list[0]

def mode(list):
    list.sort()
    array = []
    
    for i in range(len(list)):
        array.append(list.count(list[i]))
    
    first_dict = dict(zip(list, array))
    second_dict = {k for (k, v) in first_dict.items() if v == max(array)}
    return str(second_dict)


numbers = []

while True:
    number = input("Please enter a positive integer, quit with '0':")
    
    try:
        int(number)
    except:
        print("Error! Enter a POSITIVE INTEGER please.")
        continue
    
    integer = int(number)

    if integer == 0:
        break
    elif integer < 0:
        continue
    
    numbers.append(integer)
    
mean_result = round(mean(numbers), 1)
print("The mean is: ", mean_result)

median_result = round(median(numbers), 1)
print("The median is: ", median_result)

range_result = range_function(numbers)
print("The range is: ", range_result)

mode_result = mode(numbers)
print("The mode(s) is/are: ", mode_result)


sys.exit()