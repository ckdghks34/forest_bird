def exp(n,s):
    if n==eps:
        s=s+str(n)
        if eval(s) == make: print(s) #eval : str�� int ���·� �ٲپ� ���
        return
    
    for i in op:
        exp(n+1,s+str(n)+i)
    
#driver code
op=['+','-','*','/','']
eps=9
make=100
exp(1,'')