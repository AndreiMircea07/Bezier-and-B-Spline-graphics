from GHD.Punct import Punct
def citireCardinal():
    n=int(input("Cate puncte doriti sa introduceti?"))
    return n



def citirePoligon(n):
    print("introduceti varfurile poligonului")
    l=[]
    for i in  range(0,n):
       x=float(input("abscisa:"))
       y=float(input("ordonata:"))
       P=Punct(x,y)
       l.append(P)
    return l 
   
def citireOptiune():
    op=int(input("Alegeti una dintre optiunile anterioare"))
    return op

def citireParamtru():
    p=float(input("parametru(subunitar):"))
    return p

def citireSirParametrii(n):
    param=[]
    for i in range (1,n):
        t=float(input("parametru:"))
        param.append(t)
    return param
    
    

def afisareMeniu():
    print("1:Reprezentarea unei punct situat pe curba Bezier a unui poligon oarecare")
    print("2:Reprezentarea curbei Bezier, respectiv a poligonului care o determina si este dat prin capete")
    print("3:Reprezentarea unei curbe Bezier, impreuna cu derivata acesteia")
    print("4:Ridicarea cu o unitate a unei curbe Bezier si reprezentarea acesteia impreuna cu poligoanele aferente")
    print("5:Subdivizarea unei curbe Bezier dupa un parametru dat")
    print("6:Forma polara a curbei intr-un punct dat si reprezentare grafica")
    print("7:De Boor pe o curba BSpline")
    print("8:Descompunerea unei curbe BSpline in curbe Bezier componente")
    
    
    