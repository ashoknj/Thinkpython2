"""Ackerman function
A(m,n)
n+1   when m=0
A(m-1,1)  if m>0 and n=0
A(m-1,A(m,n-1)) if m>0 and n>0
Evaluate when ack(3,4). it should be 125
"""
def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))

#print(ack(3,4))
#print(ack(2,0))
print(ack(0,0))