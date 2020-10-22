# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 09:49:10 2020

@author: Mr. Conrad
"""
'''
Been a while since I did one of these
Once you start something it's always hardest to remain consistent.
I've come back though, which is huge considering,
almost 1 million people completed 'multiples of 3 and 5' 
but only half that many completed 'largest prime factor,' this problem
'''

print('''The prime factors of 13195 are 5, 7, 13 and 29.
      
What is the largest prime factor of the number 600851475143 ?''')

'''
off the top of my head I know the first few prime numbers
I'll initiate an array with those first few and continue generating them from there
but I only need to generate a certain amount of these factors
normally the largest, whole number, factor is paired with the number 2
eg. 2 and 50 make 100,  2 is the smallest factor and 50 the largest
but this only applies to even numbers.
I'd then try 3 as a factor if it's odd then 5 and so on,
Through my prime numbers until I get the smallest prime factor.
Then, knowing the smallest prime factor, I also know the largest non-prime factor
I can then generate prime numbers between that smallest prime factor and largest non-prime
then test them against my number
'''
#start with the first prime number
prime_nums = [2]

def prime_number_gen(num_arr, end_point):
    #Take one more than the largest number in the list as the Current NUMber
    c_num = num_arr[-1] + 1
    #check if that number is even
    #if it's even then it's already not a prime number
    if (c_num % 2) == 0:
        c_num += 1
        
    #loop through all the relevant checking numbers between our start and end inclusive   
    while c_num <= end_point:
        #check the current number versus all prime numbers generated so far
        found = prime_num_compare(num_arr, c_num)
        if found:
            print("Adding " + str(c_num) + " to the array...")
            num_arr.append(c_num)
            print(num_arr)
        c_num += 2
        
    return num_arr
'''
So I thought it over for a long time and I couldn't find a way around a nested loop
and when I tried to put them together in one function it was more or less falling appart.
I figured, if all I'm checking if a factor exists in the array I could go with a boolean,
And it's easier to have it gen'd by another function 
than to switch it back and forth each iteration in a mess of loops
Makes more readable
'''  
def prime_num_compare(num_arr, c_num):
        for x in num_arr:
            #check if any of the prime factors are factors of the current number
            #factors in between the prime factors are negligible!
            if (c_num % x) == 0:
                return False
        else:
            return True

#example run of generating all prime numbers between 2 and 21, inclusive
prime_nums = prime_number_gen(prime_nums, 21)