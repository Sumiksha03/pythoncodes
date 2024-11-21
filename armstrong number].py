#Program for armstrong number
n=int(input('n: '))
l=[]
s=str(n)
a=len(s)
sum=0
for i in s:
    l.append(i)
for j in l:
    sum+=int(j)**a
if sum==n:
    print('armstrong number')
else:
    print('not an armstrong number')
