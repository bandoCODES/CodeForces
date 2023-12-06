new = ""
calc1 = input()
calc1 = calc1.split("+") 
calc1.sort()

for i in range (0,len(calc1)):
    if i == len(calc1)-1:
     new = new + calc1[i]
     break
    else: 
       new += (calc1[i]+"+")
print(new)



