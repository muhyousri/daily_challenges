"""
Given a lowercase letter and a number between 0 and 26, return that letter Caesar shifted by that number. To Caesar shift a letter by a number, advance it in the alphabet by that many steps, wrapping around from z back to a:

warmup('a', 0) => 'a'
warmup('a', 1) => 'b'
warmup('a', 5) => 'f'
warmup('a', 26) => 'a'
warmup('d', 15) => 's'
warmup('z', 1) => 'a'
warmup('q', 22) => 'm'
Hint: taking a number modulo 26 will wrap around from 25 back to 0. This is commonly represented using the modulus operator %. For example, 29 % 26 = 3. Finding a way to map from the letters a-z to the numbers 0-25 and back will help.

Challenge
Given a string of lowercase letters and a number, return a string with each letter Caesar shifted by the given amount.

caesar("a", 1) => "b"
caesar("abcz", 1) => "bcda"
caesar("irk", 13) => "vex"
caesar("fusion", 6) => "layout"
caesar("dailyprogrammer", 6) => "jgorevxumxgsskx"
caesar("jgorevxumxgsskx", 20) => "dailyprogrammer"
Hint: you can use the warmup function as a helper function.
"""


# Function to shift
def shift(a,n):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    old = alph.find(a)
    if old + n >= len(alph):
        index = ((old+n) - 26) % 25
        new = alph[index]
    else:
        new = alph[old+n]

    return new 


# Main function
def caesar(str,num):
    new_string = ''
    for i in str :
        new_string += shift(i,num)
    
    return new_string
    

    
