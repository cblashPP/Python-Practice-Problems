# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:38:36 2020

@author: Mr. Conrad
"""
"""
Tried my solution on euler and found it wasn't correct :(
luckily I listed out all the factors going into the final sum!
I see now that there are duplicate factors being added
So all I need to do is 
remove the dupes from the array
and add each element to sum after doing so
"""

'''
Here's how I can remove those dupes
They occur when the factor is divisible by 3 and 5 
but this really just means it's a multiple of 15!
I can just make some sort of function that goes through the completed array
and removes at least one copy of each factor of 15
Alternatively I can have one of the factor loops, probably 5, the shorter one
conditionally check if p is divisible by 15
Eventually we'll choose one of these two methods that has the shorter run time
Specifically as the MAX_VALUE approaches infinity
Scalability everybody!
'''

#Let's filter the array on this attempt just because it sounds more difficult
import numpy as np
print("Solve the following:")
print("""
      If we list all the natural numbers below 10 
      that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
      The sum of these multiples is 23.
      Find the sum of all the multiples of 3 or 5 below 1000.
      """)
#Looking at this I think I just need to make a sum for starters
sum = 0
#To make this problem more universal we'll make 1000 variable
#Then we'll use the value to find limits of each multiple
MAX_VALUE = 1000
lim_3 = int(MAX_VALUE / 3)
lim_5 = int(MAX_VALUE / 5)
lim_15 = int(MAX_VALUE / 15)
#I'll also throw the different factors of 3 and 5 in an array and display them
#Since the loops are separate I'll throw them in, sort, then display
factors = np.array([])

#Loop for the multiples of 3
for i in range(1, lim_3):
    p = i * 3                   #Calculate the factor
    factors = np.append(factors, p)       #append the factor to the array


#The loop for multiples of 5

for i in range(1, lim_5):
    p = i * 5
    factors = np.append(factors, p)
    
'''
So here's what I'm thinking
I read through an online tutorial on filtering NumPy arrays
I can just make a loop that sets a false boolean on all the multiples of 15
Then I can add them back in on a 4th loop
hmm
but now that I think about having so many different loops is probably super slow
maybe I'll just go with plan b and just set a conditional in the shorter loop
For now I'll implement the filtering method for my own experience
Then come back and address another issue I've found
'''

#lets set the condition to make the multiples of 15 go to false
factor_15 = factors % 15 != 0 

#one line sets up the new array
factors = factors[factor_15]

#now we add back in the factors of 15
for i in range(1, lim_15):
    p = i * 15
    factors = np.append(factors, p)


print("The desired factors are as follows: ")
#sort the array and output it 
factors = np.sort(factors)
print(factors)

#now we need to add the factors together
for x in factors:
    sum += x


print("\n\nSolution:")
print("The sum of all multiples of 3 and 5 less than 1000 is " + str(sum))






