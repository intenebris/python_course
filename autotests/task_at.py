"""
n = 100

def calculateSum(n):
    lng = str(n)
    sum = 0
    for i in range(len(lng)):
        sum = sum + int(lng[i])
    return sum    

res = calculateSum(n)

print(res)
"""

"""
n = 6 -> 1 4 1  
n = 24 -> 4 16 4    
n = 60 -> 10 40 10 

n = 60
p = int(n / 6)
s = p
k = 2 * (p + s)
print(f"{p} {k} {s}")
"""

"""
n = 385916 -> yes
n = 123456 -> no


n = 385916

def checkHuppyNumber(x):
    num = str(x)
    lng = len(num)
    firstSum = 0
    secondSum = 0
    for i in range(int(lng)):
        if i < int(lng / 2):
            firstSum = firstSum + int(num[i])
        else:
            secondSum = secondSum + int(num[i])       
    if  firstSum == secondSum:
        print('yes')
    else:
        print('no')    
       

checkHuppyNumber(n)
"""


"""
a, b, c = 3, 2, 4 -> yes
a, b, c = 3, 2, 1 -> no
"""
a = 3
b = 5
c = 10

def isBreakChoco (a,b,c):
    if c % b == 0 or c % a == 0:
        print('yes')
    else:
        print('no')
        
isBreakChoco (a,b,c)            