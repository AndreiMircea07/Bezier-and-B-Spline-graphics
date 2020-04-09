from GHD.basicFunctions import *
from GHD.Punct import *
from GHD.Bezier import *
from GHD.UI import *

def main():
    """
    draw_axis(1000)
    P=Punct(50,50)
    DeseneazaPunct(P,"yellow")
    P1=Punct(0,0)
    P2=Punct(0,50)
    DeseneazaPunct(P1,"green")
    DeseneazaPunct(P2,"blue")
    draw_segment(P1, P2)
    P3=Punct(50,50)
    P4=Punct(50,0)
    DeseneazaPunct(P3,"red")
    DeseneazaPunct(P4,"black")
    P5=deCasteljau([P1,P,P3,P4], 0.33)
    DeseneazaPunct(P5,"violet")
    DeseneazaPoligon([P1,P2,P3,P4],"green")
    DeseneazaBezier([P1,P2,P3,P4],"blue")
    DeseneazaPoligon(DeterminaDerivata([P1,P2,P3,P4]),"green")
    DeseneazaBezier(DeterminaDerivata([P1,P2,P3,P4]),"red")
    DeseneazaPoligon(RidicareaGradului([P1,P2,P3,P4]),"violet")
    DeseneazaBezier(RidicareaGradului([P1,P2,P3,P4]),"red")
    
    DeseneazaPoligon(SubdivizareCapete([P1,P2,P3,P4], 0, 0.5), "black")
    DeseneazaPoligon(SubdivizareCapete([P1,P2,P3,P4], 0.5, 1), "black")
    """
    n=citireCardinal()
    l=citirePoligon(n)
    afisareMeniu()
    op=citireOptiune()
    
        
    if op==1:
        t=citireParamtru()
        draw_axis(1000)
        DeseneazaPoligon(l,"green")
        DeseneazaPunct(deCasteljau(l, t),"red")
    elif op==2 :
        draw_axis(1000)
        DeseneazaPoligon(l, "green")
        DeseneazaBezier(l,"red")
            
    elif op==3:
        draw_axis(1000)
        DeseneazaPoligon(l, "green")
        DeseneazaBezier(l,"red")
        DeseneazaPoligon(DeterminaDerivata(l),"black")
        DeseneazaBezier(DeterminaDerivata(l), "orange")
            
    elif op==4:
        draw_axis(1000)
        DeseneazaPoligon(l, "green")
        DeseneazaBezier(l,"red")
        DeseneazaPoligon(RidicareaGradului(l), "blue")
        DeseneazaBezier(RidicareaGradului(l), "pink")
            
    elif op==5:            
        t=citireParamtru()
        draw_axis(1000)
        DeseneazaPoligon(l, "green")
        DeseneazaBezier(l,"red")
        DeseneazaPoligon(SubdivizareCapete(l,0,t),"black")
        DeseneazaBezier(SubdivizareCapete(l, 0, t), "pink")
        DeseneazaPoligon(SubdivizareCapete(l,t,1),"black")
        DeseneazaBezier(SubdivizareCapete(l, t, 1), "pink")
    elif op==6:
        param=citireSirParametrii(n)
        print(FormaPolara(l, param)) 
        draw_axis(1000)       
        DeseneazaPoligon(l, "black")
        DeseneazaPunct(FormaPolara(l, param),"red")
        DeseneazaBezier(l, "brown")
    
    turtle.done()        

main()    