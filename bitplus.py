#input number of operations
#loop how many operations
# to 

op = int(input())
x = 0

for i in range(0,op):
   ops = input()
   if ops == ("X++") or ops == ("++X"):
     x += 1
   else:
      x = x - 1

print(x)