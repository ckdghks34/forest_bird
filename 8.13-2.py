a=[9,5,4,3,2,6,156,441213,52,1]
x=7
msg=('no','yes')
m=0
idx=-1
for i,v in enumerate(a): #index ���� �����۰��� i�� v�� ����
    if x == v: #x�� ���� v(a�� ������ ��)�� ���� ������
        m=1 #m���� 1�� ǥ��
        break #for����Ż��
    else: i=idx #x�� ���� v(a�� ������ ��)�� ���� �ٸ��� i�� idx�� ������ ǥ��
print(i, msg[m])