# string="hi hello "
# w=string.split(" ")
# words=w[-1::-1]
# st=" ".join(words)
# print(st)# hello hi


# str="Ravindra Boga"
# rev=""
# for i in range(len(str)):
#     rev=str[i]+rev
# print(rev) #agoB ardnivaR

str="Boga Ravindra"
word=str.split()
rev=[]
for i in word:
    i=i[::-1]
    rev.append(i)
rev_s=" ".join(rev)
print(rev_s)#agoB ardnivaR




# s="Boga Ravindra"
# word=s.split()
# print(word)
# w1=word.pop(1)
# word.insert(0,w1)
# str=" ".join(word)
# print(str)

# ['Ravindra', 'Boga']
# ['Boga', 'Ravindra']
# Boga Ravindra
