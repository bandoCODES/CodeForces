#A team problem

nprob = int(input())
num2 = 0
num3 = 0


for i in range(0,nprob):
  
    line = input()

    lines = line.split()
    for x in range(0,3):
        if lines[x] == "1":
            num2 += 1
    
    if num2 >= 2:
        num3 += 1
    num2 = 0



print(num3)


        
    
# make if lines = 1 a










    # "1 1 0"
    # [1,1,0]
    # ["1","1","0"]



# if   ==  "1"

#get them to input number of how many problems.
#ask  x (each person) yes or no * by nprob
#some how represent then in a way that is readable to print yes or no whether number of 1s is higher than 2



