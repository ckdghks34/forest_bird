#Recursive call ����� ȣ��
def strategy(n): #n=���μ�
    if n==0: return #base case Ż������
    strategy(n-1) #inductive case ��������/ �ڱⰡ ���������� �ڽ��� ȣ���� / ���
    print(n) 
    return #��������
    
#driver code
strategy(10) #calling define�� ȣ����/ 10=���μ�