# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 09:49:10 2020

@author: Mr. Conrad
"""

print('''The prime factors of 13195 are 5, 7, 13 and 29.
      
What is the largest prime factor of the number 600851475143 ?''')

'''
Picking up where I started now that I can generate prime numbers,
I just need to figure out how to use it to find the smallest/largest factor
pairing of whatever number I'm looking for.
'''
import numpy as np
#Number given by problem, find the largest prime factor of it
TARGET_NUM = 13195
#start with the first prime number
prime_nums = np.array([2])

#prime number generation function
def get_next_prime_num():
    #Take one more than the largest prime number in the list as the Current NUMber
    c_num = prime_nums[-1] + 1
    #check if that number is even
    #if it's even then it's already not a prime number
    if (c_num % 2) == 0:
        c_num += 1
        
    #loop through all the relevant checking numbers between our start and end inclusive 
    found = False
    while found != True:
        #check the current number versus all prime numbers generated so far
        if prime_num_compare(c_num): found = True
        else: c_num += 2
        
    return c_num 

#Helper function for prime number generator
def prime_num_compare(c_num):
        for x in prime_nums:
            #check if any of the prime factors are factors of the current number
            #factors in between the prime factors are negligible!
            if (c_num % x) == 0:
                return False
        else:
            return True

#Main body of code
c_factor = prime_nums[0]
#generate prime numbers until you find the smallest prime factor of the target
print("Now searching for smallest prime factor of target number " + str(TARGET_NUM) + "\n\n")
while (TARGET_NUM % c_factor) != 0:
    c_factor = get_next_prime_num()
    #print("Adding " + str(c_factor) + " to list of prime numbers...")
    prime_nums = np.append(prime_nums, c_factor)
    #prime_nums = append_prime_num_arr(prime_nums, c_factor)
    
print("Prime factor found!\n\n")


#use division to obtain the largest factor of the target
large_factor = int(TARGET_NUM / c_factor)
small_factor = c_factor
print("\n\nSmallest prime factor of target number: " + str(small_factor))
print("Other factor in pairing: " + str(large_factor))


#generate all prime numbers between the two known factors
print("Now generating all prime numbers between factor pairing.... \n\n")
while c_factor <= large_factor:
    c_factor = get_next_prime_num()
    #print("Adding " + str(c_factor) + " to list of prime numbers...")
    prime_nums = np.append(prime_nums, c_factor)
    #prime_nums = append_prime_num_arr(prime_nums, c_factor)
    
print("Generation Done!\n")
print("Known prime numbers:")
print(prime_nums)
'''
Now our goal is to check each prime number as a factor 
vs. the target number starting from the largest prime numbers going to the smallest.
eventually it might even hit our smallest prime factor
'''
#create index to be decremented on for search
d = -1
#set the current factor to the end of the prime number list, the largest prime number
c_factor = prime_nums[d]
#check if the current prime number is a factor of the target number
print("\n\nNow locating largest prime factor of target number " + str(TARGET_NUM) + " from available prime numbers:")
while (TARGET_NUM % c_factor) != 0:
    d -= 1
    c_factor = prime_nums[d]
    #print('.', end='')

#once a factor is found display it as the solution
print('')
print("Largest Prime factor found!\n\n")
l_prime_factor = c_factor     
print("Solution:")
print("The largest prime factor of " + str(TARGET_NUM) + " is " + str(l_prime_factor))
