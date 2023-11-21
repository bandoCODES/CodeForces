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
