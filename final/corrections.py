"""
1. Read through and try the following program.
2. Correct any mistakes to get it running properly (basically level 1)
3. Document and comment to make it more readable and understandable (basically level 2)
    - write an overall comment that describes the purpose of this program
    - change the variable names, possibly input and print statements and comment BLOCKS of code
4. Improve the efficiency of the code so it runs faster and properly (basically level 3)
    - rewrite parts of the code to make it more efficient (hint: look at the IF statements!)
5. Add functionality or improve the overall code structure (basically level 4)
    - Change code to make use of definitions, exception handling, and/or lists to improve the overall code structure
    - Add ONE feature such as allowing for entry of ANY number of candidates or if there is a tie for the winner, state all the winners who tied
"""
'''
The purpose of this program is to simulate an election process between 4 
candidates. The user will be able to input who they're voting for until they
decide to stop. Then, the results will be tallied up to find the total and 
the winner(s). 
'''

import operator

winners_list = []
def find_winners(candidates):
    #finding the max value of the values in the dictionary of candidates
    highest = max(candidates.values())

    #list comprehension to add any values that meet a condition to this 
    #list, iterating through the items in the candidates dictionary
    winners_list = [k for k, v in candidates.items() if v == highest]

    #returns the list just made but separated by ", " between each item
    #in the format of a string
    return ', '.join(winners_list)
        

#I wanted to create a dictionary so I could refer back 
#to the candidate who got a certain number of votes (max)
candidates = dict({
        "Mickey Mouse": 0, 
        "Donald Duck": 0, 
        "Minnie Mouse": 0, 
        "Goofy": 0
    })

while True:
    #printing out all candidates and their current # of votes
    print ()
    print ("The presidential candidates are:")
    print (f"1. Mickey Mouse: {candidates.get('Mickey Mouse')} votes")
    print (f"2. Donald Duck: {candidates.get('Donald Duck')} votes")
    print (f"3. Minnie Mouse: {candidates.get('Minnie Mouse')} votes")
    print (f"4. Goofy: {candidates.get('Goofy')} votes")
    print ("Type 0 to quit")
    
    #based on the user's input number, it'll correlate to a candidate
    user_vote = int(input("Enter a number for who you're voting: "))

    #then, it'll add 1 to whoever's value in the candidates dictionary
    if user_vote == 0:
        break
    elif user_vote == 1:
        candidates["Mickey Mouse"] += 1
    elif user_vote == 2:
        candidates["Donald Duck"] += 1
    elif user_vote == 3:
        candidates["Minnie Mouse"] += 1
    elif user_vote == 4:
        candidates["Goofy"] += 1
    else:
        #I want to have their input disregarded and let them try again
        print ("Invalid input, please try again. ")
        continue

#this takes the sum of the values in the dictionary then prints it out
sum = candidates["Mickey Mouse"] + candidates["Donald Duck"] + candidates["Minnie Mouse"] + candidates["Goofy"]
print (f"\nThe total amount of votes is {sum}")

#printing out the result of calling the find_winners function in a message
print(f"Here are your winner(s): {find_winners(candidates)}")