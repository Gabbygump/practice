# Comuter Programming 1
# File IO Quiz
#
# Names: Grace Gumpert 

# Answers to 1 - 11
'''

1)D               2)A              3)B and C

4)A and c     5)B             6) B and C 

7)C             8)  C               9)B

10)C                11)A

'''


#12
with open('scrabble_list.txt') as f:
    words = f.read().splitlines()


#13
print (len(words))


#14    
print(words[:10])


#15
count = 0
for w in words:
    if 'e' not in w:
        count +=1
print(count)



#16
with open('begin_and_end_same.txt','w') as f:
    for w in words:
        if w[0] == w[-1]:
            f.write ( w + "\n")
