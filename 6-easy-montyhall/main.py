"""
For the purpose of today's challenge, the Monty Hall scenario goes like this:

There are three closed doors, labeled #1, #2, and #3. Monty Hall randomly selects one of the three doors and puts a prize behind it. The other two doors hide nothing.
A contestant, who does not know where the prize is, selects one of the three doors. This door is not opened yet.
Monty chooses one of the three doors and opens it. The door that Monty opens (a) does not hide the prize, and (b) is not the door that the contestant selected. There may be one or two such doors. If there are two, Monty randomly selects one or the other.
There are now two closed doors, the one the contestant selected in step 2, and one they didn't select. The contestant decides whether to keep their original choice, or to switch to the other closed door.
The contestant wins if the door they selected in step 4 is the same as the one Monty put a prize behind in step 1.
Challenge
A contestant's strategy is given by their choices in steps 2 and 4. Write a program to determine the success rate of a contestant's strategy by simulating the game 1000 times and calculating the fraction of the times the contestant wins. Determine the success rate for 

Alice chooses door #1 in step 2, and always sticks with door #1 in step 4.


"""
import random

first = 1
sucess = 0
faliure = 0


for i in range(1000):
    monty_door = random.randint(1, 3)
    if monty_door == first:
     opened = random.randint(2, 3)
     second = 1
     if monty_door == second:
        sucess+=1
     else:
         faliure+=1
    elif monty_door == 2:
            opened = 3
            second =1 
            if monty_door == second:
                sucess+=1
            else:
                faliure+=1
    elif monty_door ==3:
       opened = 2
       second = 1
       if monty_door == second:
        sucess+=1
       else:
         faliure+=1

rate = (sucess/1000)*100
print(f'{rate}%')








    
    