# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:38:36 2020

@author: Mr. Conrad
"""
"""
Alright let's clean this up!
Also I'm gonna start punctuating these comments.
Makes them more readable. :)
Anyway
Here's what I know.
I can avoid duplicate factors much easier by
just using a conditional statement in one of the loops.
Preferebly this'll be in the 5 factor loop since it's shorter.
Also, I've found that 999 is not getting added into the array or sum.
I can either adjust the for loop for 3 and keep it simple.
Or I can do the longterm fix of checking my factor limits with conditional statements.
I'll do that second one.
"""

#Let's filter the array on this attempt just because it sounds more difficult
import numpy as np
print("Solve the following:")
print("""If we list all the natural numbers below 10 
that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.""")
#Looking at this I think I just need to make a sum for starters
sum = 0
#To make this problem more universal we'll make 1000 a constant changeable by the programmer
#Then we'll use the value to find limits of each multiple
MAX_VALUE = 1000

#Values of the limits are set based on division
#conditionals are used avoid problems with looping due to remainders
if MAX_VALUE % 3 == 0: 
    lim_3 = int(MAX_VALUE / 3) 
else: lim_3 = int(MAX_VALUE / 3) + 1

if MAX_VALUE % 5 == 0: 
    lim_5 = int(MAX_VALUE / 5)    
else: lim_5 = int(MAX_VALUE / 5) + 1

#UPDATE!: I realized what I just did was just rounding the quotient up!
#So I'm gonna just import math and use the round-up func from that
import math
lim_3 = math.ceil(MAX_VALUE / 3)
lim_5 = math.ceil(MAX_VALUE / 5)

#I'll also throw the different factors of 3 and 5 in an array and display them
#Since the loops are separate I'll throw them in, sort, then display
factors = np.array([])

#Loop for the multiples of 3
for i in range(1, lim_3):
    p = i * 3                             #Calculate the factor
    factors = np.append(factors, p)       #append the factor to the array
    sum += p                              #add that factor into the sum


#The loop for multiples of 5

for i in range(1, lim_5):
    p = i * 5
    #check if the factor is already in the array, 15 is also a factor of 3
    if p % 15 != 0:
        factors = np.append(factors, p)
        sum += p
    

print("The desired factors are as follows: ")
#sort the array and output it 
factors = np.sort(factors)
print(factors)


print("\n\nSolution:")
print("The sum of all multiples of 3 and 5 less than 1000 is " + str(sum))







