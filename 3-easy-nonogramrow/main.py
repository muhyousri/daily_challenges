"""
 binary array is an array consisting of only the values 0 and 1. Given a binary array of any length, return an array of positive integers that represent the lengths of the sets of consecutive 1's in the input array, in order from left to right.

nonogramrow([]) => []
nonogramrow([0,0,0,0,0]) => []
nonogramrow([1,1,1,1,1]) => [5]
nonogramrow([0,1,1,1,1,1,0,1,1,1,1]) => [5,4]
nonogramrow([1,1,0,1,0,0,1,1,1,0,0]) => [2,1,3]
nonogramrow([0,0,0,0,1,1,0,0,1,0,1,1,1]) => [2,1,3]
nonogramrow([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]) => [1,1,1,1,1,1,1,1]

As a special case, nonogram puzzles usually represent the empty output ([]) as [0]. If you prefer to do it this way, that's fine, but 0 should not appear in the output in any other case."
"""

def nonogramrow(binary):
    count = 0
    array = []
    for i in range(len(binary)):
        if binary[i] == 1:
            if i < len(binary) - 1:
              count += 1
            elif i == len(binary) - 1:
               count += 1 
               array.append(count)
        elif binary[i] == 0 and i != 0 :
            if binary[i-1] == 1:
               array.append(count)
               count = 0
        
    return array


#nonogramrow([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
            
