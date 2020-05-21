#Try to guess a random 3 digit number within 4 guesses. The digits will not be repeated.
import random
int_list = list(range(10))
random.shuffle(int_list)
if(int_list[0]==0):
    res="".join(map(str,int_list[1:4]))
else:
    res = "".join(map(str,int_list[0:3]))
#print(res)
cow=bull =0

def check(inp,res):
    global cow,bull
    for i in range(3):
        if (inp[i] == res[i]):
            bull +=1
        elif inp[i] in res:
            cow +=1
    if bull==3:
        print("You guessed it right. You have won!!!")
        exit(0)
    elif cow ==0 and bull==0:
        print("No match")
    else:
        print("Match Found: %d correct position, %d wrong position"%(bull,cow))
    

print("Guessing Game:")
for i in range(5):
    inp=list(input("Enter a 3 digit number: "))
    cow=bull=0
    check(inp,res)
print("You have lost")