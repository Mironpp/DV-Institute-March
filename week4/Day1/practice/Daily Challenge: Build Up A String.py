
import random

askUser = input("Please give me a 10 letters \"string\":")
length_answer = len(askUser)

if length_answer >10 :
    print ("string too long")

elif length_answer <10:
    print("string not long enough")

last_chr = askUser[-1]
print("Last character:" ,last_chr)

emptyy = " "
for letter in askUser :
    emptyy = emptyy + letter 
    print(emptyy)

arr = list(askUser)
print(arr)

random.shuffle(arr)
print(arr)

x = "".join(arr)

print(x)












