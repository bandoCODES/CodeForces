#Next round
#Problem : create a program to input how many players there are.
# then set a score witch is required to pass on
#then print how many pass
# input =() , #input =() # append to list # read list and do for loop to see who passes and print the number
"""
num1,num2 = input().split()
# enter how many players
 # enter score to pass 
num3 = 0
score2 =[]
score = input().split()

 # gets score
    
for x in range(0,int(num1)):
    if int(score[x]) >= int(num2):
        num3 += 1
"""



# print(num3)


NumbP,Pos = input().split()
num3 = 0
score = input().split()


for mark in score:
    if int(mark) >= int(score[int(Pos)-1]) and int(mark)>0:
        num3 += 1

print(num3)

