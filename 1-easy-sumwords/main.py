#main challenge
def sum_word(word):
    d = {}
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    num = 1
    for i in alpha:
        d[i] = num
        num += 1
    sum = 0
    for i in word:
        sum += d[i]
    return sum

#optional 1
def words_with_count(count1):
    with open('enable1.txt' , 'r') as list :
        all_words= list.readlines()
        for w in all_words:
            if sum_word(w.split()[0]) == count1:
                return w
#words_with_count(319)

#optional 2
def words_odd_sum():
    with open('enable1.txt' , 'r') as list :
        odd_count = 0
        all_words= list.readlines()
        for w in all_words:
            if sum_word(w.split()[0]) % 2 != 0:
                odd_count += 1
        return odd_count
# words_odd_sum()

#optional 3

def most_common_count():
    with open('enable1.txt' , 'r') as list :
        counts = {}
        all_words= list.readlines()
        for w in all_words:
            a = sum_word(w.split()[0])
            if a not in counts :
                counts[a] = 1
            else :
                counts[a] += 1
        most_common = max(counts.values())
        for key, value in counts.items():
         if most_common == value:
            return key
# most_common_count()


with open('enable1.txt' , 'r') as list :
    all_words= list.readlines()
    for w in all_words:
       a = sum_word(w.split()[0]) 
       for s in all_words:
           n =  sum_word(s.split()[0])
           if a == n :
               if len(s) - len(w) == 11 :
                  print (f'{s} and {w}')






        
            
