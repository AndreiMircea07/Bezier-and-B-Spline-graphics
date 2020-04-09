from GHD.basicFunctions import *

def deCasteljau(l,t):
    s=l.copy()
    n=len(s)
    while n>1:
        for i in range(1,n):
             s[i-1]=PunctRaport(s[i-1],s[i],t)
        n=n-1   
    return s[0]    


def DeseneazaBezier(l,colour):
    
    t=0.02
    while t<=1.00:
        DeseneazaPunct(deCasteljau(l, t),colour)
        draw_segment(deCasteljau(l, t-0.02), deCasteljau(l, t),colour)
        t=t+0.02
        
def DeterminaDerivata(l):
    s=[]
    n=len(l)        
    for i in range(1,len(l)):
        s.append(ScalarProduct(n,PointsDifference(l[i], l[i-1])))
    return s 

def RidicareaGradului(l):
    s=[]
    n=len(l)
    s.append(l[0])
    for i in range(1,n):
        a=i/(n+2)
        s.append(PointsSum(ScalarProduct(1-a,l[i]),ScalarProduct(a,l[i-1])))
    s.append(l[n-1])
    return s 

def SubdivizareCapete(l,c1,c2):
    
    s=l.copy()
    n=len(s)
    m=n
    x=[]
    for k in range(0,m):
        i=1
        while n>=1:
            if i<=k:   
                    for a in range(1,n):
                        s[a-1]=PunctRaport(s[a-1],s[a],c2)
                    n=n-1 
            else:
                    for a in range(1,n):
                        s[a-1]=PunctRaport(s[a-1],s[a],c1)
                    n=n-1
            i=i+1        
        x.append(s[0])
        s=l.copy()
        n=m         
    return x    

def FormaPolara(l,param):
    s=l.copy()
    n=len(s)
    m=n
    for i in range(m-2,-1,-1):
        for k in range(1,n):
            s[k-1]=PunctRaport(s[k-1],s[k],param[i])
        n=n-1
    return s[0]
                