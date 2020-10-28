# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 08:54:30 2020

@author: Mr. Conrad
"""

print('''A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.''')


'''
This problem screams at me see what 999 * 999 is and then just count backwards
there are a bunch of ways I can do this.
I remember from a Google interview I did that dividing out 10s from a big boy
can give you each digit
In actual coding the modulus can literally give me the digit, as opposed to
dividing by ten, looking at the decimal and taking that.
'''

'''
Now that I have a method for identifying a palindromic number,
I now need to figure out how I'm gonna find the biggest one,
but also doing so fast, without too much compute
I have a brute force strategy so I guess I'll start with that.
'''
'''
All I need to do is look at the product for each 3 digit number
100 to 1000 modulo the numbers out of the product and see if they palindrome
I can speed this process up by starting at 999 and going down, instead of starting 
at 100 and going up
'''

def calc_products():
    factor1 = 999
    factor2 = 999
    while factor1 >= 100:
        while factor2 >= 100:
            product = factor1 * factor2
            if find_palindrome(product):
                print("Factor 1 = " + str(factor1))
                print("Factor 2 = " + str(factor2))
                return product
            factor2 -= 1
        factor1 -= 1
    
#this function will look at each product to see if their a palindrome
def find_palindrome(p):
    num = p
    #this will hold each digit
    dig_arr = []
    while num > 0:
        dig = num % 10 
        dig_arr.append(dig)
        num //= 10
    #now that we have the array we compare the elements
    length = len(dig_arr)
    #TODO: find a way to have the array read in two halves and compare them
        
    