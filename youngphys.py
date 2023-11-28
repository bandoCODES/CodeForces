
var1 = 0
var2 = 0
var3 = 0

n = int(input())

for i in range (0,n):
    a = input().split()
     
    var1 = var1 + int(a[0])
    var2 = var2 + int(a[1])
    var3 = var3 + int(a[2])

if var1 == 0 and var2 == 0 and var3 == 0:
    print("YES")
else:
    print("NO")