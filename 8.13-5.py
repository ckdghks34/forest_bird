def search(low,high):
    if low>high:    #Ż������
        return -1
    mid=(low+high)//2   #�߾Ӱ�
    if s==a[mid]:       
        return mid
    elif s < a[mid]:
        return search(low,mid-1)
    else:
        return search(mid+1, high)


#driver code
a=[5,1,9,4,6,8]
a.sort()
n=len(a) #a�� ����
s=6 #ã����� ��
idx=search(0,n-1)
print(idx)