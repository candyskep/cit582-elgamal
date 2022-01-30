import random

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

