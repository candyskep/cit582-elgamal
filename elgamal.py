import random

from params import p
from params import g
q=(p-1)/2

def keygen():
    sk=random.randint(1,q)
    pk = pow(g,sk,p)
    #print("g",type(g),"sk",type(sk),"p",type(p))
    return pk,sk

def encrypt(pk,m):
    r = random.randint(1, q)
    #print("g",type(g),"r",type(r),"p",type(p),"pk",type(pk),"m",type(m))
    c1 = pow(g,r,p)
    y1=pow(pk,r,p)
    y2=pow(m,1,p)
    y3=y1*y2
    #print("y3",type(y3))
    c2 = pow(y3,1,p)
    print("m-ini=",m)
    return [c1,c2]

def decrypt(sk,c):
    x1=pow(c[1],1,p)
    #print("c1=",c[0],'\n',"c2=",c[1],'\n',"x1=",x1,'\n',"sk=",sk)
    x2=pow(c[0],-sk,p)
    #print("x2",x2,type(x2))
    x3=x1*x2
    m = pow(x3,1,p)
    print("m-de=",m)
    return m

#pk,sk=keygen()
#print(encrypt(pk,20))





'''import random

from params import p
from params import g
q=(p-1)/2

def keygen():
    sk=random.randint(1,q)
    pk = pow(g,sk,p)
    return pk,sk

def encrypt(pk,m):
    r = random.randint(1, q)
    c1 = pow(g,r,p)
    c2 = pow(pow(pk,r)*m,1,p)
    return [c1,c2]

def decrypt(sk,c):
    x=c[1]*pow(c[0],-sk)
    m = pow(x,1,p)
    return m
    '''

