# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:38:36 2020

@author: Mr. Conrad
"""
import numpy as np
"""
I'm kind of bored at the moment, and this is my first real practice problem
It's on this site called project euler, here's the url
https://projecteuler.net/
After looking at it I think I solve it, so that's a good sign.
I think the biggest problem will be putting it in my Github repo.
The time I made this is at the top of this file
I wonder how much of a gap there'll be between that time and the commit
Let's get started shall we!
"""
print("Solve the following:")
print("""
      If we list all the natural numbers below 10 
      that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
      The sum of these multiples is 23.
      Find the sum of all the multiples of 3 or 5 below 1000.
      """)
#Looking at this I think I just need to make a sum for starters
sum = 0
#Now the problem tells me to list the items then it tells me their sum
#Hmm
#No I don't think that tells me anything
#But I do know what to do now!

#I shall have a number that increments, I'll call it 'i'
i = 0
#Then I increment why by 1 and multiply it by 3 and 5
#If I were to put it into a loop the sequence would go something like this
"""
i * 3 = p (where p is the product)
if p < 1000
then 
sum += p
else move on I guess

then do the above for i and 5
use p again because it's just a place holder for that multiple
after adding p to the sum we increase i by 1

now the loop should end when 
that if condition for p is false for both 3 and 5
since 5 is bigger it'll be false first, when i = 200 to be exact
3 multiplied by 200 is only 600 though, so we'll be adding in multiples of 3 
many more times than multiples of 5
hm
I know what the amount of multiple of 5 there are by  dividing 1000 by 5
I can do the same for 3!
1000 by 3 is 333
so I can just do two separate loops one counting to 200 and 1 counting to 333!
"""
#To make this problem more universal we'll make 1000 variable
#Then we'll use the value to find limits of each multiple
MAX_VALUE = 1000
lim_3 = int(MAX_VALUE / 3)
lim_5 = int(MAX_VALUE / 5)
#I'll also throw the different factors of 3 and 5 in an array and display them
#Since the loops are separate I'll throw them in, sort, then display
factors = np.array([])
#Here's the loop for the multiples of 3
for i in range(1, lim_3):
    p = i * 3                   #Calculate the factor
    factors = np.append(factors, p)       #append the factor to the array
    sum += p                    #add factor to sum


#The loop for multiples of 5
for i in range(1, lim_5):
    p = i * 5
    factors = np.append(factors, p)
    sum += p

print("The desired factors are as follows: ")
#sort the array and output it 
factors = np.sort(factors)
print(factors)

print("\n\nSolution:")
print("The sum of all multiples of 3 and 5 less than 1000 is " + str(sum))






