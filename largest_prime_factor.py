# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 09:49:10 2020

@author: Mr. Conrad
"""

print('''The prime factors of 13195 are 5, 7, 13 and 29.
      
What is the largest prime factor of the number 600851475143 ?''')

'''
ALright after looking up the solution for this I see that the example part of 
the question, where it gives me the prime factors of 13195, tells me the answer!
The prime numbers 5, 7, 13 and 29. Multiply these together and you get 13195.
This is prime factorization.
If I divide out the smallest prime factor from any number eventually I'll have
a set of prime numbers that when multiplied together, will give me the original!


That being said, I'm just gonna start over, mostly
'''

import math
#Number given by problem, find the largest prime factor of it
TARGET_NUM = 600851475143

#array for storing prime factors when found
prime_factors = ([])

#function examines target number and divides out each of its prime factors 
def largest_prime_factor ():
    c_num = TARGET_NUM
    global prime_factors
    #loop until return statement is hit within loop conditionals
    while True:
        nxt = next_prime_factor(c_num)
        if nxt < c_num:
            prime_factors.append(nxt)
            c_num //= nxt
        else:
            prime_factors.append(c_num)
            return c_num
    

#Determines next smallest prime factor to be divided out of starting number 
def next_prime_factor(tar):
    #Check if the received number is already 2
    assert tar >= 2
    #check all numbers betweeen 2 and the square root of the recieved number, 
    #inclusive, thus the + 1
    
    #these numbers are all candidates for the next smallest prime factor
    
    #factors after the squareroot aren't relevant 
    #because they are essentially the other half of potential factor pairings
    for x in range(2, int(math.sqrt(tar)) + 1):
        #return the first number that divides our target evenly, 
        #it will always be a prime factor 
        if (tar % x) == 0:
            return x
    #If no factors were found the current target itself is a prime number 
    return tar

#Main body of code
if __name__ == "__main__":
    solution = largest_prime_factor()
    print("The prime factors of " + str(TARGET_NUM) + " are as follows:")
    print(prime_factors)
    print("Solution:")
    print(solution)