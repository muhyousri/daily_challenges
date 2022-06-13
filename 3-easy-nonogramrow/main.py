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

def nonogram(binary):
    count = 0
    array = []
    for i in range(len(binary)):
        if binary[i] == 1:
            count += 1
            print(count)
        elif binary[i] == 1 and binary[i+1] == 0:
            count +=1
            array.append(count)
            count = 0
        elif binary[i] == 1 and i == (len(binary) - 1):
            count +=1 
        
    return array



            
