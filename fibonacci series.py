#fibonacci series
n=int(input('n: '))
a=0
b=1
print(a)
print(b)
for i in range (0,n-2):
    t=a+b
    a=b
    b=t
    print(t)
